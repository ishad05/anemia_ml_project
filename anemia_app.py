import streamlit as st
import pandas as pd
import joblib

# Load model
clf = joblib.load("anemia_model.pkl")

st.set_page_config(page_title="Anemia Subtype Classifier", layout="centered")

st.title("Anemia Subtype Prediction System")
st.write("Enter CBC report values to predict anemia type")

st.divider()

# Input fields
RBC = st.number_input("RBC (million cells/µL)", 2.0, 10.0, 4.5)
PCV = st.number_input("PCV / Hematocrit (%)", 20.0, 60.0, 40.0)
MCV = st.number_input("MCV (fL)", 50.0, 110.0, 85.0)
MCH = st.number_input("MCH (pg)", 15.0, 40.0, 28.0)
MCHC = st.number_input("MCHC (g/dL)", 25.0, 38.0, 33.0)
RDW = st.number_input("RDW (%)", 10.0, 25.0, 13.5)
TLC = st.number_input("TLC (cells/mm³)", 2000, 15000, 7000)
PLT = st.number_input("Platelets (cells/mm³)", 50000, 600000, 250000)
HGB = st.number_input("Hemoglobin (g/dL)", 5.0, 18.0, 12.0)

# Mentzer Index
mentzer_index = MCV / RBC
st.info(f"Mentzer Index = {mentzer_index:.2f}")

# Create input dataframe in EXACT training order
input_df = pd.DataFrame([[
    RBC, PCV, MCV, MCH, MCHC, RDW, TLC, PLT, HGB, mentzer_index
]], columns=[
    "RBC","PCV","MCV","MCH","MCHC","RDW","TLC","PLT /mm3","HGB","mentzer_index"
])

# Prediction
if st.button("Predict Anemia Type"):
    prediction = clf.predict(input_df)[0]
    probabilities = clf.predict_proba(input_df)[0]

    classes = {
        0: "Normal",
        1: "Iron Deficiency Anemia",
        2: "Thalassemia"
    }

    st.subheader("Prediction Result")
    st.success(f"Predicted Class: **{classes[prediction]}**")

    st.subheader("Prediction Probabilities")
    prob_df = pd.DataFrame({
        "Condition": classes.values(),
        "Probability": probabilities
    })

    st.dataframe(prob_df)