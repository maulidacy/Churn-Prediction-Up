import joblib
import numpy as np
import pandas as pd
import streamlit as st

from config import MODEL_PATH, PREPROCESSOR_PATH
from data_service import load_dataset, get_reference_date, load_selected_features
from preprocess import (
    create_customer_features,
    calculate_iqr_bounds,
    apply_iqr_capping,
    align_features,
)


@st.cache_resource(show_spinner=False)
def load_assets():
    """
    Load model dan preprocessing pipeline.

    File best_model.pkl pada project ini berbentuk dictionary.
    Estimator utama diambil dari key 'best_estimator'.
    Jika preprocessor tersedia di dictionary, gunakan preprocessor dari dictionary.
    Jika tidak tersedia, gunakan file preprocessing_pipeline.pkl.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"File model tidak ditemukan: {MODEL_PATH}")

    loaded_model = joblib.load(MODEL_PATH)

    model_metadata = {}

    if isinstance(loaded_model, dict):
        model_metadata = loaded_model

        if "best_estimator" in loaded_model:
            model = loaded_model["best_estimator"]
        elif "model" in loaded_model:
            model = loaded_model["model"]
        elif "best_model" in loaded_model:
            model = loaded_model["best_model"]
        else:
            raise ValueError(
                "File model berbentuk dictionary, tetapi estimator tidak ditemukan. "
                f"Key yang tersedia: {list(loaded_model.keys())}"
            )

        if "preprocessor" in loaded_model:
            preprocessor = loaded_model["preprocessor"]
        else:
            if not PREPROCESSOR_PATH.exists():
                raise FileNotFoundError(
                    f"File preprocessing pipeline tidak ditemukan: {PREPROCESSOR_PATH}"
                )
            preprocessor = joblib.load(PREPROCESSOR_PATH)

    else:
        model = loaded_model

        if not PREPROCESSOR_PATH.exists():
            raise FileNotFoundError(
                f"File preprocessing pipeline tidak ditemukan: {PREPROCESSOR_PATH}"
            )

        preprocessor = joblib.load(PREPROCESSOR_PATH)

    if not hasattr(model, "predict"):
        raise TypeError(
            f"Object model tidak memiliki method predict(). Tipe object: {type(model)}"
        )

    return model, preprocessor, model_metadata


@st.cache_data(show_spinner=False)
def load_iqr_bounds():
    """
    Membuat bounds IQR dari dataset raw sebagai fallback.
    Jika bounds sudah tersedia di best_model.pkl, bagian ini tidak dipakai.
    """
    df = load_dataset()

    if df.empty:
        return {}

    if "churn" in df.columns:
        df = df.drop(columns=["churn"])

    features = create_customer_features(df, get_reference_date())

    return calculate_iqr_bounds(features)


def _to_feature_dataframe(transformed, preprocessor) -> pd.DataFrame:
    """
    Mengubah hasil transform pipeline menjadi DataFrame bernama kolom.
    Nama kolom penting agar selected_features dapat dipilih dengan benar.
    """
    try:
        feature_names = preprocessor.get_feature_names_out()
        return pd.DataFrame(transformed, columns=feature_names)
    except Exception:
        return pd.DataFrame(transformed)


def predict_customer(input_df: pd.DataFrame) -> dict:
    """
    Alur prediksi:
    1. Load model final dan preprocessor.
    2. Feature engineering dari input user.
    3. Outlier capping.
    4. Transformasi menggunakan preprocessing pipeline.
    5. Seleksi fitur jika model memakai selected_features.
    6. Prediksi churn.
    """
    model, preprocessor, model_metadata = load_assets()

    # Ambil reference date dari metadata model jika tersedia.
    # Ini lebih konsisten dengan proses training.
    reference_date = model_metadata.get("reference_date", None)

    if reference_date is None:
        reference_date = get_reference_date()

    # Feature engineering mengikuti proses notebook.
    features = create_customer_features(input_df, reference_date)

    # Ambil IQR bounds dari metadata model jika tersedia.
    # Jika tidak ada, gunakan fallback dari dataset raw.
    iqr_bounds = model_metadata.get("iqr_bounds", None)

    if iqr_bounds is None:
        iqr_bounds = load_iqr_bounds()

    if iqr_bounds:
        features = apply_iqr_capping(features, iqr_bounds)

    # Transform input menggunakan preprocessor.
    transformed = preprocessor.transform(features)
    transformed_df = _to_feature_dataframe(transformed, preprocessor)

    # Ambil selected features dari metadata model jika tersedia.
    selected_features = model_metadata.get("selected_features", None)

    if selected_features is None:
        selected_features = load_selected_features()

    # Sesuaikan fitur dengan model.
    model_input = align_features(
        transformed_df=transformed_df,
        model=model,
        selected_features=selected_features,
    )

    prediction = int(model.predict(model_input)[0])

    probability = None
    confidence = None

    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(model_input)[0]

        if len(proba) >= 2:
            probability = float(proba[1])
            confidence = float(max(proba))

    elif hasattr(model, "decision_function"):
        score = float(model.decision_function(model_input)[0])
        probability = float(1 / (1 + np.exp(-score)))
        confidence = probability if prediction == 1 else 1 - probability

    return {
        "prediction": prediction,
        "probability": probability,
        "confidence": confidence,
    }