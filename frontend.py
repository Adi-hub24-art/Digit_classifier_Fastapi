import streamlit as st
import io
import os 
import requests
from PIL import Image


API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title = "DIGIT CLASSIFIER", layout="centered")

st.title("Digit Classifier (8 * 8)")
st.write("Upload a **8 * 8 grayscale PNG** or use a sample image")


# lets upload an img
uploaded_file = st.file_uploader("upload PNG image", type=["png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="uploaded Image", width=150)

    if st.button("Predict"):
        files = {"file": (uploaded_file.name,
                          uploaded_file.getvalue(),
                          uploaded_file.type,
                          )
                }

        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Predicted Digit : {prediction}")
        else:
            st.error("Prediction Failed")