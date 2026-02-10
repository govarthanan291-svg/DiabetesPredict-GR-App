import streamlit as st
import pandas as pd
import pickle

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Diabetes Progression Predictor",
    page_icon="🩺",
    layout="centered"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

body {
    background: linear-gradient(120deg, #1CB5E0, #000851);
}

.main {
    background-color: #f4f9ff;
    padding: 25px;
    border-radius: 15px;
}

h1 {
    text-align: center;
    color: #0b3c5d;
}

h2 {
    color: #1f7a8c;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}

.predict-btn button {
    background: linear-gradient(90deg,#ff512f,#dd2476);
    color: white;
    font-size: 20px;
    border-radius: 10px;
    width: 100%;
    height: 60px;
}

.result {
    background: linear-gradient(90deg,#00b09b,#96c93d);
    padding: 20px;
    border-radius: 10px;
    font-size: 22px;
    color: white;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_model():
    with open("diabetes_model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# ------------------ TITLE ------------------
st.markdown("<h1>🩺 Diabetes Progression Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:gray;'>Enter Patient Medical Details</h3>", unsafe_allow_html=True)

# ------------------ INPUT CARD ------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

age = st.number_input("👤 Age", 1, 100, 25)
sex = st.selectbox("⚧ Gender", ["Female", "Male"])
bmi = st.number_input("⚖️ Body Mass Index (BMI)", 10.0, 50.0, 22.0)
bp = st.number_input("💓 Blood Pressure", 50.0, 200.0, 80.0)

tc = st.number_input("🧪 Total Cholesterol", 50.0, 400.0, 180.0)
ldl = st.number_input("🩸 LDL Cholesterol (Bad)", 50.0, 300.0, 100.0)
hdl = st.number_input("🧬 HDL Cholesterol (Good)", 10.0, 150.0, 50.0)
ratio = st.number_input("📊 Cholesterol Ratio", 1.0, 10.0, 4.0)
trig = st.number_input("🥩 Triglycerides", 50.0, 500.0, 150.0)
sugar = st.number_input("🍬 Blood Sugar Level", 60.0, 400.0, 120.0)

st.markdown("</div>", unsafe_allow_html=True)

# ------------------ ENCODING ------------------
sex_value = 1 if sex == "Male" else 0

features = pd.DataFrame({
    "age": [age],
    "sex": [sex_value],
    "bmi": [bmi],
    "bp": [bp],
    "s1": [tc],
    "s2": [ldl],
    "s3": [hdl],
    "s4": [ratio],
    "s5": [trig],
    "s6": [sugar]
})

# ------------------ PREDICT BUTTON ------------------
st.markdown("<div class='predict-btn'>", unsafe_allow_html=True)
predict = st.button("🔮 Predict Diabetes Progression")
st.markdown("</div>", unsafe_allow_html=True)

# ------------------ OUTPUT ------------------
if predict:
    prediction = model.predict(features)[0]
    st.markdown(
        f"<div class='result'>📈 Predicted Diabetes Progression Score: <b>{prediction:.2f}</b></div>",
        unsafe_allow_html=True
    )

# ------------------ FOOTER ------------------
st.markdown("<p style='text-align:center;color:gray;'>Developed with ❤️ using Machine Learning & Streamlit</p>", unsafe_allow_html=True)
