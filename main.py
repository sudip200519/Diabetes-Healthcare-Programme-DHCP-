import streamlit as st
from web_functions import load_data

from Tabs import diagnosis, home, result,  kc, talk2doc

######
# --- Title + Theme Toggle ---
col1, col2 = st.columns([8, 2])
with col1:
    st.title("💊 Diabetes HealthCare Programme")
with col2:
    theme = st.selectbox("Theme", ["Light 🌞", "Dark 🌙"], label_visibility="collapsed")

# --- Theme Variables ---
is_light = "Light" in theme
bg = "#fff" if is_light else "#0e1117"
text = "#000" if is_light else "#fafafa"
sidebar = "#f0f2f6" if is_light else "#262730"
header = bg
select_bg = bg
select_text = text
hover = "#e8e8e8" if is_light else "#2a2d33"
border = "#ccc" if is_light else "#333"

# --- CSS ---
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
  background-color:{bg}; color:{text};
}}
[data-testid="stSidebar"], [data-testid="stHeader"] {{
  background-color:{header} !important; color:{text};
  border-bottom:1px solid {border};
}}
div[data-baseweb="select"] > div {{
  background:{select_bg}; color:{select_text};
  border:1.5px solid {border}; border-radius:8px;
  padding:5px 10px; font-size:15px; width:120px;
}}
div[data-baseweb="select"] > div:hover {{
  background:{hover}; cursor:pointer;
}}
div[data-baseweb="popover"], li[role="option"] {{
  background:{select_bg}; color:{select_text};
  border:1px solid {border};
}}
li[role="option"]:hover {{ background:{hover}; }}
</style>
""", unsafe_allow_html=True)


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
