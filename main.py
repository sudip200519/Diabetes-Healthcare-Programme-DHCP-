import streamlit as st
from web_functions import load_data

from Tabs import diagnosis, home, result,  kc, talk2doc

# Configure the app
st.set_page_config(
    page_title = 'Diabetes Prediction System',
    page_icon = '🥯',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)
#extra
col1, col2 = st.columns([8, 2])
with col2:
    theme = st.selectbox("Theme", ["Light", "Dark"])

if theme == "Light":
    bg_color = "#ffffff"
    text_color = "#000000"
else:
    bg_color = "#0e1117"
    text_color = "#fafafa"

st.markdown(
    f"""
    <style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)
 # break

Tabs = {
    "Home":home,
    "Ask Queries":talk2doc,
    "Diagnosis":diagnosis,
    "Result":result,
    "Knowledge Center":kc
}

st.sidebar.title('Navigation')

page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info('Made with 💙 by Mainak')

df, X, y = load_data()

if page in ["Diagnosis"]:
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
