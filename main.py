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
    bg_color = "#ffffff"
    text_color = "#000000"
    sidebar_bg = "#f0f2f6"
else:
    bg_color = "#0e1117"
    text_color = "#fafafa"
    sidebar_bg = "#262730"

# --- Apply Custom CSS ---
st.markdown(
    f"""
    <style>
    /* Main background */
    [data-testid="stAppViewContainer"] {{
        background-color: {bg_color};
        color: {text_color};
    }}
    /* Sidebar background */
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg};
    }}
    /* Header & text color */
    h1, h2, h3, p, span, div {{
        color: {text_color} !important;
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
