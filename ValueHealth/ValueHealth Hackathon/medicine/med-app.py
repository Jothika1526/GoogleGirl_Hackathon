import streamlit as st
import pandas as pd
import pdfplumber

# Define drugList and reactionList
drugList = {
    'adalimumab': 1, 'secukinumab': 2, 'ranitidine': 3, 'hydrochloride': 4, 
    'hydrochloride,': 5, 'sodium': 6, 'acetate': 7, 'prednisone,': 8, 
    'certolizumab': 9, 'sulfate,': 10, 'calcium': 11, 'sodium,': 12, 
    'adalimumab,': 13, 'upadacitinib': 14, 'fingolimod': 15, 'pegol': 16, 
    'insulin': 17, 'glargine': 18, 'levonorgestrel': 19, 'human': 20, 
    'oxycodone': 21, 'palbociclib': 22, 'leuprolide': 23, 'tozinameran': 24, 
    'others': 25
}

reactionList = {
    'cough': 1, 'drug ineffective': 2, 'headache': 3, 'pyrexia': 4, 
    'nausea': 5, 'pain in extremity': 6, 'fatigue': 7, 'diarrhoea': 8, 
    'injection site pain': 9, 'dizziness': 10, 'asthenia': 11, 'rash': 12, 
    'pain': 13, 'malaise': 14, 'arthralgia': 15, 'condition aggravated': 16, 
    'pruritus': 17, 'vomiting': 18, 'dyspnoea': 19, 'illness': 20, 
    'weight decreased': 21, 'others': 22
}

# Function to extract medications from a prescription report PDF
def extract_medications_from_pdf(pdf_file):
    medications = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if "Medications:" in text:
                start_index = text.index("Medications:") + len("Medications:")
                # Split the medications based on commas
                medications = [med.strip() for med in text[start_index:].split(",")]
                break
    return medications

# Function to predict reactions based on the extracted medications
def predict_reactions(medications):
    predicted_reactions = []
    
    # Check for each medication and append the reactions
    for med in medications:
        med = med.lower()  # Convert to lowercase for consistency
        if med in drugList.keys():
            # Example reactions for each drug
            if med == 'adalimumab':
                predicted_reactions.append('nausea')
                predicted_reactions.append('headache')
            elif med == 'secukinumab':
                predicted_reactions.append('rash')
                predicted_reactions.append('fatigue')
            elif med == 'ranitidine':
                predicted_reactions.append('diarrhoea')
                predicted_reactions.append('vomiting')
            elif med == 'hydrochloride':
                predicted_reactions.append('headache')
                predicted_reactions.append('nausea')
            elif med == 'sodium':
                predicted_reactions.append('fatigue')
                predicted_reactions.append('muscle cramps')
            elif med == 'acetate':
                predicted_reactions.append('asthenia')
            elif med == 'prednisone':
                predicted_reactions.append('malaise')
                predicted_reactions.append('weight decreased')
            elif med == 'certolizumab':
                predicted_reactions.append('injection site pain')
                predicted_reactions.append('pyrexia')
            elif med == 'sulfate':
                predicted_reactions.append('cough')
            elif med == 'calcium':
                predicted_reactions.append('constipation')
            elif med == 'upadacitinib':
                predicted_reactions.append('nausea')
                predicted_reactions.append('headache')
            elif med == 'fingolimod':
                predicted_reactions.append('dizziness')
                predicted_reactions.append('dyspnoea')
            elif med == 'pegol':
                predicted_reactions.append('rash')
            elif med == 'insulin':
                predicted_reactions.append('hypoglycemia')
            elif med == 'glargine':
                predicted_reactions.append('weight gain')
            elif med == 'levonorgestrel':
                predicted_reactions.append('breast tenderness')
                predicted_reactions.append('headache')
            elif med == 'human':
                predicted_reactions.append('allergic reactions')
            elif med == 'oxycodone':
                predicted_reactions.append('dizziness')
                predicted_reactions.append('constipation')
            elif med == 'palbociclib':
                predicted_reactions.append('fatigue')
                predicted_reactions.append('headache')
            elif med == 'leuprolide':
                predicted_reactions.append('hot flashes')
                predicted_reactions.append('malaise')
            elif med == 'tozinameran':
                predicted_reactions.append('pyrexia')
                predicted_reactions.append('pain at injection site')
            # Add other drugs and their corresponding reactions as needed
        else:
            predicted_reactions.append('others')

    return list(set(predicted_reactions))  # Return unique reactions

# Streamlit app
st.title("Medication Reaction Prediction")
st.write("Upload a prescription report PDF or input medication names to predict reactions.")

# Add input options for both PDF and text
input_type = st.radio("Select input type:", ("Upload PDF", "Text Input"))

medications = []

if input_type == "Upload PDF":
    # File uploader for PDF
    pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

    if pdf_file is not None:
        # Extract medications from the uploaded PDF file
        medications = extract_medications_from_pdf(pdf_file)
        st.write("Extracted Medications:")
        st.write(medications)
else:
    # Text input for medications
    medication_text = st.text_area("Enter the medications (comma-separated):")
    if medication_text:
        medications = [med.strip() for med in medication_text.split(",")]
        st.write("Entered Medications:")
        st.write(medications)

# If medications are available, predict the reactions
if medications:
    predicted_reactions = predict_reactions(medications)

    # Display predictions in a visually appealing format
    st.write("The side effects of the prescription uploaded can be:")
    
    # Format the list using markdown for better visual appeal
    st.markdown("### Side Effects:")
    st.markdown("\n".join([f"- {reaction.capitalize()}" for reaction in predicted_reactions]))