import streamlit as st

# Configure the app
st.set_page_config(
    page_title='Theme Changer App',
    page_icon='🎨',
    layout='wide',
    initial_sidebar_state='auto'
)

# Option to adjust label visibility (for demonstration)
show_label = st.checkbox("Show label for theme selector?", value=False)
label_visibility = "visible" if show_label else "collapsed"

# Theme selector with adjustable label_visibility
theme = st.selectbox(
    "Choose Theme" if show_label else "",  # Label only if visible
    ["🌞 Light", "🌙 Dark"],
    label_visibility=label_visibility
)

# Define theme colors
if theme == "🌞 Light":
    bg_color = "#ffffff"
    text_color = "#000000"
    sidebar_bg = "#f0f2f6"
    header_bg = "#ffffff"
    button_bg = "#e6e6e6"
    button_text = "#000000"
else:  # Dark mode
    bg_color = "#0e1117"
    text_color = "#fafafa"
    sidebar_bg = "#262730"
    header_bg = "#0e1117"
    button_bg = "#2a2d33"
    button_text = "#ffffff"

# Apply custom CSS for theme
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
        transition: all 0.3s ease-in-out;
    }}

    /* Buttons */
    .stButton > button {{
        background-color: {button_bg};
        color: {button_text};
        border: 1px solid {text_color};
        transition: all 0.3s ease-in-out;
    }}

    .stButton > button:hover {{
        background-color: {text_color};
        color: {bg_color};
    }}

    /* Text elements */
    h1, h2, h3, p, span, div {{
        color: {text_color} !important;
        transition: color 0.3s ease-in-out;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.title("Theme Changer Demo")
st.write("Use the checkbox above to toggle the label visibility for the theme selector.")
st.write(f"Current label visibility: **{label_visibility}**")

# Example elements to demonstrate theme
st.header("Sample Header")
st.write("This is some sample text to show how the theme affects colors.")
if st.button("Click Me!"):
    st.success("Button clicked! Theme is working.")

# Sidebar content
st.sidebar.header("Sidebar")
st.sidebar.write("This sidebar also changes with the theme.")
