def lifestyle_risk(age, systolic_bp, cholesterol, active):
    risk = 0
    if age > 50:
        risk += 1
    if systolic_bp > 140:
        risk += 1
    if cholesterol != "Normal":
        risk += 1
    if not active:
        risk += 1
    if risk <= 1:
        return "Low"
    elif risk == 2:
        return "Medium"
    else:
        return "High"

def clinical_risk(chest_pain, max_hr):
    if chest_pain in ["Typical Angina", "Asymptomatic"] or max_hr < 120:
        return "High"
    elif max_hr < 140:
        return "Medium"
    else:
        return "Low"

def ecg_risk(age, systolic_bp):
    if age > 50 and systolic_bp > 140:
        return "High"
    elif systolic_bp > 130:
        return "Medium"
    else:
        return "Low"
