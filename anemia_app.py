import streamlit as st
import pandas as pd
import joblib
import random


# Page config

st.set_page_config(
    page_title="Anemia Subtype Classifier",
    layout="centered"
)


# Load trained model

clf = joblib.load("anemia_model.pkl")


# Random CBC generator

def generate_random_cbc():
    return {
        "RBC": round(random.uniform(3.5, 6.5), 2),
        "PCV": round(random.uniform(28.0, 50.0), 1),
        "MCV": round(random.uniform(60.0, 95.0), 1),
        "MCH": round(random.uniform(20.0, 32.0), 1),
        "MCHC": round(random.uniform(30.0, 36.0), 1),
        "RDW": round(random.uniform(11.0, 18.0), 1),
        "TLC": random.randint(4000, 11000),
        "PLT": random.randint(150000, 450000),
        "HGB": round(random.uniform(8.0, 15.0), 1)
    }

# Initialize session state

if "cbc" not in st.session_state:
    st.session_state.cbc = generate_random_cbc()


# UI

st.title("Anemia Subtype Prediction System")
st.write(
    "This app simulates a **new CBC report** and predicts the most likely anemia subtype."
)

# Generate new patient
if st.button("🔄 Generate New Random Patient"):
    st.session_state.cbc = generate_random_cbc()
    st.rerun()   # ✅ FIXED (was st.experimental_rerun())

st.divider()

cbc = st.session_state.cbc


# Input fields (state-safe)

RBC = st.number_input("RBC (million cells/µL)", 2.0, 10.0, cbc["RBC"])
PCV = st.number_input("PCV / Hematocrit (%)", 20.0, 60.0, cbc["PCV"])
MCV = st.number_input("MCV (fL)", 50.0, 110.0, cbc["MCV"])
MCH = st.number_input("MCH (pg)", 15.0, 40.0, cbc["MCH"])
MCHC = st.number_input("MCHC (g/dL)", 25.0, 38.0, cbc["MCHC"])
RDW = st.number_input("RDW (%)", 10.0, 25.0, cbc["RDW"])
TLC = st.number_input("TLC (cells/mm³)", 2000, 15000, cbc["TLC"])
PLT = st.number_input("Platelets (cells/mm³)", 50000, 600000, cbc["PLT"])
HGB = st.number_input("Hemoglobin (g/dL)", 5.0, 18.0, cbc["HGB"])


# Derived feature

mentzer_index = MCV / RBC
st.info(f"Mentzer Index: **{mentzer_index:.2f}**")


# Create input dataframe (EXACT training order)

input_df = pd.DataFrame([[
    RBC, PCV, MCV, MCH, MCHC,
    RDW, TLC, PLT, HGB, mentzer_index
]], columns=[
    "RBC", "PCV", "MCV", "MCH", "MCHC",
    "RDW", "TLC", "PLT /mm3", "HGB", "mentzer_index"
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

    st.subheader("🔍 Prediction Result")
    st.success(f"**{classes[prediction]}**")

    st.subheader("📊 Prediction Confidence")
    prob_df = pd.DataFrame({
        "Condition": list(classes.values()),
        "Probability": probabilities
    })

    st.dataframe(prob_df, use_container_width=True)

st.caption("Educational use only. Not a medical diagnosis tool.")