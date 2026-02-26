import streamlit as st
import pandas as pd
import joblib

# Configuración visual

st.set_page_config(page_title="Diabetes Risk Predictor", layout="centered")

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stButton>button {
    background-color: #1f77b4;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Cargar modelo

model = joblib.load("model.pkl")
threshold = joblib.load("threshold.pkl")

st.title("Diabetes Risk Prediction Tool")
st.markdown("Complete the patient information below to estimate diabetes risk.")

# Inputs organizados

st.subheader("Medical History")

HighBP = st.radio("Hypertension", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
HighChol = st.radio("High Cholesterol", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
CholCheck = st.radio("Cholesterol Check in last 5 years", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

st.subheader("Body & Lifestyle")

BMI = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
Smoker = st.radio("Smoker (100+ cigarettes lifetime)", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
PhysActivity = st.radio("Physical Activity (last 30 days)", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

st.subheader("General Health")

GenHlth = st.slider("General Health (1=Excellent, 5=Poor)", 1, 5, 3)
MentHlth = st.slider("Poor Mental Health Days (last 30)", 0, 30, 0)
PhysHlth = st.slider("Poor Physical Health Days (last 30)", 0, 30, 0)
DiffWalk = st.radio("Difficulty Walking", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

st.subheader("Demographics")

Sex = st.radio("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")

# AGE
age_options = {
    "18–24": 1,
    "25–29": 2,
    "30–34": 3,
    "35–39": 4,
    "40–44": 5,
    "45–49": 6,
    "50–54": 7,
    "55–59": 8,
    "60–64": 9,
    "65–69": 10,
    "70–74": 11,
    "75–79": 12,
    "80+": 13
}
age_label = st.selectbox("Age Range", list(age_options.keys()))
Age = age_options[age_label]

# EDUCATION
education_options = {
    "Never attended school": 1,
    "Elementary": 2,
    "Some high school": 3,
    "High school graduate": 4,
    "Some college": 5,
    "College graduate": 6
}
education_label = st.selectbox("Education Level", list(education_options.keys()))
Education = education_options[education_label]

# INCOME
income_options = {
    "< $10,000": 1,
    "$10,000–$15,000": 2,
    "$15,000–$20,000": 3,
    "$20,000–$25,000": 4,
    "$25,000–$35,000": 5,
    "$35,000–$50,000": 6,
    "$50,000–$75,000": 7,
    "$75,000+": 8
}
income_label = st.selectbox("Annual Income", list(income_options.keys()))
Income = income_options[income_label]

# Predicción

if st.button("Predict Risk"):

    input_data = pd.DataFrame([{
        "HighBP": HighBP,
        "HighChol": HighChol,
        "CholCheck": CholCheck,
        "BMI": BMI,
        "Smoker": Smoker,
        "Stroke": 0,
        "HeartDiseaseorAttack": 0,
        "PhysActivity": PhysActivity,
        "Fruits": 1,
        "Veggies": 1,
        "HvyAlcoholConsump": 0,
        "AnyHealthcare": 1,
        "NoDocbcCost": 0,
        "GenHlth": GenHlth,
        "MentHlth": MentHlth,
        "PhysHlth": PhysHlth,
        "DiffWalk": DiffWalk,
        "Sex": Sex,
        "Age": Age,
        "Education": Education,
        "Income": Income
    }])

    prob = model.predict_proba(input_data)[0][1]
    prediction = 1 if prob > threshold else 0

    st.subheader("Prediction Result")

    st.progress(prob)

    st.write(f"Estimated probability of diabetes risk: **{prob:.2%}**")

    if prediction == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")