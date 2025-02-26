
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt  # Add this import

# Determine which mode to run
MODE = os.getenv("STREAMLIT_MODE", "CHEST")  # Default to BRAIN if no environment variable is provided
st.write(f"Running in {MODE} mode")

if MODE == "CHEST":
    st.title("🔍 Chest X-ray Disease Detection")
    
    @st.cache_resource
    def load_chest_xray_model():
        return tf.keras.models.load_model("chest_xray_model.h5", safe_mode=False)

    chest_xray_model = load_chest_xray_model()

    def preprocess_xray_image(image):
        img = image.resize((224, 224))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)
        return img

    CLASS_NAMES = [
        "Cardiomegaly", "Emphysema", "Effusion", "Hernia", "Infiltration",
        "Mass", "Nodule", "Atelectasis", "Pneumothorax", "Pleural_Thickening",
        "Pneumonia", "Fibrosis", "Edema", "Consolidation"
    ]

    uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded X-ray", use_column_width=True)

        processed_image = preprocess_xray_image(image)
        prediction = chest_xray_model.predict(processed_image)[0]

        predicted_index = np.argmax(prediction)
        predicted_class = CLASS_NAMES[predicted_index]
        confidence = prediction[predicted_index] * 100

        st.subheader(f"Predicted Class: **{predicted_class} ({confidence:.2f}%)**")

elif MODE == "BRAIN":
    st.title("🧠 Brain Tumor Segmentation")

    @st.cache_resource
    def load_brain_tumor_model():
        return tf.keras.models.load_model("brain_tumor_segmentation_unet.h5")

    brain_tumor_model = load_brain_tumor_model()

    def preprocess_brain_image(image):
        img = image.resize((256, 256))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        return img

    uploaded_file = st.file_uploader("Upload a Brain MRI Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded MRI", use_column_width=True)

        processed_image = preprocess_brain_image(image)
        predicted_mask = brain_tumor_model.predict(processed_image)[0]

        # Visualize original image and the predicted mask side by side
        st.subheader("Predicted Tumor Segmentation")
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))

        # Show the original image
        axes[0].imshow(processed_image[0], cmap='gray')
        axes[0].set_title("Original MRI")
        axes[0].axis('off')

        # Show the predicted mask
        axes[1].imshow(predicted_mask, cmap='jet')
        axes[1].set_title("Predicted Mask")
        axes[1].axis('off')

        # Display plot
        st.pyplot(fig)
