import streamlit as st
import PIL

#######
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

def app():
    st.title('Integrated Diabetes Health Care Program')
    st.image('./images/diabetic.png')

    
    st.markdown(
    """<p style="font-size:20px;">
            Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
            There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
            This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Random Forest Classifier.
        </p>
    """, unsafe_allow_html=True)
    
