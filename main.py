import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

# Configure the app
st.set_page_config(
    page_title='Diabetes Healthcare Program',
    page_icon='🥯',
    layout='wide',
    initial_sidebar_state='auto'
)

# Theme selector in columns
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("**Select Theme:**")
with col2:
    theme = st.selectbox("Theme", ["Light🌞", "🌙Dark"], label_visibility="collapsed")

# Theme color variables
if theme == "🌞":
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

# Apply custom CSS
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-color: {bg_color};
        color: {text_color};
        transition: all 0.3s ease-in-out;
    }}
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg};
        transition: all 0.3s ease-in-out;
    }}
    [data-testid="stHeader"] {{
        background-color: {header_bg} !important;
        color: {text_color} !important;
        border-bottom: 1px solid {border_color};
        transition: all 0.3s ease-in-out;
    }}
    h1, h2, h3, p, span, div {{
        color: {text_color} !important;
        transition: color 0.3s ease-in-out;
    }}
    div[data-baseweb="select"] > div {{
        background-color: {select_bg};
        color: {select_text};
        border: 1.5px solid {border_color};
        border-radius: 4px;
        padding: 10px 15px;
        font-weight: 100;
        margin-top: 5px;
        margin-right: 10px;
        width: 200px;
        height: 40px;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
    }}
    div[data-baseweb="select"] span {{
        font-size: 14px !important;
        color: inherit !important;
    }}
    div[data-baseweb="select"] div[role="button"] {{
        font-size: 14px !important;
        color: inherit !important;
    }}
    div[data-baseweb="select"] > div:hover {{
        background-color: {hover_bg};
        box-shadow: 0px 0px 6px rgba(0,0,0,0.1);
    }}
    div[data-baseweb="popover"] {{
        background-color: {select_bg} !important;
        color: {select_text} !important;
        border: 1.5px solid {border_color};
        border-radius: 10px;
        overflow: visible;
    }}
    li[role="option"] {{
        background-color: {select_bg};
        color: {select_text};
        padding: 15px;
        font-weight: 250;
        font-size: 14px;
    }}
    li[role="option"]:hover {{
        background-color: {hover_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load and prepare data/model
@st.cache_data
def load_data():
    if os.path.exists('diabetes.csv'):
        df = pd.read_csv('diabetes.csv')
        X = df.drop('Outcome', axis=1)
        y = df['Outcome']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        accuracy = accuracy_score(y_test, model.predict(X_test))
        return df, X, y, model, accuracy
    else:
        st.error("Dataset 'diabetes.csv' not found. Please download it from Kaggle.")
        return None, None, None, None, None

df, X, y, model, accuracy = load_data()

# Tabs dictionary
def home_app():
    st.title("🏥 Welcome to Diabetes Healthcare Program")
    st.write("Manage your diabetes with personalized tools, predictions, and education.")
    if df is not None:
        st.write(f"Dataset loaded with {len(df)} records. Model accuracy: {accuracy:.2f}")
    st.subheader("Quick Tips")
    st.write("- Monitor blood sugar regularly.")
    st.write("- Eat balanced meals and exercise.")
    st.write("- Consult a doctor for personalized advice.")

def talk2doc_app():
    st.title("💬 Ask Queries")
    st.write("Ask health-related questions about diabetes.")
    user_query = st.text_input("Your Question:")
    if user_query:
        # Simple response logic (expand with AI like OpenAI if needed)
        if "sugar" in user_query.lower():
            st.write("**Response:** Maintain blood sugar between 70-140 mg/dL. Check with a glucometer.")
        elif "diet" in user_query.lower():
            st.write("**Response:** Focus on low-carb foods like vegetables, lean proteins, and whole grains.")
        else:
            st.write("**Response:** Please consult a healthcare professional for detailed advice.")

def diagnosis_app(df, X, y, model):
    st.title("🔍 Diagnosis")
    st.write("Enter your details for diabetes risk prediction.")
    if model is None:
        st.error("Model not loaded.")
        return
    pregnancies = st.number_input("Pregnancies", 0, 20, 0)
    glucose = st.number_input("Glucose Level", 0, 200, 100)
    blood_pressure = st.number_input("Blood Pressure", 0, 150, 70)
    skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
    insulin = st.number_input("Insulin", 0, 900, 80)
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
    age = st.number_input("Age", 0, 120, 30)
    if st.button("Predict"):
        input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
        prediction = model.predict(input_data)[0]
        st.session_state['prediction'] = "High Risk (Diabetes Detected)" if prediction == 1 else "Low Risk (No Diabetes)"
        st.success("Prediction complete! Check the Result tab.")

def result_app():
    st.title("📊 Result")
    if 'prediction' in st.session_state:
        st.write(f"**Prediction:** {st.session_state['prediction']}")
        if "High Risk" in st.session_state['prediction']:
            st.warning("Consult a doctor immediately. Monitor symptoms and lifestyle.")
        else:
            st.success("Great! Maintain healthy habits. Regular check-ups recommended.")
    else:
        st.write("No prediction available. Please complete Diagnosis first.")

def kc_app():
    st.title("📚 Knowledge Center")
    st.subheader("Diabetes Management Tips")
    st.write("### What is Diabetes?")
    st.write("Diabetes is a condition where blood sugar levels are too high due to insulin issues.")
    st.write("### Types:")
    st.write("- Type 1: Autoimmune, requires insulin.")
    st.write("- Type 2: Lifestyle-related, manageable with diet/exercise.")
    st.write("### Prevention:")
    st.write("- Healthy diet, exercise, weight management.")
    st.write("- Regular screenings.")
    st.expander("More Resources").write("Visit WHO or ADA websites for in-depth guides.")

# Sidebar navigation
st.sidebar.title('Navigation')
Tabs = {
    "Home": home_app,
    "Ask Queries": talk2doc_app,
    "Diagnosis": diagnosis_app,
    "Result": result_app,
    "Knowledge Center": kc_app
}
page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info('Made with 💙 by Sudip & Raz')

# Route to selected tab
if page == "Diagnosis":
    Tabs[page](df, X, y, model)
else:
    Tabs[page]()
