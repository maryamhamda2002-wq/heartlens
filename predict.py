# utils/predict.py

def lifestyle_risk(age, systolic_bp, cholesterol, active):
    """
    Calculates lifestyle risk based on simple rules.
    """
    risk = "Low"
    if age > 50 or systolic_bp > 140 or cholesterol != "Normal" or not active:
        risk = "Medium"
    if age > 65 or systolic_bp > 160 or cholesterol == "Well Above Normal" or not active:
        risk = "High"
    return risk


def clinical_risk(chest_pain, max_hr):
    """
    Calculates clinical risk based on chest pain type and max heart rate.
    """
    risk = "Low"
    if chest_pain in ["Typical Angina", "Atypical Angina"] or max_hr < 120:
        risk = "Medium"
    if chest_pain == "Typical Angina" and max_hr < 100:
        risk = "High"
    return risk


def ecg_risk(age, systolic_bp):
    """
    ECG risk based on age and systolic blood pressure.
    """
    risk = "Low"
    if age > 55 or systolic_bp > 150:
        risk = "Medium"
    if age > 65 or systolic_bp > 160:
        risk = "High"
    return risk
