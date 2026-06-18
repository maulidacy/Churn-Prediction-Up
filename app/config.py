from pathlib import Path

# Folder utama project.
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "raw" / "Sales - Marketing customer dataset.csv"

MODELS_DIR = BASE_DIR / "models"
MODEL_PATH = MODELS_DIR / "best_model.pkl"
PREPROCESSOR_PATH = MODELS_DIR / "preprocessing_pipeline.pkl"

OUTPUTS_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
REPORTS_DIR = OUTPUTS_DIR / "reports"

# Beberapa notebook bisa menyimpan nama file hasil evaluasi yang berbeda.
MODEL_RESULT_CANDIDATES = [
    REPORTS_DIR / "model_results_all_scenarios.csv",
    REPORTS_DIR / "final_model_ranking.csv",
    REPORTS_DIR / "hyperparameter_tuning_results.csv",
    MODELS_DIR / "model_results.csv",
]

FINAL_SUMMARY_CANDIDATES = [
    REPORTS_DIR / "final_best_model_summary.csv",
    REPORTS_DIR / "best_model_by_scenario.csv",
]

SELECTED_FEATURE_CANDIDATES = [
    REPORTS_DIR / "selected_features_best_tuned_model.csv",
    REPORTS_DIR / "selected_features_best_model.csv",
]

FEATURE_IMPORTANCE_CANDIDATES = [
    REPORTS_DIR / "feature_importance_hyperparameter_tuning.csv",
    REPORTS_DIR / "feature_importance_preprocessing_random_forest.csv",
]

# Fallback digunakan kalau dataset tidak terbaca saat aplikasi dijalankan.
FALLBACK_OPTIONS = {
    "gender": ["Female", "Male", "Other"],
    "country": ["United States", "United Kingdom", "Canada", "Australia", "Germany", "France", "India", "Indonesia"],
    "city": ["New York", "London", "Toronto", "Sydney", "Berlin", "Paris", "Mumbai", "Jakarta"],
    "acquisition_channel": ["Email", "Organic", "Facebook Ads", "Referral", "Google Ads"],
    "device_type": ["Desktop", "Mobile", "Tablet"],
    "subscription_type": ["Basic", "Standard", "Premium"],
    "payment_method": ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "E-Wallet"],
}

# Kolom numerik kontinu untuk capping outlier.
# Kolom biner 0/1 tidak dimasukkan agar nilainya tidak berubah.
OUTLIER_COLUMNS = [
    "age",
    "total_visits",
    "avg_session_time",
    "pages_per_session",
    "email_open_rate",
    "email_click_rate",
    "total_spent",
    "avg_order_value",
    "support_tickets",
    "delivery_delay_days",
    "marketing_spend_per_user",
    "lifetime_value",
    "last_3_month_purchase_freq",
    "customer_tenure_days",
    "days_since_last_purchase",
]

APP_TITLE = "Customer Churn Analytics"
APP_SUBTITLE = "Dashboard analitik dan prediksi churn pelanggan berbasis machine learning."