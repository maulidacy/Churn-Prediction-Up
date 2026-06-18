import streamlit as st

from styles import apply_styles
from ui_components import sidebar_navigation, model_summary_sidebar
from pages_dashboard import render_dashboard
from pages_data_analysis import render_data_analysis
from pages_model_performance import render_model_performance
from pages_prediction import render_churn_prediction
from pages_insights import render_customer_insights
from pages_about import render_about_project


# Konfigurasi halaman harus diletakkan paling awal setelah import.
st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    apply_styles()

    selected_page = sidebar_navigation()
    model_summary_sidebar()

    if selected_page == "Dashboard":
        render_dashboard()

    elif selected_page == "Data Analysis":
        render_data_analysis()

    elif selected_page == "Model Performance":
        render_model_performance()

    elif selected_page == "Churn Prediction":
        render_churn_prediction()

    elif selected_page == "Customer Insights":
        render_customer_insights()

    elif selected_page == "About Project":
        render_about_project()


if __name__ == "__main__":
    main()