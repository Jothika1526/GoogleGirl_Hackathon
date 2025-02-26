# 🌟 MediCare AI – AI-Powered Healthcare Assistance  

MediCare AI is an intelligent healthcare assistant designed to enhance **medical diagnosis, report generation, and medication safety** using AI-powered solutions. It integrates **deep learning, NLP, and machine learning** to assist doctors and patients in making better medical decisions.  

## 📌 Key Features  
👉 AI-based **Medical Image Diagnosis** (Chest X-rays & Brain MRI)  
👉 **Automated Medical Report Generation** (Using Generative AI)  
👉 **Predict Side Effects of Medications** (ML-based Analysis)  

---

## 🩺 Problem Statement  
Healthcare data is often **fragmented**, making medical diagnosis and prescription management inefficient.  
Patients visit multiple doctors, leading to:  
- Redundant prescriptions & conflicting diagnoses  
- Difficulty in managing medical records  
- Lack of awareness about medication side effects  

**MediCare AI** provides an AI-powered **end-to-end healthcare assistant** to solve these challenges.  

---

## ⚙️ Solution Approach  

### 🏥 1. Medical Image Diagnosis  
💡 AI-powered analysis of **Chest X-rays & Brain MRI scans** using:  
- **DenseNet** (Chest X-ray Classification)  
- **UNet** (Brain Tumor Segmentation)  
- Instant AI-based medical imaging insights  

### 📄 2. Unified Medical Report Generation  
🧠 Uses **LangChain & Gemini AI** to generate structured medical reports  
📝 Summarizes multiple prescriptions into **one cohesive document**  

### 💊 3. Prescription Side Effects Prediction  
🏨 ML-based model predicts **potential side effects of medications**  
🔬 Helps in **safe prescription handling & risk assessment**  

---

## 🧠 AI Models & Technologies Used  

| **Module**                    | **AI Model / Approach**                  | **Libraries Used**               |
| ----------------------------- | ---------------------------------------- | -------------------------------- |
| **Medical Image Diagnosis**   | DenseNet (Chest X-ray), UNet (Brain MRI) | TensorFlow, Keras, OpenCV        |
| **Unified Medical Report**    | LangChain + Gemini API (GenAI)           | Langchain, Gemini AI, Streamlit  |
| **Prescription Side Effects** | Machine Learning Model                   | TensorFlow, pandas, scikit-learn |

---

## 🚀 Setup Instructions  

### 📌 Step 1: Clone the Repository  
```bash
git clone https://github.com/Jothika1526/GoogleGirl_Hackathon.git
cd GoogleGirl_Hackathon
```

### 📌 Step 2: Install Dependencies  
```bash
pip install -r requirements.txt
```

### 📌 Step 3: Setup Individual Modules  

#### 🔍 Medical Image Diagnosis  
Move to the **Medical Images Diagnosis** folder:  
```bash
cd "Medical Images Diagnosis"
```
Create & activate virtual environments for each model:  

##### 🌍 Chest X-ray Diagnosis (DenseNet)
```bash
python -m venv chest_env
chest_env\Scripts\activate  # Windows
source chest_env/bin/activate  # Mac/Linux
pip install tensorflow==2.4.1 keras==3.5
```

##### 🌍 Brain Tumor Diagnosis (UNet)
```bash
python -m venv brain_env
brain_env\Scripts\activate  # Windows
source brain_env/bin/activate  # Mac/Linux
pip install tensorflow==2.17.1
```
Run the **Streamlit app** for medical image analysis:  
```bash
streamlit run app.py
```
The application will open on **localhost**, where users can upload images & fetch results.  

---

#### 🔬 Unified Medical Report  
Move to the **Unified Medical Report** folder:  
```bash
cd "Unified Medical Report"
```
Install dependencies:  
```bash
pip install -r requirements.txt
```
Modify **line 35** in `final_app.py` and add your **Gemini API Key**.  
Run the **Streamlit app**:  
```bash
streamlit run final_app.py
```

---

#### 💊 Prescription Side Effects Prediction  
Move to the **Prescription Side Effects** folder:  
```bash
cd "Prescription Side Effects"
```
Run the **med-app** model:  
```bash
python med-app.py
```
This module will predict potential side effects of medications.  

---

## 🎡 AI Models Saved As:  
- `Medical Images Diagnosis\chest_xray_model.h5`  
- `Medical Images Diagnosis\brain_tumor_model.h5`  
- `Prescription Side Effects\model.h5`  

---

## 🚀 Future Scope  
💡 **Expansion to Other Medical Images** – Integrating AI models for CT Scans, Ultrasounds, and Pathology Slides.  
🔍 **Enhanced NLP for Reports** – Improving GenAI-based report summarization.  
🏨 **Personalized Healthcare Recommendations** – AI-driven patient-specific health suggestions.  
🛠 **Integration with IoT & Wearables** – Real-time health monitoring using IoT devices.  
🌐 **Deployment on Cloud** – Scalable AI healthcare solutions for hospitals.  

---

## ⭐ Acknowledgments  
Special thanks to **GoogleGirl Hackathon** for providing the opportunity to develop this project! 🎉  

