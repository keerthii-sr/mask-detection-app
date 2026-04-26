import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Dummy model (since TensorFlow is not deployed)
def predict(image):
    # Fake logic for now (replace later with real model)
    return np.random.choice([0, 1])  # 0 = mask, 1 = no mask


st.title("😷 Face Mask Detection App")

st.write("Upload an image to check if the person is wearing a mask")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

def preprocess(img):
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = np.array(image)
    processed_img = preprocess(img)

    prediction = predict(processed_img)

    # ✅ Correct logic
    if prediction == 1:
        st.error("❌ Without Mask Detected")
    else:
        st.success("✅ With Mask Detected")
