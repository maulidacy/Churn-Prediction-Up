import streamlit as st

from charts import (
    histogram_chart,
    box_chart_by_churn,
    heatmap_chart,
    horizontal_bar_chart,
)
from data_service import load_dataset, load_feature_importance
from ui_components import page_header


def render_data_analysis():
    page_header(
        "Data Analysis",
        "Eksplorasi data pelanggan untuk memahami missing value, distribusi, korelasi, dan fitur penting.",
        "Exploratory Data Analysis",
    )

    df = load_dataset()

    if df.empty:
        st.error("Dataset tidak ditemukan. Pastikan file tersedia di data/raw.")
        return

    with st.expander("Filter Data", expanded=False):
        col1, col2 = st.columns(2, gap="medium")

        with col1:
            country = st.multiselect(
                "Country",
                sorted(df["country"].dropna().unique()) if "country" in df.columns else [],
            )

        with col2:
            subscription = st.multiselect(
                "Subscription Type",
                sorted(df["subscription_type"].dropna().unique()) if "subscription_type" in df.columns else [],
            )

    filtered = df.copy()

    if country and "country" in filtered.columns:
        filtered = filtered[filtered["country"].isin(country)]

    if subscription and "subscription_type" in filtered.columns:
        filtered = filtered[filtered["subscription_type"].isin(subscription)]

    total_filtered = f"{len(filtered):,}".replace(",", ".")
    total_data = f"{len(df):,}".replace(",", ".")

    st.caption(f"Data ditampilkan: {total_filtered} dari {total_data} pelanggan")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Missing Value Analysis</div>
                <div class="card-desc">Kolom dengan nilai kosong pada dataset.</div>
            """,
            unsafe_allow_html=True,
        )

        missing = (filtered.isnull().mean() * 100).sort_values(ascending=False)
        missing = missing[missing > 0].head(10)

        if len(missing) > 0:
            horizontal_bar_chart(
                missing,
                "Missing Value Percentage",
                "Percentage",
                "Feature",
            )
        else:
            st.success("Tidak ada missing value pada data terfilter.")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Age Distribution</div>
                <div class="card-desc">Distribusi usia pelanggan pada dataset.</div>
            """,
            unsafe_allow_html=True,
        )

        if "age" in filtered.columns:
            histogram_chart(filtered, "age", "Age Distribution")
        else:
            st.info("Kolom age tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="medium")

    with col3:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Total Spent vs Churn</div>
                <div class="card-desc">Perbandingan total transaksi berdasarkan status churn.</div>
            """,
            unsafe_allow_html=True,
        )

        if {"total_spent", "churn"}.issubset(filtered.columns):
            box_chart_by_churn(
                filtered,
                "total_spent",
                "Total Spent by Churn",
            )
        else:
            st.info("Kolom total_spent atau churn tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown(
            """
            <div class="chart-card">
                <div class="card-title">Satisfaction Score vs Churn</div>
                <div class="card-desc">Perbandingan kepuasan pelanggan berdasarkan status churn.</div>
            """,
            unsafe_allow_html=True,
        )

        if {"satisfaction_score", "churn"}.issubset(filtered.columns):
            box_chart_by_churn(
                filtered,
                "satisfaction_score",
                "Satisfaction Score by Churn",
            )
        else:
            st.info("Kolom satisfaction_score atau churn tidak tersedia.")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="chart-card">
            <div class="card-title">Correlation Heatmap</div>
            <div class="card-desc">Korelasi antar fitur numerik pada dataset.</div>
        """,
        unsafe_allow_html=True,
    )

    numeric_df = filtered.select_dtypes(include=["int64", "float64"])

    if numeric_df.shape[1] > 1:
        corr = numeric_df.corr()
        heatmap_chart(corr, "Numeric Feature Correlation")
    else:
        st.info("Fitur numerik tidak cukup untuk membuat heatmap.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="chart-card">
            <div class="card-title">Feature Importance</div>
            <div class="card-desc">Fitur yang paling berpengaruh berdasarkan output model.</div>
        """,
        unsafe_allow_html=True,
    )

    importance = load_feature_importance()

    if not importance.empty and {"feature", "importance"}.issubset(importance.columns):
        top_features = (
            importance
            .sort_values("importance", ascending=False)
            .head(15)
            .set_index("feature")["importance"]
        )

        horizontal_bar_chart(
            top_features,
            "Top Feature Importance",
            "Importance",
            "Feature",
        )
    else:
        st.info("File feature importance belum ditemukan atau format kolom belum sesuai.")

    st.markdown("</div>", unsafe_allow_html=True)