import streamlit as st
from web_functions import load_data

from Tabs import diagnosis, home, result,  kc, talk2doc

######
# --- Layout: Title + Theme Toggle ---
col1, col2 = st.columns([8, 2])
with col1:
    st.title("💊 Diabetes HealthCare Programme")
with col2:
    theme = st.selectbox("Theme", ["Light 🌞", "Dark 🌙"], label_visibility="collapsed")

# --- Theme Color Variables ---
if "Light" in theme:
    bg_color = "#ffffff"
    text_color = "#000000"
    sidebar_bg = "#f0f2f6"
    header_bg = "#ffffff"
    select_bg = "#ffffff"
    select_text = "#000000"
    hover_bg = "#e6e6e6"
    border_color = "#d0d0d0"
else:
    bg_color = "#0e1117"
    text_color = "#fafafa"
    sidebar_bg = "#262730"
    header_bg = "#0e1117"
    select_bg = "#1a1d21"
    select_text = "#ffffff"
    hover_bg = "#2a2d33"
    border_color = "#333333"

# --- Apply Custom CSS ---
st.markdown(
    f"""
    <style>
    /* Main page background */
    [data-testid="stAppViewContainer"] {{
        background-color: {bg_color};
        color: {text_color};
        transition: all 0.3s ease-in-out;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg};
        transition: all 0.3s ease-in-out;
    }}

    /* Header */
    [data-testid="stHeader"] {{
        background-color: {header_bg} !important;
        color: {text_color} !important;
        border-bottom: 1px solid {border_color};
        transition: all 0.3s ease-in-out;
    }}

    /* Improve visibility of selected text inside dropdown */
    div[data-baseweb="select"] span {{
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 0.3px;
        color: inherit !important;
    }}

    /* Improve visibility of placeholder and value text */
    div[data-baseweb="select"] div[role="button"] {{
        color: inherit !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        text-align: center;
    }}

    /* Text elements */
    h1, h2, h3, p, span, div {{
        color: {text_color} !important;
        transition: color 0.3s ease-in-out;
    }}

    /* Theme dropdown container */
    div[data-baseweb="select"] > div {{
        background-color: {select_bg};
        color: {select_text};
        border: 1.5px solid {border_color};
        border-radius: 10px;
        padding: 6px 10px;
        font-weight: 500;
        margin-top: 6px;
        margin-right: 12px;
        transition: all 0.3s ease-in-out;
    }}

    /* Hover / focus effect for dropdown */
    div[data-baseweb="select"] > div:hover {{
        background-color: {hover_bg};
        box-shadow: 0px 0px 6px rgba(0,0,0,0.1);
        cursor: pointer;
    }}

    /* Dropdown popover (option list) */
    div[data-baseweb="popover"] {{
        background-color: {select_bg} !important;
        color: {select_text} !important;
        border: 1.5px solid {border_color};
        border-radius: 10px;
        overflow: hidden;
    }}

    /* Each option inside dropdown */
    li[role="option"] {{
        background-color: {select_bg};
        color: {select_text};
        padding: 10px;
        font-weight: 500;
        transition: background-color 0.2s ease-in-out;
    }}

    li[role="option"]:hover {{
        background-color: {hover_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#####

# Configure the app
st.set_page_config(
    page_title = 'Diabetes Prediction System',
    page_icon = '🥯',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)


Tabs = {
    "Home":home,
    "Ask Queries":talk2doc,
    "Diagnosis":diagnosis,
    "Result":result,
    "Knowledge Center":kc
}

st.sidebar.title('Navigation')

page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info('Made with 💙 by Sudip &')

df, X, y = load_data()

if page in ["Diagnosis"]:
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
