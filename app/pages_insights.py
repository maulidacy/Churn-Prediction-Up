import streamlit as st

from charts import bar_chart
from data_service import load_dataset
from ui_components import page_header


def render_customer_insights():
    page_header(
        "Customer Insights",
        "Ringkasan insight bisnis dari perilaku pelanggan, engagement, kepuasan, dan potensi retensi.",
        "Business Intelligence",
    )

    df = load_dataset()

    if df.empty:
        st.error("Dataset tidak ditemukan.")
        return

    churn_rate = df["churn"].mean() if "churn" in df.columns else 0

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            f"""
            <div class="insight-card">
                <b>Churn Risk Segmentation</b><br>
                Churn rate pada dataset adalah <b>{churn_rate:.2%}</b>.
                Segmentasi pelanggan berisiko dapat difokuskan pada pelanggan dengan kepuasan rendah,
                interaksi rendah, atau riwayat support ticket tinggi.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="insight-card">
                <b>Retention Recommendation</b><br>
                Strategi retensi dapat diarahkan pada follow-up pelanggan berisiko, evaluasi keluhan,
                peningkatan engagement email, dan penawaran yang relevan.
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3, col4 = st.columns(2, gap="medium")

    with col3:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Churn by Subscription Type</div>
                <div class="card-desc">Rata-rata churn berdasarkan tipe subscription.</div>
            """,
            unsafe_allow_html=True,
        )

        if {"subscription_type", "churn"}.issubset(df.columns):
            series = (
                df.groupby("subscription_type")["churn"]
                .mean()
                .sort_values(ascending=False)
            )

            bar_chart(
                series,
                "Churn Rate by Subscription Type",
                "",
                "Churn Rate",
            )
        else:
            st.info("Kolom subscription_type/churn tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Churn by Acquisition Channel</div>
                <div class="card-desc">Rata-rata churn berdasarkan channel akuisisi.</div>
            """,
            unsafe_allow_html=True,
        )

        if {"acquisition_channel", "churn"}.issubset(df.columns):
            series = (
                df.groupby("acquisition_channel")["churn"]
                .mean()
                .sort_values(ascending=False)
            )

            bar_chart(
                series,
                "Churn Rate by Acquisition Channel",
                "",
                "Churn Rate",
            )
        else:
            st.info("Kolom acquisition_channel/churn tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Executive Summary")

    st.markdown(
        """
        <div class="content-card">
            <div class="card-title">Business Interpretation</div>
            <div class="card-desc">
                Insight utama dari project ini adalah prediksi churn tidak cukup hanya dilihat dari satu fitur.
                Model mempertimbangkan kombinasi perilaku pelanggan, transaksi, interaksi marketing, dan kepuasan.
                Hasil prediksi dapat membantu tim bisnis menentukan pelanggan mana yang perlu diprioritaskan untuk retensi.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )