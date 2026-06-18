from pathlib import Path
import pandas as pd
import streamlit as st

from config import (
    DATA_PATH,
    FALLBACK_OPTIONS,
    MODEL_RESULT_CANDIDATES,
    FINAL_SUMMARY_CANDIDATES,
    SELECTED_FEATURE_CANDIDATES,
    FEATURE_IMPORTANCE_CANDIDATES,
    FIGURES_DIR,
)


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    """Membaca dataset raw. Jika file tidak ada, kembalikan DataFrame kosong."""
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)

    return pd.DataFrame()


@st.cache_data(show_spinner=False)
def get_reference_date():
    """Tanggal referensi untuk menghitung days_since_last_purchase."""
    df = load_dataset()

    if not df.empty and "last_purchase_date" in df.columns:
        ref = pd.to_datetime(df["last_purchase_date"], errors="coerce").max()
        if pd.notna(ref):
            return ref

    return pd.Timestamp.today().normalize()


@st.cache_data(show_spinner=False)
def get_options() -> dict:
    """Mengambil opsi input dari dataset agar dropdown sesuai data training."""
    df = load_dataset()

    if df.empty:
        return FALLBACK_OPTIONS

    options = {}

    for col, fallback in FALLBACK_OPTIONS.items():
        if col in df.columns:
            values = (
                df[col]
                .dropna()
                .astype(str)
                .sort_values()
                .unique()
                .tolist()
            )
            options[col] = values if values else fallback
        else:
            options[col] = fallback

    return options


def read_first_existing(paths: list[Path]) -> pd.DataFrame:
    """Membaca file CSV pertama yang ditemukan dari daftar path."""
    for path in paths:
        if path.exists():
            return pd.read_csv(path)

    return pd.DataFrame()


@st.cache_data(show_spinner=False)
def load_model_results() -> pd.DataFrame:
    """Membaca hasil evaluasi model dari beberapa kemungkinan nama file."""
    return read_first_existing(MODEL_RESULT_CANDIDATES)


@st.cache_data(show_spinner=False)
def load_final_summary() -> pd.DataFrame:
    """Membaca ringkasan model final jika tersedia."""
    return read_first_existing(FINAL_SUMMARY_CANDIDATES)


@st.cache_data(show_spinner=False)
def load_selected_features() -> list[str] | None:
    """Membaca selected features jika tersedia dari output notebook tuning."""
    df = read_first_existing(SELECTED_FEATURE_CANDIDATES)

    if df.empty:
        return None

    for col in ["feature", "features", "selected_feature", "selected_features", "Feature"]:
        if col in df.columns:
            return df[col].dropna().astype(str).tolist()

    if df.shape[1] == 1:
        return df.iloc[:, 0].dropna().astype(str).tolist()

    return None


@st.cache_data(show_spinner=False)
def load_feature_importance() -> pd.DataFrame:
    """Membaca feature importance dari file output jika tersedia."""
    df = read_first_existing(FEATURE_IMPORTANCE_CANDIDATES)

    if df.empty:
        return df

    lower_map = {col.lower(): col for col in df.columns}

    if "feature" not in df.columns and "feature" in lower_map:
        df = df.rename(columns={lower_map["feature"]: "feature"})

    if "importance" not in df.columns and "importance" in lower_map:
        df = df.rename(columns={lower_map["importance"]: "importance"})

    return df


def find_figure(keywords: list[str]) -> Path | None:
    """Mencari file gambar berdasarkan keyword nama file."""
    if not FIGURES_DIR.exists():
        return None

    images = (
        list(FIGURES_DIR.glob("*.png"))
        + list(FIGURES_DIR.glob("*.jpg"))
        + list(FIGURES_DIR.glob("*.jpeg"))
    )

    for image in images:
        lower_name = image.name.lower()

        if all(keyword.lower() in lower_name for keyword in keywords):
            return image

    return None


def get_best_model_info() -> dict:
    """Mengambil ringkasan model terbaik dari hasil evaluasi."""
    results = load_model_results()
    summary = load_final_summary()

    info = {
        "model": "Best Model",
        "scenario": "-",
        "accuracy": None,
        "precision": None,
        "recall": None,
        "f1": None,
    }

    if not summary.empty:
        row = summary.iloc[0]

        for col in summary.columns:
            col_lower = col.lower()
            value = row[col]

            if "model" in col_lower:
                info["model"] = str(value)
            elif "scenario" in col_lower:
                info["scenario"] = str(value)
            elif "accuracy" in col_lower:
                info["accuracy"] = value
            elif "precision" in col_lower:
                info["precision"] = value
            elif "recall" in col_lower:
                info["recall"] = value
            elif "f1" in col_lower:
                info["f1"] = value

    if not results.empty:
        metric_col = "F1-Score" if "F1-Score" in results.columns else ("F1" if "F1" in results.columns else None)

        if metric_col:
            best = results.sort_values(metric_col, ascending=False).iloc[0]

            info["model"] = str(best.get("Model", info["model"]))
            info["scenario"] = str(best.get("Scenario", info["scenario"]))
            info["accuracy"] = best.get("Accuracy", info["accuracy"])
            info["precision"] = best.get("Precision", info["precision"])
            info["recall"] = best.get("Recall", info["recall"])
            info["f1"] = best.get(metric_col, info["f1"])

    return info