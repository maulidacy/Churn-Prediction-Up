import streamlit as st

from model_service import predict_customer, load_assets
from ui_components import page_header, prediction_form, render_prediction_result


def render_churn_prediction():
    page_header(
        "Churn Prediction",
        "Masukkan data pelanggan untuk memprediksi apakah pelanggan berpotensi churn atau tidak churn.",
        "AI Prediction Interface",
    )

    try:
        load_assets()
    except FileNotFoundError as error:
        st.error(str(error))
        st.stop()

    submitted, input_df = prediction_form()

    if submitted:
        if input_df.loc[0, "last_purchase_date"] < input_df.loc[0, "signup_date"]:
            st.error("Tanggal pembelian terakhir tidak boleh lebih awal dari tanggal daftar.")
            st.stop()

        with st.spinner("Model sedang memproses prediksi..."):
            result = predict_customer(input_df)

        render_prediction_result(result)