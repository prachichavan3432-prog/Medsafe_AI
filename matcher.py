from rapidfuzz import process, fuzz

# Your database from Activity 2.1
MEDICINE_DATA = {
    "Paracetamol": "Low",
    "Ibuprofen": "Moderate",
    "Aspirin": "High",
    "Amoxicillin": "Moderate",
    "Metformin": "Low"
}


def identify_medicine(user_input, age=25):  # Added age here
    medicine_list = list(MEDICINE_DATA.keys())
    result = process.extractOne(user_input, medicine_list, scorer=fuzz.WRatio)#type:ignore

    if result and result[1] > 70:
        name = str(result[0])
        risk = MEDICINE_DATA[name]

        # --- NEW WARNING LOGIC FOR ACTIVITY 4.2 ---
        warning = "Standard usage recommended."
        if age < 12 and risk == "High":
            warning = "🚨 CRITICAL: High risk for children under 12. Consult a doctor."
        elif risk == "High":
            warning = "⚠️ Warning: Potential strong side effects. Use as prescribed."
        # ------------------------------------------

        return {
            "name": name,
            "score": int(result[1]),
            "risk": risk,
            "warning": warning,  # The new field
            "found": True
        }
    return {"found": False}


def extract_medicines_from_text():
    return None