import streamlit as st

from ui_components import page_header


def render_about_project():
    page_header(
        "About Project",
        "Penjelasan singkat tentang tujuan project, dataset, workflow machine learning, dan tools yang digunakan.",
        "Project Documentation",
    )

    st.markdown(
        """
        <div class="content-card">
            <div class="card-title">Project Overview</div>
            <div class="card-desc">
                Project ini membangun sistem prediksi churn pelanggan berbasis machine learning.
                Churn berarti pelanggan berhenti menggunakan layanan atau tidak lagi melakukan aktivitas pembelian.
                Aplikasi ini dibuat untuk membantu mengidentifikasi pelanggan yang berpotensi churn agar dapat
                diprioritaskan dalam strategi retensi.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Dataset")

    st.write(
        """
        Dataset yang digunakan adalah Sales and Marketing Customer Dataset. Dataset ini berisi informasi
        pelanggan seperti data demografis, aktivitas penggunaan layanan, riwayat transaksi, interaksi pemasaran,
        metode pembayaran, serta indikator kepuasan pelanggan. Target prediksi pada project ini adalah kolom
        `churn`, yaitu status apakah pelanggan termasuk churn atau tidak churn.
        """
    )

    st.markdown("### Machine Learning Workflow")

    st.markdown(
        """
        1. **Exploratory Data Analysis (EDA)** untuk memahami kondisi data, distribusi target, missing value, dan pola awal pada fitur.
        2. **Direct Modeling** sebagai baseline awal sebelum preprocessing lebih lanjut.
        3. **Preprocessing Modeling** untuk menangani data kategorikal, numerik, missing value, outlier, dan transformasi fitur.
        4. **Hyperparameter Tuning** untuk mencari konfigurasi model yang lebih optimal.
        5. **Model Comparison** untuk membandingkan performa model dari beberapa skenario eksperimen.
        6. **Streamlit Deployment** untuk menampilkan dashboard, analisis data, evaluasi model, dan fitur prediksi churn.
        """
    )

    st.markdown("### Final Output")

    st.write(
        """
        Output akhir dari project ini adalah aplikasi Streamlit yang dapat digunakan untuk melihat ringkasan dataset,
        analisis data, performa model, insight pelanggan, serta melakukan prediksi churn berdasarkan input data pelanggan.
        """
    )

    st.markdown("### Tools and Technologies")

    st.markdown(
        """
        - Python
        - Pandas
        - NumPy
        - Scikit-learn
        - Joblib
        - Altair
        - Streamlit
        """
    )