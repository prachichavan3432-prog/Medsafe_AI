import streamlit as st
from PIL import Image
from utils.matcher import identify_medicine, extract_medicines_from_text
from src.ocr_processor import extract_text_from_image

# 1. Page Setup
st.set_page_config(page_title="MedSafe AI Dashboard", layout="wide")
st.title("🛡️ MedSafe AI - Safety Assistant")

# 2. Activity 3.1: Create the Multi-Tab Layout
tab1, tab2, tab3 = st.tabs(["📸 Prescription Scan", "🔍 Safety Checker", "👤 Patient Profile"])

with tab1:
    st.header("Prescription OCR Scanner")
    uploaded_file = st.file_uploader("Upload prescription photo", type=['jpg', 'jpeg', 'png'])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Prescription', width=500)

        with st.spinner('AI is reading the text...'):  # type: ignore
            raw_text = extract_text_from_image(uploaded_file)

        # Activity 2.3 logic
        detected_meds = extract_medicines_from_text()

        if detected_meds:
            st.subheader("💊 Detected Medicines")
            for med in detected_meds:
                st.success(f"Verified: {med['name']} ({med['score']}% match)")
        else:
            st.warning("No medicines recognized from the image.")

with tab2:
    st.header("🔍 Manual Safety Check")
    query = st.text_input("Type a medicine name to check risk:")

    if query:
        result = identify_medicine(query)
        if result["found"]:
            # Activity 3.3: Structured Metrics
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Medicine", result['name'])
            with col_b:
                st.metric("Risk Level", result['risk'])

            st.info(f"💡 AI Note: Testing safety for {result['name']}.")
        else:
            st.error("Medicine not found.")

with tab3:
    st.header("👤 Patient Profile")
    # Activity 3.2: Robust demographic inputs
    age = st.number_input("Patient Age", min_value=0, max_value=120, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    st.success(f"Profile Active: {age} year old {gender}")