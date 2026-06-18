import pandas as pd
import altair as alt
import streamlit as st


COLOR_PALETTE = [
    "#2563EB",
    "#7C3AED",
    "#F97316",
    "#16A34A",
    "#0891B2",
    "#DC2626",
]

TEXT_COLOR = "#0F172A"
MUTED_COLOR = "#64748B"
BORDER_COLOR = "#E2E8F0"
CHART_BG = "#FFFFFF"


def _base_config(chart):
    return (
        chart
        .configure(background=CHART_BG)
        .configure_view(
            fill=CHART_BG,
            stroke=None,
        )
        .configure_axis(
            labelColor=MUTED_COLOR,
            titleColor=MUTED_COLOR,
            gridColor=BORDER_COLOR,
            domainColor=BORDER_COLOR,
            tickColor=BORDER_COLOR,
            labelFontSize=12,
            titleFontSize=12,
        )
        .configure_legend(
            labelColor=MUTED_COLOR,
            titleColor=TEXT_COLOR,
            labelFontSize=12,
            titleFontSize=12,
        )
    )


def bar_chart(series: pd.Series, title: str = "", xlabel: str = "", ylabel: str = ""):
    data = series.reset_index()
    data.columns = ["category", "value"]

    chart = (
        alt.Chart(data)
        .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
        .encode(
            x=alt.X(
                "category:N",
                title=xlabel,
                sort=None,
                axis=alt.Axis(labelAngle=-25),
            ),
            y=alt.Y("value:Q", title=ylabel),
            color=alt.Color(
                "category:N",
                scale=alt.Scale(range=COLOR_PALETTE),
                legend=None,
            ),
            tooltip=[
                alt.Tooltip("category:N", title="Category"),
                alt.Tooltip("value:Q", title="Value", format=",.2f"),
            ],
        )
        .properties(height=320)
    )

    st.altair_chart(_base_config(chart), use_container_width=True, theme=None)


def horizontal_bar_chart(series: pd.Series, title: str = "", xlabel: str = "", ylabel: str = ""):
    data = series.reset_index()
    data.columns = ["category", "value"]

    chart = (
        alt.Chart(data)
        .mark_bar(cornerRadiusTopRight=6, cornerRadiusBottomRight=6)
        .encode(
            y=alt.Y(
                "category:N",
                title=ylabel,
                sort="-x",
            ),
            x=alt.X("value:Q", title=xlabel),
            color=alt.Color(
                "category:N",
                scale=alt.Scale(range=COLOR_PALETTE),
                legend=None,
            ),
            tooltip=[
                alt.Tooltip("category:N", title="Feature"),
                alt.Tooltip("value:Q", title="Value", format=",.2f"),
            ],
        )
        .properties(height=360)
    )

    st.altair_chart(_base_config(chart), use_container_width=True, theme=None)


def histogram_chart(data: pd.DataFrame, column: str, title: str = ""):
    chart_data = data[[column]].dropna()

    chart = (
        alt.Chart(chart_data)
        .mark_bar(
            color="#2563EB",
            cornerRadiusTopLeft=4,
            cornerRadiusTopRight=4,
        )
        .encode(
            x=alt.X(
                f"{column}:Q",
                bin=alt.Bin(maxbins=30),
                title=column,
            ),
            y=alt.Y("count():Q", title="Frequency"),
            tooltip=[
                alt.Tooltip("count():Q", title="Count"),
            ],
        )
        .properties(height=320)
    )

    st.altair_chart(_base_config(chart), use_container_width=True, theme=None)


def box_chart_by_churn(data: pd.DataFrame, column: str, title: str = ""):
    chart_data = data[[column, "churn"]].dropna().copy()
    chart_data["churn_label"] = chart_data["churn"].map(
        {
            0: "Not Churn",
            1: "Churn",
        }
    )

    chart = (
        alt.Chart(chart_data)
        .mark_boxplot(size=55)
        .encode(
            x=alt.X("churn_label:N", title="Churn Status"),
            y=alt.Y(f"{column}:Q", title=column),
            color=alt.Color(
                "churn_label:N",
                scale=alt.Scale(
                    domain=["Not Churn", "Churn"],
                    range=["#16A34A", "#DC2626"],
                ),
                legend=None,
            ),
            tooltip=[
                alt.Tooltip("churn_label:N", title="Status"),
                alt.Tooltip(f"{column}:Q", title=column, format=",.2f"),
            ],
        )
        .properties(height=320)
    )

    st.altair_chart(_base_config(chart), use_container_width=True, theme=None)


def heatmap_chart(corr: pd.DataFrame, title: str = ""):
    corr_data = corr.reset_index().melt(id_vars="index")
    corr_data.columns = ["feature_x", "feature_y", "correlation"]

    chart = (
        alt.Chart(corr_data)
        .mark_rect()
        .encode(
            x=alt.X(
                "feature_y:N",
                title="",
                axis=alt.Axis(labelAngle=-45),
            ),
            y=alt.Y("feature_x:N", title=""),
            color=alt.Color(
                "correlation:Q",
                scale=alt.Scale(scheme="blueorange"),
                title="Correlation",
            ),
            tooltip=[
                alt.Tooltip("feature_x:N", title="Feature X"),
                alt.Tooltip("feature_y:N", title="Feature Y"),
                alt.Tooltip("correlation:Q", title="Correlation", format=".2f"),
            ],
        )
        .properties(height=520)
    )

    st.altair_chart(_base_config(chart), use_container_width=True, theme=None)


def grouped_metrics_chart(results: pd.DataFrame):
    metric_cols = [
        col for col in ["Accuracy", "Precision", "Recall", "F1-Score"]
        if col in results.columns
    ]

    if not metric_cols:
        st.info("Kolom metrik evaluasi tidak tersedia.")
        return

    plot_df = results.copy()

    for col in metric_cols:
        plot_df[col] = pd.to_numeric(plot_df[col], errors="coerce")

    plot_df = plot_df.dropna(subset=metric_cols, how="all")

    if plot_df.empty:
        st.info("Data metrik evaluasi belum tersedia untuk divisualisasikan.")
        return

    if "Scenario" in plot_df.columns and "Model" in plot_df.columns:
        plot_df["Label"] = (
            plot_df["Scenario"].astype(str)
            + " - "
            + plot_df["Model"].astype(str)
        )
    elif "Model" in plot_df.columns:
        plot_df["Label"] = plot_df["Model"].astype(str)
    else:
        plot_df["Label"] = "Model " + (plot_df.index + 1).astype(str)

    melted = plot_df.melt(
        id_vars=["Label"],
        value_vars=metric_cols,
        var_name="Metric",
        value_name="Score",
    )

    heatmap = (
        alt.Chart(melted)
        .mark_rect(cornerRadius=4)
        .encode(
            x=alt.X(
                "Metric:N",
                title="Metric",
                sort=["Accuracy", "Precision", "Recall", "F1-Score"],
            ),
            y=alt.Y(
                "Label:N",
                title="Model",
                sort="-x",
            ),
            color=alt.Color(
                "Score:Q",
                scale=alt.Scale(scheme="blues", domain=[0, 1]),
                title="Score",
            ),
            tooltip=[
                alt.Tooltip("Label:N", title="Model"),
                alt.Tooltip("Metric:N", title="Metric"),
                alt.Tooltip("Score:Q", title="Score", format=".2%"),
            ],
        )
        .properties(height=430)
    )

    text = (
        alt.Chart(melted)
        .mark_text(
            fontSize=12,
            fontWeight="bold",
        )
        .encode(
            x=alt.X(
                "Metric:N",
                sort=["Accuracy", "Precision", "Recall", "F1-Score"],
            ),
            y=alt.Y("Label:N", sort="-x"),
            text=alt.Text("Score:Q", format=".1%"),
            color=alt.condition(
                alt.datum.Score > 0.55,
                alt.value("white"),
                alt.value("#0F172A"),
            ),
        )
    )

    chart = heatmap + text

    st.altair_chart(_base_config(chart), use_container_width=True, theme=None)