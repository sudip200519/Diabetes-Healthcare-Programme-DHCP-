import streamlit as st
import PIL

#######
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
    
