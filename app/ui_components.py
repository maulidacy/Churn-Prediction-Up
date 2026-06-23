from datetime import date, timedelta

import numpy as np
import pandas as pd
import streamlit as st

from config import APP_TITLE, APP_SUBTITLE
from data_service import get_options, get_best_model_info


def page_header(title: str, description: str, eyebrow: str = "Analytics Dashboard"):
    """Header halaman yang konsisten di semua page."""
    st.markdown(
        f"""
        <div class="page-header">
            <div class="eyebrow">{eyebrow}</div>
            <h1>{title}</h1>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, hint: str = "", color: str = "blue"):
    """KPI card dengan aksen warna."""
    st.markdown(
        f"""
        <div class="metric-card {color}">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-hint">{hint}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def sidebar_navigation() -> str:
    """Sidebar navigation sederhana, rapi, dan tanpa icon."""
    st.sidebar.markdown(
        f"""
        <div class="brand-card">
            <div class="brand-title">{APP_TITLE}</div>
            <div class="brand-subtitle">{APP_SUBTITLE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    menu = {
        "Dashboard": "Dashboard",
        "Data Analysis": "Data Analysis",
        "Model Performance": "Model Performance",
        "Churn Prediction": "Churn Prediction",
        "Customer Insights": "Customer Insights",
        "About Project": "About Project",
    }

    selected_label = st.sidebar.radio(
        "Navigation",
        options=list(menu.values()),
        label_visibility="collapsed",
    )

    for key, label in menu.items():
        if selected_label == label:
            return key

    return "Dashboard"


def yes_no_input(label: str, key: str) -> int:
    value = st.selectbox(label, ["Tidak", "Ya"], key=key)
    return 1 if value == "Ya" else 0


def prediction_form():
    """
    Form input prediksi pelanggan.

    Semua fitur tetap ditampilkan karena digunakan oleh model.
    Form hanya dirapikan ke dalam beberapa section agar lebih mudah dipahami.
    """
    options = get_options()

    with st.form("churn_prediction_form"):
        st.markdown("### Informasi Pelanggan (Customer Information)")
        st.caption("Data dasar pelanggan yang digunakan untuk membentuk profil pelanggan.")

        col1, col2 = st.columns(2, gap="medium")

        with col1:
            gender = st.selectbox("Jenis Kelamin (gender)", options["gender"])
            age = st.number_input("Umur Pelanggan (age)", min_value=10, max_value=100, value=32, step=1)
            country = st.selectbox("Negara (country)", options["country"])
            city = st.selectbox("Kota (city)", options["city"])

        with col2:
            signup_date = st.date_input(
                "Tanggal Daftar (signup_date)",
                value=date.today() - timedelta(days=365),
            )
            last_purchase_date = st.date_input(
                "Tanggal Pembelian Terakhir (last_purchase_date)",
                value=date.today() - timedelta(days=30),
            )
            device_type = st.selectbox("Jenis Perangkat (device_type)", options["device_type"])
            payment_method = st.selectbox("Metode Pembayaran (payment_method)", options["payment_method"])

        st.markdown("---")

        st.markdown("### Langganan & Promosi (Subscription & Promotion)")
        st.caption("Informasi paket langganan, status premium, serta penggunaan promosi.")

        col3, col4 = st.columns(2, gap="medium")

        with col3:
            subscription_type = st.selectbox(
                "Jenis Langganan (subscription_type)",
                options["subscription_type"],
            )
            is_premium_user = yes_no_input("Pengguna Premium (is_premium_user)", "premium_user")

        with col4:
            discount_used = yes_no_input("Menggunakan Diskon (discount_used)", "discount_used")
            using_coupon = yes_no_input("Menggunakan Kode Kupon (coupon_code)", "using_coupon")

        st.markdown("---")

        st.markdown("### Aktivitas & Transaksi (Activity & Transactions)")
        st.caption("Aktivitas penggunaan layanan dan riwayat transaksi pelanggan.")

        col5, col6, col7 = st.columns(3, gap="medium")

        with col5:
            total_visits = st.number_input("Total Kunjungan (total_visits)", min_value=0, value=25, step=1)
            avg_session_time = st.number_input(
                "Rata-rata Waktu Sesi (avg_session_time)",
                min_value=0.0,
                value=12.5,
                step=0.5,
            )
            pages_per_session = st.number_input(
                "Halaman per Sesi (pages_per_session)",
                min_value=0.0,
                value=4.0,
                step=0.5,
            )

        with col6:
            total_spent = st.number_input(
                "Total Belanja (total_spent)",
                min_value=0.0,
                value=750.0,
                step=50.0,
            )
            avg_order_value = st.number_input(
                "Rata-rata Nilai Pesanan (avg_order_value)",
                min_value=0.0,
                value=120.0,
                step=10.0,
            )
            lifetime_value = st.number_input(
                "Estimasi Nilai Pelanggan (lifetime_value)",
                min_value=0.0,
                value=1200.0,
                step=50.0,
            )

        with col7:
            last_3_month_purchase_freq = st.number_input(
                "Frekuensi Pembelian 3 Bulan Terakhir (last_3_month_purchase_freq)",
                min_value=0,
                value=3,
                step=1,
            )
            support_tickets = st.number_input(
                "Tiket Bantuan/Keluhan (support_tickets)",
                min_value=0,
                value=1,
                step=1,
            )
            delivery_delay_days = st.number_input(
                "Hari Keterlambatan Pengiriman (delivery_delay_days)",
                min_value=0,
                value=2,
                step=1,
            )

        st.markdown("---")

        st.markdown("### Interaksi Marketing (Marketing Interaction)")
        st.caption("Interaksi pelanggan dengan channel akuisisi dan aktivitas email marketing.")

        col8, col9, col10 = st.columns(3, gap="medium")

        with col8:
            acquisition_channel = st.selectbox(
                "Channel Akuisisi (acquisition_channel)",
                options["acquisition_channel"],
            )

        with col9:
            email_open_rate = st.slider(
                "Tingkat Buka Email (email_open_rate)",
                0.0,
                1.0,
                0.45,
                0.01,
            )

        with col10:
            email_click_rate = st.slider(
                "Tingkat Klik Email (email_click_rate)",
                0.0,
                1.0,
                0.12,
                0.01,
            )

        marketing_spend_per_user = st.number_input(
            "Biaya Marketing per Pelanggan (marketing_spend_per_user)",
            min_value=0.0,
            value=45.0,
            step=5.0,
        )

        st.markdown("---")

        st.markdown("### Kepuasan Pelanggan (Customer Satisfaction)")
        st.caption("Indikator kepuasan, loyalitas, refund, dan potensi keluhan pelanggan.")

        col11, col12, col13 = st.columns(3, gap="medium")

        with col11:
            satisfaction_score = st.slider(
                "Skor Kepuasan (satisfaction_score)",
                1.0,
                5.0,
                3.8,
                0.1,
            )

        with col12:
            nps_score = st.slider("Skor NPS/Loyalitas (nps_score)", 0, 10, 7, 1)

        with col13:
            refund_requested = yes_no_input("Permintaan Refund (refund_requested)", "refund_requested")

        submitted = st.form_submit_button(
            "Prediksi Churn Pelanggan",
            use_container_width=True,
        )

    coupon_code = "USED" if using_coupon == 1 else np.nan

    input_df = pd.DataFrame(
        [
            {
                "customer_id": 0,
                "gender": gender,
                "age": age,
                "country": country,
                "city": city,
                "signup_date": signup_date,
                "last_purchase_date": last_purchase_date,
                "acquisition_channel": acquisition_channel,
                "device_type": device_type,
                "subscription_type": subscription_type,
                "is_premium_user": is_premium_user,
                "total_visits": total_visits,
                "avg_session_time": avg_session_time,
                "pages_per_session": pages_per_session,
                "email_open_rate": email_open_rate,
                "email_click_rate": email_click_rate,
                "total_spent": total_spent,
                "avg_order_value": avg_order_value,
                "discount_used": discount_used,
                "coupon_code": coupon_code,
                "support_tickets": support_tickets,
                "refund_requested": refund_requested,
                "delivery_delay_days": delivery_delay_days,
                "payment_method": payment_method,
                "satisfaction_score": satisfaction_score,
                "nps_score": nps_score,
                "marketing_spend_per_user": marketing_spend_per_user,
                "lifetime_value": lifetime_value,
                "last_3_month_purchase_freq": last_3_month_purchase_freq,
            }
        ]
    )

    return submitted, input_df

def render_prediction_result(result: dict):
    """Menampilkan hasil prediksi dengan custom card agar warna teks selalu jelas."""
    prediction = result["prediction"]
    probability = result["probability"]
    confidence = result["confidence"]

    if prediction == 1:
        badge_class = "risk-badge danger"
        result_class = "prediction-card danger"
        label = "Risiko Churn Tinggi"
        title = "Pelanggan Diprediksi Churn"
        description = "Pelanggan ini diprediksi memiliki risiko berhenti menggunakan layanan."
        recommendation = (
            "Prioritaskan pelanggan ini untuk strategi retensi, cek keluhan pelanggan, "
            "dan berikan follow-up personal."
        )
        progress_class = "progress-fill danger"
    else:
        badge_class = "risk-badge safe"
        result_class = "prediction-card safe"
        label = "Risiko Churn Rendah"
        title = "Pelanggan Diprediksi Tidak Churn"
        description = "Pelanggan ini diprediksi masih memiliki kecenderungan bertahan."
        recommendation = (
            "Pertahankan engagement pelanggan melalui komunikasi, pengalaman layanan yang baik, "
            "dan penawaran yang relevan."
        )
        progress_class = "progress-fill safe"

    probability_text = "-"
    probability_width = 0

    if probability is not None:
        probability_text = f"{probability:.2%}"
        probability_width = min(max(probability * 100, 0), 100)

    confidence_text = "-"

    if confidence is not None:
        confidence_text = f"{confidence:.2%}"

    html_parts = [
        '<div class="prediction-section">',
        f'<div class="{result_class}">',
        f'<div class="{badge_class}">{label}</div>',
        f"<h2>{title}</h2>",
        f"<p>{description}</p>",
        "</div>",
        '<div class="prediction-metric-grid">',
        '<div class="prediction-metric-card">',
        '<div class="prediction-metric-label">Probabilitas Churn (churn_probability)</div>',
        f'<div class="prediction-metric-value">{probability_text}</div>',
        '<div class="progress-track">',
        f'<div class="{progress_class}" style="width: {probability_width}%;"></div>',
        "</div>",
        "</div>",
        '<div class="prediction-metric-card">',
        '<div class="prediction-metric-label">Skor Keyakinan Model (confidence_score)</div>',
        f'<div class="prediction-metric-value">{confidence_text}</div>',
        '<div class="prediction-metric-desc">Tingkat keyakinan model terhadap hasil prediksi.</div>',
        "</div>",
        "</div>",
        '<div class="recommendation-card">',
        '<div class="recommendation-title">Rekomendasi (recommendation)</div>',
        f"<p>{recommendation}</p>",
        "</div>",
        "</div>",
    ]

    html = "".join(html_parts)
    st.markdown(html, unsafe_allow_html=True)


def model_summary_sidebar():
    """Ringkasan model final pada bagian bawah sidebar."""
    info = get_best_model_info()

    st.sidebar.divider()
    st.sidebar.markdown("#### Final Model")
    st.sidebar.write(f"**Model:** {info['model']}")
    st.sidebar.write(f"**Scenario:** {info['scenario']}")

    if info["accuracy"] is not None:
        st.sidebar.write(f"**Accuracy:** {float(info['accuracy']):.2%}")

    if info["f1"] is not None:
        st.sidebar.write(f"**F1-Score:** {float(info['f1']):.2%}")