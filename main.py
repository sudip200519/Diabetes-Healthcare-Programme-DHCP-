import streamlit as st
###
import streamlit.components.v1 as components
###
from web_functions import load_data
from Tabs import diagnosis, home, result, kc, talk2doc

# Configure the app (moved to the top for best practices)
st.set_page_config(
    page_title='Diabetes Prediction System',
    page_icon='🥯',
    layout='wide',
    initial_sidebar_state='auto'
    
)
######
# Read HTML file
# Read HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Read CSS
with open("assets/css/styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Inject JS
with open("assets/js/main.js") as f:
    js_code = f.read()

#######
#######
# Theme selector in a column layout (fixed: adjusted column ratios for visibility)
col1, col2 = st.columns([8, 1])  # Changed [0, 2] to [1, 2] for col1 to have some width
with col1:
    # Added a placeholder or label if needed; currently empty as in original
    pass
with col2:
    theme = st.selectbox("Theme", ["🌞", "🌙"], label_visibility="visible")

# --- Theme Color Variables ---
# Fixed: Check for "🌞" (sun emoji) for light mode instead of "Light"
if theme == "🌞":  # Assuming 🌞 is light mode
    bg_color = "#ffffff"
    text_color = "#000000"
    sidebar_bg = "#f0f2f6"
    header_bg = "#7067C7"
    select_bg = "#ffffff"
    select_text = "#000000"
    hover_bg = "#e6e6e6"
    border_color = "#d0d0d0"
else:  # 🌙 for dark mode
    bg_color = "#0e1117"
    text_color = "#fafafa"
    sidebar_bg = "#262730"
    header_bg = "#07023B"
    select_bg = "#1a1d21"
    select_text = "#ffffff"
    hover_bg = "#2a2d33"
    border_color = "#333333"
    size="10"

# --- Apply Custom CSS ---
# Fixed: Removed invalid f-string syntax (extra quotes), corrected CSS errors (e.g., # comment, overflow value)
st.markdown(
f"""
    <style>
    /* Main page background */
    [data-testid="stAppViewContainer"] {{
        background-color: {bg_color};
        color: {text_color};
      border.radius="10"
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
        font-size: 8px !important;
        font-weight: 300 !important;
        letter-spacing: 0.3px;
        color: inherit !important;
    }}

    /* Improve visibility of placeholder and value text */
    div[data-baseweb="select"] div[role="button"] {{
        color: inherit !important;
        font-size: 6px !important;
        font-weight: 250 !important;
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
        border-radius: 4px;
        padding: 5px 5px;
        font-weight: 100;
        margin-top: 5px;
        margin-right: 10px;
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
        overflow: visible;  /* Fixed: Changed 'unhidden' to 'visible' (valid CSS value) */
    }}

    /* Each option inside dropdown */
    li[role="option"] {{
        background-color: {select_bg};
        color: {select_text};
        padding: 10px;
        font-weight: 250;
        transition: background-color 0.2s ease-in-out;
    }}

    li[role="option"]:hover {{
        background-color: {hover_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)
######
# Tabs dictionary
Tabs = {
    "Home": home,
    "Diagnosis": diagnosis,
    "Result": result,
    "Ask Queries": talk2doc,
    "Knowledge Center": kc
}

#######

st.set_page_config(page_title="AI Healthcare", layout="wide")

# CSS Load
with open("assets/css/styles.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# HTML Sidebar Load
with open("index.html", "r", encoding="utf-8") as f:
    html_sidebar = f.read()

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

st.components.v1.html(html_sidebar, height=700, scrolling=True)

page = st.session_state["page"]

# Page content based on selection
if page == "Home":
    st.title("🏠 Home")
elif page == "Diagnosis":
    st.title("🧪 Diagnosis")
elif page == "Result":
    st.title("📊 Result")
elif page == "Ask Queries":
    st.title("💬 Ask Queries")
elif page == "Knowledge Center":
    st.title("📚 Knowledge Center")
######

# Sidebar navigation
"""
st.sidebar.title('Navigation')
page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info('Made with 💙 by Sudip & Raz') """

# Load data (consider adding @st.cache_data for performance if data is large)
df, X, y = load_data()

# Route to the selected tab
# Fixed: Simplified condition from list check to direct equality
if page == "Diagnosis":
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
