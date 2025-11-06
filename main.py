import streamlit as st
from web_functions import load_data

from Tabs import diagnosis, home, result,  kc, talk2doc

######
col1, col2 = st.columns([8, 2])
with col1:
    st.title("💊 Diabetes HealthCare Programme")
with col2:
    theme = st.selectbox("Theme", ["Light 🌞", "Dark 🌙"], label_visibility="collapsed")

# --- Theme Color Variables ---
if "Light" in theme:
    bg_color = "#ffffff"          # Main background
    text_color = "#000000"        # Text color
    sidebar_bg = "#f0f2f6"        # Sidebar background
    header_bg = "#ffffff"         # Header background (was black)
    select_bg = "#ffffff"         # Dropdown background
    select_text = "#000000"
else:
    bg_color = "#0e1117"
    text_color = "#fafafa"
    sidebar_bg = "#262730"
    header_bg = "#0e1117"
    select_bg = "#1a1d21"
    select_text = "#ffffff"

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

    /* Header (top bar) */
    [data-testid="stHeader"] {{
        background-color: {header_bg} !important;
        color: {text_color} !important;
        border-bottom: 1px solid #ccc;
        transition: all 0.3s ease-in-out;
    }}

    /* Text elements */
    h1, h2, h3, p, span, div {{
        color: {text_color} !important;
        transition: color 0.3s ease-in-out;
    }}

    /* Dropdown (theme select box) */
    div[data-baseweb="select"] > div {{
        background-color: {select_bg};
        color: {select_text};
        border-radius: 10px;
        padding: 4px 6px;
        margin-top: 6px;
        margin-right: 12px;
        transition: all 0.3s ease-in-out;
    }}

    /* Dropdown popover (options list) */
    div[data-baseweb="popover"] {{
        background-color: {select_bg} !important;
        color: {select_text} !important;
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
