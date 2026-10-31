
import streamlit as st


def apply_theme():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* GLOBAL THEME */

    html, body, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], .stApp {
        background-color: #F8F7FC !important;
        color: #29263D !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* MAIN CONTENT */

    [data-testid="stMainBlockContainer"] {
        padding: 2.5rem 3rem 3rem 3rem;
        max-width: 1500px;
    }

    /* TYPOGRAPHY */

    h1, h2, h3 {
        color: #29263D !important;
        font-family: 'Inter', sans-serif !important;
    }

    h1 {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        letter-spacing: -1px !important;
    }

    h2 {
        font-size: 1.55rem !important;
        font-weight: 700 !important;
    }

    h3 {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        color: #403B58 !important;
    }

    p, label, .stCaption {
        color: #817995;
        font-family: 'Inter', sans-serif !important;
    }

    /* SIDEBAR */

    [data-testid="stSidebar"] {
        background-color: #EAE6F5 !important;
        border-right: 1px solid #DDD5ED !important;
    }

    [data-testid="stSidebar"] * {
        color: #29263D !important;
        font-family: 'Inter', sans-serif !important;
    }

    [data-testid="stSidebar"] a {
        border-radius: 10px !important;
        transition: background-color 0.2s ease;
    }

    [data-testid="stSidebar"] a:hover {
        background-color: #DCD4ED !important;
    }

    [data-testid="stSidebar"] a[aria-current="page"] {
        background-color: #D5CBEA !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
    }

    /* METRIC CARDS */

    [data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E5E0EF !important;
        padding: 22px !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 16px rgba(41, 38, 61, 0.045);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 7px 20px rgba(41, 38, 61, 0.08);
    }

    [data-testid="stMetricLabel"] {
        color: #817995 !important;
        font-weight: 600 !important;
    }

    [data-testid="stMetricValue"] {
        color: #29263D !important;
        font-weight: 800 !important;
    }

    /* INPUT FIELDS */

    .stTextInput input,
    .stNumberInput input,
    .stDateInput input,
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #29263D !important;
        border: 1px solid #DDD5ED !important;
        border-radius: 10px !important;
    }

    .stTextInput input:focus,
    .stNumberInput input:focus,
    .stTextArea textarea:focus {
        border-color: #9484BD !important;
        box-shadow: 0 0 0 2px rgba(148, 132, 189, 0.15) !important;
    }

    /* SELECT BOXES */

    [data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border-color: #DDD5ED !important;
        border-radius: 10px !important;
    }

    [data-baseweb="select"] * {
        color: #29263D !important;
    }

    /* BUTTONS */

.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button,
[data-testid="stPageLink"] a {
    background-color: #DCD4ED !important;
    color: #29263D !important;
    border: 1px solid #C9BDE1 !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    transition: all 0.2s ease;
}

.stButton > button *,
.stFormSubmitButton > button *,
.stDownloadButton > button *,
[data-testid="stPageLink"] a * {
    color: #29263D !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover,
[data-testid="stPageLink"] a:hover {
    background-color: #C9BDE1 !important;
    color: #29263D !important;
}

    /* FORMS */

    [data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E5E0EF !important;
        padding: 25px !important;
        border-radius: 16px !important;
        box-shadow: 0 3px 14px rgba(41, 38, 61, 0.035);
    }

    /* DATAFRAMES */

    [data-testid="stDataFrame"] {
        border: 1px solid #E5E0EF !important;
        border-radius: 12px !important;
        overflow: hidden;
    }

    /* PROGRESS BARS */

    [data-testid="stProgressBar"] > div > div {
        background-color: #9484BD !important;
    }

    [data-testid="stProgressBar"] {
        background-color: #EAE6F5 !important;
    }

    /* ALERTS */

    [data-testid="stAlert"] {
        border-radius: 12px !important;
        border: 1px solid #E5E0EF !important;
    }

    /* CHECKBOXES */

    [data-testid="stCheckbox"] label {
        color: #403B58 !important;
    }

    /* DIVIDERS */

    hr {
        border-color: #E5E0EF !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }

    /* RESPONSIVE SPACING */

    @media (max-width: 768px) {
        [data-testid="stMainBlockContainer"] {
            padding: 1.2rem !important;
        }

        h1 {
            font-size: 1.7rem !important;
        }
    }

    </style>
    """, unsafe_allow_html=True)
