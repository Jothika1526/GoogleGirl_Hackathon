from fpdf import FPDF
import random

# Predefined list of medications
# Example medications to test that should yield specific reactions
medications = [
    'adalimumab',
    'secukinumab',
    'ranitidine',
    'hydrochloride',
    'hydrochloride,',
]



# Function to generate a prescription
def generate_prescription(num_meds):
    # Randomly select medications
    selected_meds = random.sample(medications, k=num_meds)
    # Join them in the required format
    prescription = ", ".join(selected_meds)
    return prescription

# Function to create a PDF report
def create_pdf(prescription, filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Prescription Report", ln=True, align="C")
    
    # Prescription Content
    pdf.set_font("Arial", size=12)
    pdf.ln(10)  # New line
    pdf.cell(0, 10, "Medications:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, prescription, ln=True)
    
    # Save the PDF
    pdf.output(filename)
    print(f"Prescription report saved as '{filename}'.")

# Specify the number of medications you want in the prescription
num_meds = 5  # Change this to generate more or fewer medications

# Generate the prescription
prescription = generate_prescription(num_meds)

# Create the PDF report
create_pdf(prescription, "prescription_report.pdf")
