import streamlit as st
from predict import lifestyle_risk, clinical_risk, ecg_risk
from pathlib import Path

# ---------- Load CSS ----------
def load_css():
    css_path = Path("style.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# ---------- Page ----------
st.markdown("<div class='title'>❤️ HeartLens</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Multi-Source Cardiovascular Risk Tool</div>", unsafe_allow_html=True)

# ---------- Inputs ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)

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

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Risk Summary")
    st.markdown(f"🟦 Lifestyle Risk: <span class='risk'>{l_r}</span>", unsafe_allow_html=True)
    st.markdown(f"🟨 Clinical Risk: <span class='risk'>{c_r}</span>", unsafe_allow_html=True)
    st.markdown(f"🟥 ECG Risk: <span class='risk'>{e_r}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
