import pandas as pd

from config import OUTLIER_COLUMNS


def create_customer_features(data: pd.DataFrame, reference_date) -> pd.DataFrame:
    """
    Feature engineering yang mengikuti notebook:
    - tanggal diubah menjadi durasi dan bulan,
    - coupon_code diubah menjadi indikator,
    - customer_id dan kolom tanggal mentah tidak digunakan langsung.
    """
    data = data.copy()

    data["signup_date"] = pd.to_datetime(data["signup_date"], errors="coerce")
    data["last_purchase_date"] = pd.to_datetime(data["last_purchase_date"], errors="coerce")
    reference_date = pd.to_datetime(reference_date, errors="coerce")

    data["customer_tenure_days"] = (data["last_purchase_date"] - data["signup_date"]).dt.days
    data["days_since_last_purchase"] = (reference_date - data["last_purchase_date"]).dt.days
    data["signup_month"] = data["signup_date"].dt.month
    data["last_purchase_month"] = data["last_purchase_date"].dt.month
    data["has_coupon_code"] = data["coupon_code"].notna().astype(int)

    drop_cols = [
        "customer_id",
        "signup_date",
        "last_purchase_date",
        "coupon_code",
    ]

    data = data.drop(columns=drop_cols, errors="ignore")

    return data


def calculate_iqr_bounds(data: pd.DataFrame) -> dict:
    """Menghitung batas IQR hanya untuk kolom numerik kontinu."""
    bounds = {}
    available_columns = [col for col in OUTLIER_COLUMNS if col in data.columns]

    for col in available_columns:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1

        bounds[col] = {
            "lower_bound": q1 - 1.5 * iqr,
            "upper_bound": q3 + 1.5 * iqr,
        }

    return bounds


def apply_iqr_capping(data: pd.DataFrame, bounds: dict) -> pd.DataFrame:
    """Membatasi nilai ekstrem agar input tetap wajar."""
    data = data.copy()

    for col, limit in bounds.items():
        if col in data.columns:
            data[col] = data[col].clip(
                lower=limit["lower_bound"],
                upper=limit["upper_bound"],
            )

    return data


def align_features(
    transformed_df: pd.DataFrame,
    model,
    selected_features: list[str] | None = None,
) -> pd.DataFrame:
    """
    Menyesuaikan kolom hasil preprocessing dengan fitur yang dibutuhkan model.
    Prioritas pertama memakai feature_names_in_ dari model karena ini paling aman.
    """
    model_features = getattr(model, "feature_names_in_", None)

    if model_features is not None:
        return transformed_df.reindex(columns=list(model_features), fill_value=0)

    if selected_features:
        return transformed_df.reindex(columns=selected_features, fill_value=0)

    return transformed_df