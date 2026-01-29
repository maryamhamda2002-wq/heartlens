import streamlit as st
from pathlib import Path
from utils.predict import lifestyle_risk, clinical_risk, ecg_risk

# ---------- Load CSS ----------
def load_css():
    css_path = Path("assets/style.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# ---------- Session State ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- PAGE: HOME ----------
if st.session_state.page == "home":
    st.markdown("<div class='title'>❤️ HeartLens</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Multi-Source Cardiovascular Risk Tool</div>", unsafe_allow_html=True)

    if st.button("Start"):
        st.session_state.page = "login"

# ---------- PAGE: LOGIN ----------
elif st.session_state.page == "login":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Login / Enter Your Details")

    name = st.text_input("Full Name", value=st.session_state.get("name",""))
    age = st.number_input("Age", 18, 100, value=st.session_state.get("age",25))
    gender = st.selectbox("Gender", ["Female", "Male"], index=0 if st.session_state.get("gender","Female")=="Female" else 1)

    if st.button("Continue"):
        if name.strip() == "":
            st.warning("Please enter your name to continue")
        else:
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.gender = gender
            st.session_state.page = "input"
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- PAGE: PATIENT INPUT ----------
elif st.session_state.page == "input":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(f"Welcome {st.session_state.name}, enter patient data")

    systolic = st.number_input("Systolic BP", 80, 200, value=st.session_state.get("systolic",120))
    diastolic = st.number_input("Diastolic BP", 50, 150, value=st.session_state.get("diastolic",80))
    cholesterol = st.selectbox("Cholesterol Level", ["Normal","Above Normal","Well Above Normal"], 
                               index=["Normal","Above Normal","Well Above Normal"].index(st.session_state.get("cholesterol","Normal")))
    active = st.checkbox("Physically Active", value=st.session_state.get("active",True))
    chest_pain = st.selectbox("Chest Pain Type", ["Asymptomatic","Typical Angina","Atypical Angina","Non-Anginal"],
                              index=["Asymptomatic","Typical Angina","Atypical Angina","Non-Anginal"].index(st.session_state.get("chest_pain","Asymptomatic")))
    max_hr = st.number_input("Max Heart Rate Achieved", 60, 220, value=st.session_state.get("max_hr",150))

    if st.button("Analyze Heart Risk"):
        st.session_state.systolic = systolic
        st.session_state.diastolic = diastolic
        st.session_state.cholesterol = cholesterol
        st.session_state.active = active
        st.session_state.chest_pain = chest_pain
        st.session_state.max_hr = max_hr
        st.session_state.page = "results"

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- PAGE: RESULTS ----------
elif st.session_state.page == "results":
    l_risk = lifestyle_risk(st.session_state.age, st.session_state.systolic, st.session_state.cholesterol, st.session_state.active)
    c_risk = clinical_risk(st.session_state.chest_pain, st.session_state.max_hr)
    e_risk = ecg_risk(st.session_state.age, st.session_state.systolic)

    # Risk summary
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Risk Summary")
    st.markdown(f"🟦 Lifestyle Risk: <span class='risk-{l_risk.lower()}'>{l_risk}</span>", unsafe_allow_html=True)
    st.markdown(f"🟨 Clinical Risk: <span class='risk-{c_risk.lower()}'>{c_risk}</span>", unsafe_allow_html=True)
    st.markdown(f"🟥 ECG Risk: <span class='risk-{e_risk.lower()}'>{e_risk}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Interpretation
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Interpretation & Logic")
    st.write(f"Hello {st.session_state.name}, here is how your risk is calculated:")
    st.markdown("""
- **Lifestyle Risk:** Based on age, systolic BP, cholesterol, and physical activity  
- **Clinical Risk:** Based on chest pain type and max heart rate  
- **ECG Risk:** Population-level ECG pattern rules based on age and systolic BP  
""")
    st.write("This rule-based approach provides a beginner-friendly, hackathon-ready assessment.")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Start Over"):
        st.session_state.page = "home"

# ---------- FOOTER ----------
st.markdown("<footer>HeartLens &copy; 2026 – Hackathon Ready</footer>", unsafe_allow_html=True)
