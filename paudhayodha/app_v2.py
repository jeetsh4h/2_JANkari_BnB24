import numpy as np
from PIL import Image
import streamlit as st
from keras.models import load_model
from plant_care_tips import plant_care_tips

def process_file(uploaded_file):
    image = Image.open(uploaded_file)
    image = image.resize((256, 256))
    image = np.array(image)
    
    return image


# streamlit web app things,,, prettify
st.set_page_config(
    page_title="PaudhaYodha", 
    page_icon=":potted_plant:", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# header
st.title('PodhaYodha :potted_plant:')
st.subheader('Hello, Learn the best way to treat your favourite plants! :wave:')
st.write("PodhaYodha is a web app that helps you identify and treat your plants. It uses machine learning to identify the plant and provide you with the best care tips. Just upload a picture of your plant and let PodhaYodha do the rest!")
st.write("Upload a picture of your plant and let PodhaYodha identify it for you. Once the plant is identified, PodhaYodha will provide you with the best care tips for your plant. It will also provide you with the best plant shops near you.")

# loading model
st.write("Loading model...")
model = load_model("./assets/resent_plant_village_final.h5")
st.write("Model loaded successfully")

# setting up image input
option = st.selectbox("Select an option:", ("Take a photo", "Upload an image"))

if option == "Take a photo":
    # Use webcam to capture image
    image = st.camera_input("Capture image")
    if image is not None:
        image = process_file(image)
        predictions = model.predict(image[np.newaxis, ...])
        st.write(f"Class {np.argmax(predictions)} predicted with confidence {np.max(predictions) * 100:.2f}%")

elif option == "Upload an image":
    # Allow user to upload image
    uploaded_file = st.file_uploader("Choose an image:", type=["jpg", "png", "jpeg", "heic"])
    if uploaded_file is not None:
        image = process_file(uploaded_file)
        predictions = model.predict(image[np.newaxis, ...])
        st.write(f"Class {np.argmax(predictions)} predicted with confidence {np.max(predictions) * 100:.2f}%")
