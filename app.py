from predict import lifestyle_risk, clinical_risk, ecg_risk
import streamlit as st

st.title("❤️ HeartLens - Test App")

age = st.number_input("Age", 18, 100, 25)
systolic = st.number_input("Systolic BP", 80, 200, 120)
cholesterol = st.selectbox("Cholesterol", ["Normal", "Above Normal", "Well Above Normal"])
active = st.checkbox("Physically Active", True)
chest_pain = st.selectbox("Chest Pain", ["Asymptomatic","Typical Angina","Atypical Angina","Non-Anginal"])
max_hr = st.number_input("Max Heart Rate", 60, 220, 150)

if st.button("Analyze Heart Risk"):
    l_r = lifestyle_risk(age, systolic, cholesterol, active)
    c_r = clinical_risk(chest_pain, max_hr)
    e_r = ecg_risk(age, systolic)

    st.write(f"Lifestyle Risk: {l_r}")
    st.write(f"Clinical Risk: {c_r}")
    st.write(f"ECG Risk: {e_r}")
