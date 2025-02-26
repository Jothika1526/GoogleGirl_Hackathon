import streamlit as st

# Page Configuration
st.set_page_config(page_title="MediCare AI", page_icon="🩺", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .title {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        color: transparent;
    }
    .subtitle {
        font-size: 25px;
        text-align: center;
        font-weight: 300;
        color: #bbbbbb;
    }
    .box {
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        background: rgba(255, 255, 255, 0.05);
        margin: 15px;
        box-shadow: 0px 4px 10px rgba(0, 255, 255, 0.2);
        transition: 0.3s;
    }
    .box:hover {
        background: rgba(255, 255, 255, 0.1);
        box-shadow: 0px 6px 14px rgba(0, 255, 255, 0.4);
    }
    .emoji {
        font-size: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<h1 class='title'>🌟 MediCare AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI-Powered Healthcare Assistant</p>", unsafe_allow_html=True)

st.write("---")

# Features Section
st.markdown("### 📌 **Key Features**")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='box'><span class='emoji'>🩺</span><br> Medical Imaging Analysis with AI</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='box'><span class='emoji'>📄</span><br> Unified Medical Reports</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='box'><span class='emoji'>💊</span><br> Drug Side-Effects Prediction</div>", unsafe_allow_html=True)

st.write("---")

# Call to Action
st.markdown("<h3 style='text-align:center;'>🚀 Start Your AI Healthcare Journey Today!</h3>", unsafe_allow_html=True)
