import streamlit as st
from web_functions import load_data

from Tabs import diagnosis, home, result,  kc, talk2doc

######

# --- Initialize Session State for Persistence ---
if 'theme' not in st.session_state:
    st.session_state.theme = "Light 🌞"
if 'text_size' not in st.session_state:
    st.session_state.text_size = "Medium"

# --- Layout: Title + Theme Toggle + Text Size ---
col1, col2, col3 = st.columns([6, 2, 2])  # Adjusted columns for the new text size selectbox
with col1:
    st.title("💊 Diabetes HealthCare Programme")
with col2:
    theme = st.selectbox("Theme", ["Light 🌞", "Dark 🌙"], index=["Light 🌞", "Dark 🌙"].index(st.session_state.theme), label_visibility="collapsed")
    st.session_state.theme = theme  # Update session state
with col3:
    text_size = st.selectbox("Text Size", ["Small", "Medium", "Large"], index=["Small", "Medium", "Large"].index(st.session_state.text_size), label_visibility="collapsed")
    st.session_state.text_size = text_size  # Update session state

# --- Theme Color Variables ---
if "Light" in theme:
    bg_color = "#ffffff"
    text_color = "#000000"
    sidebar_bg = "#f0f2f6"
    header_bg = "#ffffff"
    select_bg = "#ffffff"
    select_text = "#000000"
    hover_bg = "#e6e6e6"       # touch effect grey
    border_color = "#d0d0d0"
else:
    bg_color = "#0e1117"
    text_color = "#fafafa"
    sidebar_bg = "#262730"
    header_bg = "#0e1117"
    select_bg = "#1a1d21"
    select_text = "#ffffff"
    hover_bg = "#2a2d31"
    border_color = "#444"

# --- Text Size Variables ---
if text_size == "Small":
    font_size = "12px"
elif text_size == "Medium":
    font_size = "16px"
else:  # Large
    font_size = "20px"

# --- Apply Custom CSS ---
st.markdown(
    f"""
    <style>
    /* Main background */
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

    /* Header bar */
    [data-testid="stHeader"] {{
        background-color: {header_bg} !important;
        color: {text_color} !important;
        border-bottom: 1px solid {border_color};
        transition: all 0.3s ease-in-out;
    }}

    /* Text (with dynamic font size) */
    h1, h2, h3, p, span, div {{
        color: {text_color} !important;
        font-size: {font_size} !important;  /* Dynamic text size */
        transition: color 0.3s ease-in-out, font-size 0.3s ease-in-out;
    }}

    /* Dropdown main button */
    div[data-baseweb="select"] > div {{
        background-color: {select_bg};
        color: {select_text};
        border-radius: 8px;
        padding: 6px 10px;
        border: 1px solid {border_color};
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
    }}
    div[data-baseweb="select"] > div:hover {{
        background-color: {hover_bg};
        cursor: pointer;
    }}

    /* Dropdown options container */
    div[data-baseweb="popover"] {{
        background-color: {select_bg} !important;
        border-radius: 10px;
        border: 1px solid {border_color};
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        padding: 6px;
        transition: all 0.3s ease-in-out;
    }}

    /* Dropdown individual options (smaller text, left-aligned) */
    div[data-baseweb="option"] {{
        background-color: {select_bg};
        color: {select_text};
        border-radius: 6px;
        padding: 8px 12px;
        margin-bottom: 4px;
        font-size: 14px;  /* Smaller text size */
        text-align: left;  /* Left-aligned for better positioning */
        transition: all 0.2s ease-in-out;
    }}
    div[data-baseweb="option"]:hover {{
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
