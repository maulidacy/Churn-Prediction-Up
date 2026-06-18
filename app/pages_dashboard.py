import streamlit as st

from charts import bar_chart
from data_service import load_dataset, get_best_model_info
from ui_components import page_header, metric_card


def render_dashboard():
    page_header(
        "Executive Churn Dashboard",
        "Ringkasan performa pelanggan, distribusi churn, segmentasi, dan indikator bisnis utama.",
        "Dashboard",
    )

    df = load_dataset()
    best = get_best_model_info()

    if df.empty:
        st.error(
            "Dataset tidak ditemukan. Pastikan file CSV tersedia di folder data/raw."
        )
        return

    total_customers = len(df)
    churn_rate = df["churn"].mean() if "churn" in df.columns else 0
    best_model = best["model"]
    accuracy = best["accuracy"]

    col1, col2, col3, col4 = st.columns(4, gap="small")

    with col1:
        metric_card(
            "Total Customers",
            f"{total_customers:,}".replace(",", "."),
            "Jumlah data pelanggan",
            color="blue",
        )

    with col2:
        metric_card(
            "Churn Rate",
            f"{churn_rate:.2%}",
            "Proporsi pelanggan churn",
            color="red",
        )

    with col3:
        metric_card(
            "Best Model",
            best_model,
            best["scenario"],
            color="purple",
        )

    with col4:
        metric_card(
            "Model Accuracy",
            f"{float(accuracy):.2%}" if accuracy is not None else "-",
            "Evaluasi model final",
            color="green",
        )

    st.markdown("### Customer Overview")

    col5, col6 = st.columns(2, gap="medium")

    with col5:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Churn Distribution</div>
                <div class="card-desc">Perbandingan pelanggan churn dan tidak churn.</div>
            """,
            unsafe_allow_html=True,
        )

        churn_counts = df["churn"].map({0: "Not Churn", 1: "Churn"}).value_counts()
        bar_chart(churn_counts, "Churn Distribution", "", "Customers")

        st.markdown("</div>", unsafe_allow_html=True)

    with col6:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Subscription Type</div>
                <div class="card-desc">Distribusi pelanggan berdasarkan tipe subscription.</div>
            """,
            unsafe_allow_html=True,
        )

        if "subscription_type" in df.columns:
            bar_chart(
                df["subscription_type"].value_counts(),
                "Subscription Type Distribution",
                "",
                "Customers",
            )
        else:
            st.info("Kolom subscription_type tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    col7, col8 = st.columns(2, gap="medium")

    with col7:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Acquisition Channel</div>
                <div class="card-desc">Sumber akuisisi pelanggan dari aktivitas marketing.</div>
            """,
            unsafe_allow_html=True,
        )

        if "acquisition_channel" in df.columns:
            bar_chart(
                df["acquisition_channel"].value_counts(),
                "Acquisition Channel",
                "",
                "Customers",
            )
        else:
            st.info("Kolom acquisition_channel tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    with col8:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Top Countries</div>
                <div class="card-desc">Distribusi pelanggan berdasarkan negara.</div>
            """,
            unsafe_allow_html=True,
        )

        if "country" in df.columns:
            top_countries = df["country"].value_counts().head(10)
            bar_chart(top_countries, "Top Countries", "", "Customers")
        else:
            st.info("Kolom country tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Business Insight Summary")

    col9, col10, col11 = st.columns(3, gap="medium")

    with col9:
        st.markdown(
            f"""
            <div class="insight-card">
                <b>Churn Overview</b><br>
                Churn rate pada dataset adalah <b>{churn_rate:.2%}</b>.
                Karena kelas churn lebih kecil, evaluasi model perlu melihat F1-score dan recall.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col10:
        st.markdown(
            """
            <div class="insight-card">
                <b>Model Usage</b><br>
                Model terbaik digunakan untuk membantu mengidentifikasi pelanggan yang perlu diprioritaskan dalam strategi retensi.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col11:
        st.markdown(
            """
            <div class="insight-card">
                <b>Business Action</b><br>
                Pelanggan berisiko dapat diberikan follow-up, promo relevan, atau penanganan keluhan lebih cepat.
            </div>
            """,
            unsafe_allow_html=True,
        )