import streamlit as st
import pytesseract
from PIL import Image

# Add this decorator to 'remember' results and speed up the app
@st.cache_data
def extract_text_from_image(image_file):
    try:
        img = Image.open(image_file)
        # Ensure your tesseract_cmd is still set here if needed
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {str(e)}"