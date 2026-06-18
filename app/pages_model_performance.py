import streamlit as st
import pandas as pd

from charts import grouped_metrics_chart, bar_chart
from data_service import load_model_results, get_best_model_info, find_figure
from ui_components import page_header, metric_card


def render_model_performance():
    page_header(
        "Model Performance",
        "Perbandingan performa model dari direct modeling, preprocessing, dan hyperparameter tuning.",
        "Machine Learning Evaluation",
    )

    results = load_model_results()
    best = get_best_model_info()

    if results.empty:
        st.error("File hasil evaluasi model belum ditemukan di outputs/reports atau models.")
        return

    col1, col2, col3, col4 = st.columns(4, gap="small")

    with col1:
        metric_card(
            "Best Model",
            best["model"],
            best["scenario"],
            color="purple",
        )

    with col2:
        metric_card(
            "Accuracy",
            f"{float(best['accuracy']):.2%}" if best["accuracy"] is not None else "-",
            "Model final",
            color="blue",
        )

    with col3:
        metric_card(
            "Recall",
            f"{float(best['recall']):.2%}" if best["recall"] is not None else "-",
            "Kemampuan mendeteksi churn",
            color="orange",
        )

    with col4:
        metric_card(
            "F1-Score",
            f"{float(best['f1']):.2%}" if best["f1"] is not None else "-",
            "Keseimbangan precision dan recall",
            color="green",
        )

    tab1, tab2, tab3 = st.tabs(["Model Table", "Metric Charts", "Confusion Matrix"])

    with tab1:
        st.markdown("### Model Comparison Table")

        display_cols = [
            col
            for col in ["Scenario", "Model", "Accuracy", "Precision", "Recall", "F1-Score"]
            if col in results.columns
        ]

        numeric_format = {
            col: "{:.2%}"
            for col in display_cols
            if col not in ["Scenario", "Model"]
        }

        st.dataframe(
            results[display_cols].style.format(numeric_format),
            use_container_width=True,
        )

    with tab2:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Evaluation Metrics by Model</div>
                <div class="card-desc">
                    Visualisasi perbandingan accuracy, precision, recall, dan F1-score untuk setiap model.
                    Warna yang lebih gelap menunjukkan skor yang lebih tinggi.
                </div>
            """,
            unsafe_allow_html=True,
        )

        grouped_metrics_chart(results)

        st.markdown("</div>", unsafe_allow_html=True)

        if "F1-Score" in results.columns and "Model" in results.columns:
            st.markdown(
                """
                <div class="chart-card">
                    <div class="card-title">Model Ranking by F1 Score</div>
                    <div class="card-desc">
                        Ranking model berdasarkan F1-score untuk melihat model terbaik secara cepat.
                    </div>
                """,
                unsafe_allow_html=True,
            )

            f1_df = results.copy()
            f1_df["F1-Score"] = pd.to_numeric(f1_df["F1-Score"], errors="coerce")
            f1_df = f1_df.dropna(subset=["F1-Score"])

            if "Scenario" in f1_df.columns:
                f1_df["Label"] = (
                    f1_df["Scenario"].astype(str)
                    + " - "
                    + f1_df["Model"].astype(str)
                )
            else:
                f1_df["Label"] = f1_df["Model"].astype(str)

            f1_series = (
                f1_df
                .set_index("Label")["F1-Score"]
                .sort_values(ascending=False)
            )

            bar_chart(
                f1_series,
                "",
                "",
                "F1-Score",
            )

            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("Kolom F1-Score atau Model belum tersedia.")

    with tab3:
        st.markdown("### Confusion Matrix")

        cm_path = find_figure(["confusion", "best"])

        if cm_path is None:
            cm_path = find_figure(["confusion", "tuning"])

        if cm_path is not None:
            st.image(str(cm_path), use_container_width=True)
        else:
            st.info(
                "Gambar confusion matrix tidak ditemukan. Jika sudah ada, pastikan tersimpan di outputs/figures."
            )

        st.markdown("### ROC Curve")

        roc_path = find_figure(["roc"])

        if roc_path is not None:
            st.image(str(roc_path), use_container_width=True)
        else:
            st.info("ROC curve belum tersedia dari output notebook saat ini.")