import streamlit as st


def apply_styles():
    """
    Styling utama aplikasi.
    Desain dibuat modern, responsif, tanpa gradient, dan tanpa asset eksternal.
    """
    st.markdown(
        """
        <style>
        :root {
            --bg: #F8FAFC;
            --surface: #FFFFFF;
            --navy: #0F172A;
            --navy-2: #111827;
            --slate: #334155;
            --muted: #64748B;
            --border: #E2E8F0;

            --blue: #2563EB;
            --blue-dark: #1D4ED8;
            --green: #16A34A;
            --orange: #F97316;
            --purple: #7C3AED;
            --red: #DC2626;
            --cyan: #0891B2;

            --blue-soft: #EFF6FF;
            --green-soft: #ECFDF3;
            --orange-soft: #FFF7ED;
            --purple-soft: #F5F3FF;
            --red-soft: #FEF2F2;

            --shadow: 0 10px 28px rgba(15, 23, 42, 0.07);
        }

        html, body, [class*="css"] {
            font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        .stApp {
            background: var(--bg);
            color: var(--navy);
        }

        .block-container {
            max-width: 1220px;
            padding-top: 4.5rem;
            padding-left: 2rem;
            padding-right: 2rem;
            padding-bottom: 2.5rem;
        }

        /* Header bawaan Streamlit tetap ada agar tombol sidebar mobile tetap muncul */
        header[data-testid="stHeader"] {
            background: #0F172A;
            border-bottom: 1px solid #1E293B;
            height: 3.25rem;
            z-index: 999;
        }

        header[data-testid="stHeader"] button {
            color: #FFFFFF !important;
        }

        button[data-testid="collapsedControl"] {
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
            color: #FFFFFF !important;
        }

        div[data-testid="stDecoration"],
        div[data-testid="stStatusWidget"],
        div[data-testid="stToolbar"] {
            display: none !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #0F172A;
            border-right: 1px solid #1E293B;
        }

        section[data-testid="stSidebar"] > div {
            padding-top: 1.25rem;
        }

        .brand-card {
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 1rem;
            background: #111827;
            border: 1px solid #1E293B;
            box-shadow: none;
        }

        .brand-title {
            font-size: 1rem;
            font-weight: 900;
            color: #FFFFFF;
            margin-bottom: .25rem;
        }

        .brand-subtitle {
            font-size: .82rem;
            line-height: 1.45;
            color: #CBD5E1;
        }

        /* Sidebar menu */
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            background: transparent;
            border: 1px solid transparent;
            border-radius: 14px;
            padding: .65rem .75rem;
            margin-bottom: .35rem;
            transition: all .16s ease;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: #172554;
            border-color: #1D4ED8;
            transform: translateX(2px);
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label p {
            color: #E2E8F0 !important;
            font-size: .95rem;
            font-weight: 600;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
            background: #2563EB;
            border-color: #2563EB;
            box-shadow: 0 8px 18px rgba(37, 99, 235, 0.28);
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
            color: #FFFFFF !important;
            font-weight: 800;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] input {
            display: none;
        }

        /* Page header */
        .page-header {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 1.35rem 1.5rem;
            box-shadow: var(--shadow);
            margin-top: 1rem;
            margin-bottom: 1.2rem;
            position: relative;
            overflow: hidden;
        }

        .page-header::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            width: 7px;
            height: 100%;
            background: var(--blue);
        }

        .page-header .eyebrow {
            color: var(--blue);
            font-weight: 900;
            font-size: .76rem;
            text-transform: uppercase;
            letter-spacing: .1em;
            margin-bottom: .35rem;
        }

        .page-header h1 {
            margin: 0;
            color: var(--navy);
            font-size: clamp(1.8rem, 3vw, 2.6rem);
            line-height: 1.1;
            letter-spacing: -0.035em;
        }

        .page-header p {
            margin: .7rem 0 0 0;
            color: var(--muted);
            max-width: 820px;
            line-height: 1.65;
            font-size: 1rem;
        }

        /* KPI cards */
        .metric-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: .9rem 1rem;
            box-shadow: var(--shadow);
            min-height: 110px;
            position: relative;
            overflow: hidden;
            margin-bottom: .55rem;
        }

        .metric-card::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 5px;
            background: var(--blue);
        }

        .metric-card.blue::before { background: var(--blue); }
        .metric-card.green::before { background: var(--green); }
        .metric-card.orange::before { background: var(--orange); }
        .metric-card.purple::before { background: var(--purple); }
        .metric-card.red::before { background: var(--red); }
        .metric-card.cyan::before { background: var(--cyan); }

        .metric-label {
            color: var(--muted);
            font-size: .86rem;
            font-weight: 700;
            margin-bottom: .55rem;
        }

        .metric-value {
            color: var(--navy);
            font-size: clamp(1.25rem, 2vw, 1.55rem);
            font-weight: 900;
            line-height: 1.2;
            margin-bottom: .3rem;
            word-break: normal;
        }

        .metric-hint {
            color: var(--muted);
            font-size: .82rem;
            line-height: 1.45;
        }

        /* Content cards */
        .chart-card,
        .content-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 1rem;
            box-shadow: var(--shadow);
            margin-bottom: 1rem;
        }

        .card-title {
            color: var(--navy);
            font-size: 1.08rem;
            font-weight: 900;
            margin-bottom: .2rem;
        }

        .card-desc {
            color: var(--muted);
            font-size: .9rem;
            margin-bottom: .9rem;
            line-height: 1.55;
        }

        .insight-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-left: 6px solid var(--purple);
            border-radius: 20px;
            padding: 1rem;
            box-shadow: var(--shadow);
            margin-bottom: .8rem;
            color: var(--slate);
            line-height: 1.6;
        }

        .result-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 1.25rem;
            box-shadow: var(--shadow);
            margin-top: 1rem;
        }

        .badge {
            display: inline-flex;
            padding: .35rem .75rem;
            border-radius: 999px;
            font-size: .82rem;
            font-weight: 900;
            margin-bottom: .6rem;
        }

        .badge-safe {
            color: var(--green);
            background: var(--green-soft);
        }

        .badge-danger {
            color: var(--red);
            background: var(--red-soft);
        }

        .badge-warning {
            color: #B45309;
            background: var(--orange-soft);
        }

        /* Form */
        div[data-testid="stForm"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 1rem;
            box-shadow: var(--shadow);
        }

        /* Form labels */
            div[data-testid="stForm"] label,
            div[data-testid="stForm"] label p,
            div[data-testid="stForm"] label span,
            div[data-testid="stForm"] [data-testid="stWidgetLabel"],
            div[data-testid="stForm"] [data-testid="stWidgetLabel"] p,
            div[data-testid="stForm"] [data-testid="stWidgetLabel"] span {
                color: #334155 !important;
                opacity: 1 !important;
                font-weight: 700 !important;
            }

            /* Help text / caption inside form */
            div[data-testid="stForm"] small,
            div[data-testid="stForm"] .stCaptionContainer,
            div[data-testid="stForm"] .stCaptionContainer p {
                color: #64748B !important;
                opacity: 1 !important;
            }

            /* Text input, number input, date input */
            div[data-testid="stForm"] input {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border-color: #CBD5E1 !important;
                caret-color: #0F172A !important;
            }

            /* Input wrapper */
            div[data-testid="stForm"] div[data-baseweb="input"] {
                background-color: #FFFFFF !important;
                border-color: #CBD5E1 !important;
            }

            div[data-testid="stForm"] div[data-baseweb="input"] > div {
                background-color: #FFFFFF !important;
                border-color: #CBD5E1 !important;
            }

            /* Selectbox */
            div[data-testid="stForm"] div[data-baseweb="select"] > div {
                background-color: #FFFFFF !important;
                border-color: #CBD5E1 !important;
            }

            div[data-testid="stForm"] div[data-baseweb="select"] span,
            div[data-testid="stForm"] div[data-baseweb="select"] div {
                color: #0F172A !important;
            }

            /* Number input minus/plus button */
            div[data-testid="stForm"] div[data-testid="stNumberInput"] button {
                background-color: #F8FAFC !important;
                color: #0F172A !important;
                border-color: #CBD5E1 !important;
            }

            div[data-testid="stForm"] div[data-testid="stNumberInput"] button * {
                color: #0F172A !important;
            }

            /* Date input */
            div[data-testid="stForm"] div[data-baseweb="datepicker"] input {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
            }

            /* Expander title */
            details[data-testid="stExpander"] summary,
            details[data-testid="stExpander"] summary p,
            details[data-testid="stExpander"] summary span {
                color: #0F172A !important;
                font-weight: 800 !important;
            }

            /* Markdown heading inside form */
            div[data-testid="stForm"] h1,
            div[data-testid="stForm"] h2,
            div[data-testid="stForm"] h3,
            div[data-testid="stForm"] h4 {
                color: #0F172A !important;
            }

        /* Dataframe */
        div[data-testid="stDataFrame"] {
            border-radius: 18px;
            overflow: hidden;
            border: 1px solid var(--border);
        }

        /* Tabs */
        div[data-baseweb="tab-list"] {
            gap: .55rem;
            border-bottom: none;
            margin-bottom: 1rem;
        }

        button[data-baseweb="tab"] {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 999px !important;
            padding: .55rem 1rem !important;
            box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
        }

        button[data-baseweb="tab"] p,
        button[data-baseweb="tab"] span,
        button[data-baseweb="tab"] div {
            color: #334155 !important;
            font-weight: 700 !important;
            font-size: .92rem !important;
        }

        button[data-baseweb="tab"]:hover {
            background: #EFF6FF !important;
            border-color: #BFDBFE !important;
        }

        button[data-baseweb="tab"]:hover p,
        button[data-baseweb="tab"]:hover span,
        button[data-baseweb="tab"]:hover div {
            color: #1D4ED8 !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: #0F172A !important;
            border-color: #0F172A !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] p,
        button[data-baseweb="tab"][aria-selected="true"] span,
        button[data-baseweb="tab"][aria-selected="true"] div {
            color: #FFFFFF !important;
            font-weight: 800 !important;
        }

        div[data-baseweb="tab-highlight"] {
            background: transparent !important;
        }

        /* Form submit button - selector dibuat paling spesifik */
        div[data-testid="stFormSubmitButton"] button {
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            border: 1px solid #2563EB !important;
            border-radius: 14px !important;
            min-height: 3rem !important;
            width: 100% !important;
            font-weight: 900 !important;
            box-shadow: 0 10px 22px rgba(37, 99, 235, 0.22) !important;
            transition: all 0.15s ease !important;
        }

        div[data-testid="stFormSubmitButton"] button *,
        div[data-testid="stFormSubmitButton"] button p,
        div[data-testid="stFormSubmitButton"] button span,
        div[data-testid="stFormSubmitButton"] button div {
            color: #FFFFFF !important;
            font-weight: 900 !important;
        }

        div[data-testid="stFormSubmitButton"] button:hover {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
            border-color: #1D4ED8 !important;
            transform: translateY(-1px);
        }

        div[data-testid="stFormSubmitButton"] button:hover *,
        div[data-testid="stFormSubmitButton"] button:active *,
        div[data-testid="stFormSubmitButton"] button:focus *,
        div[data-testid="stFormSubmitButton"] button:focus-visible * {
            color: #FFFFFF !important;
        }

        div[data-testid="stFormSubmitButton"] button:active,
        div[data-testid="stFormSubmitButton"] button:focus,
        div[data-testid="stFormSubmitButton"] button:focus-visible {
            background-color: #1E40AF !important;
            color: #FFFFFF !important;
            border-color: #1E40AF !important;
            box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.18) !important;
        }

        .small-muted {
            color: var(--muted);
            font-size: .9rem;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 3.75rem;
                padding-bottom: 1.5rem;
            }

            .page-header {
                padding: 1rem;
                margin-top: .75rem;
                margin-bottom: .85rem;
            }

            .page-header h1 {
                font-size: 1.55rem;
            }

            .metric-card {
                min-height: 96px;
                margin-bottom: .55rem;
                padding: .85rem 1rem;
            }

            .metric-value {
                font-size: 1.35rem;
                white-space: normal;
            }

            .chart-card,
            .content-card,
            .result-card {
                padding: .9rem;
                margin-bottom: .85rem;
            }

            .prediction-metric-grid {
                grid-template-columns: 1fr;
            }

            .prediction-card,
            .prediction-metric-card,
            .recommendation-card {
                padding: 1rem;
            }

            .prediction-metric-value {
                font-size: 1.6rem;
            }
        }

        /* Prediction result */
        .prediction-section {
            margin-top: 1rem;
        }

        .prediction-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 22px;
            padding: 1.5rem;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.07);
            margin-bottom: 1rem;
        }

        .prediction-card.safe {
            border-left: 7px solid #16A34A;
        }

        .prediction-card.danger {
            border-left: 7px solid #DC2626;
        }

        .prediction-card h2 {
            color: #0F172A !important;
            font-size: clamp(1.8rem, 3vw, 2.6rem);
            line-height: 1.15;
            margin: .8rem 0 .75rem 0;
            font-weight: 900;
        }

        .prediction-card p {
            color: #334155 !important;
            font-size: 1.02rem;
            line-height: 1.65;
            margin: 0;
        }

        .risk-badge {
            display: inline-flex;
            align-items: center;
            padding: .42rem .9rem;
            border-radius: 999px;
            font-size: .88rem;
            font-weight: 900;
        }

        .risk-badge.safe {
            color: #15803D !important;
            background: #DCFCE7;
        }

        .risk-badge.danger {
            color: #B91C1C !important;
            background: #FEE2E2;
        }

        .prediction-metric-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .prediction-metric-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 20px;
            padding: 1.1rem;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
        }

        .prediction-metric-label {
            color: #64748B !important;
            font-size: .92rem;
            font-weight: 800;
            margin-bottom: .35rem;
        }

        .prediction-metric-value {
            color: #0F172A !important;
            font-size: 2rem;
            font-weight: 900;
            margin-bottom: .65rem;
        }

        .prediction-metric-desc {
            color: #64748B !important;
            font-size: .9rem;
            line-height: 1.5;
        }

        .progress-track {
            width: 100%;
            height: 12px;
            background: #E2E8F0;
            border-radius: 999px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            border-radius: 999px;
        }

        .progress-fill.safe {
            background: #16A34A;
        }

        .progress-fill.danger {
            background: #DC2626;
        }

        .recommendation-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-left: 7px solid #2563EB;
            border-radius: 20px;
            padding: 1.1rem;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.05);
        }

        .recommendation-title {
            color: #0F172A !important;
            font-size: 1rem;
            font-weight: 900;
            margin-bottom: .35rem;
        }

        .recommendation-card p {
            color: #334155 !important;
            font-size: .98rem;
            line-height: 1.6;
            margin: 0;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )