import streamlit as st
import tensorflow as tf
import numpy as np
import pytesseract
from PIL import Image
import pdfplumber

# Load your trained model
model = tf.keras.models.load_model('model.h5')

# Preprocessing function (adjust this based on your model's requirements)
def preprocess(text):
    # Here you should tokenize and pad the text as needed for the model
    # This is an example placeholder preprocessing step
    processed_text = text.lower()  # Simple preprocessing example
    # Return a numpy array or tensor, ready for model input
    return np.array([processed_text])

# Function to extract text from a PDF file (if applicable)
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to extract text from an image using OCR (for image-based prescriptions)
def extract_text_from_image(image_file):
    img = Image.open(image_file)
    text = pytesseract.image_to_string(img)
    return text

# Function to process the uploaded file (PDF, Image, or Text)
def process_file(uploaded_file, file_type):
    if file_type == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_type in ['png', 'jpg', 'jpeg']:
        return extract_text_from_image(uploaded_file)
    else:
        return str(uploaded_file.read(), 'utf-8')

# Function to process model predictions
def process_predictions(predictions):
    # Convert model output to a human-readable format (depends on your model)
    # Assuming the output is a list of side effects
    return predictions

# Streamlit UI
st.title("SyncMyCare - Drug Side Effect Predictor")

# Option for user to upload file or manually type prescription
option = st.selectbox("Choose how to provide the prescription:", ("Upload File", "Type Prescription"))

if option == "Upload File":
    uploaded_file = st.file_uploader("Upload your prescription (PDF, Image, or Text)", type=["pdf", "png", "jpg", "jpeg", "txt"])

    if uploaded_file is not None:
        # Determine file type and extract text
        file_type = uploaded_file.name.split('.')[-1]
        prescription_text = process_file(uploaded_file, file_type)

        st.subheader("Extracted Prescription Text:")
        st.write(prescription_text)
        
        # Preprocess the extracted text for the model
        input_data = preprocess(prescription_text)
        
        # Predict side effects
        predictions = model.predict(input_data)
        
        # Process and display the predictions
        side_effects = process_predictions(predictions)
        st.subheader("Predicted Side Effects:")
        st.write(side_effects)

elif option == "Type Prescription":
    # Manually input prescription text
    prescription_text = st.text_area("Enter your prescription:")

    if st.button("Get Side Effects"):
        if prescription_text:
            # Preprocess the manual input for the model
            input_data = preprocess(prescription_text)
            
            # Predict side effects
            predictions = model.predict(input_data)
            
            # Process and display the predictions
            side_effects = process_predictions(predictions)
            st.subheader("Predicted Side Effects:")
            st.write(side_effects)
        else:
            st.warning("Please enter the prescription text.")