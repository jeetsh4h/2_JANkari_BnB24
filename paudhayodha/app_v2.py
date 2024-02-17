import numpy as np
from PIL import Image
import streamlit as st
from keras.models import load_model
from plant_care_tips import plant_care_tips

@st.cache_resource()
def load_plant_disease_model():
    return load_model("./assets/resent_plant_village_final.h5")


def process_file(uploaded_file):
    image = Image.open(uploaded_file)
    image = image.resize((256, 256))
    return np.array(image)

def process_image(model, image):
    """
    returns a string that needs to be written using the streamlit write function
    """
    confidences = model.predict(image[np.newaxis, ...])
    class_pred =  np.argmax(confidences)
    
    # TODO: get the plant name and disease from the class_pred
    # make sure to use the confidence value and a threshold to 
    # decide if the prediction is correct and what to write out

    NotImplemented
    return ""


# streamlit web app things,,, prettify
def main():
    st.set_page_config(
        page_title="PaudhaYodha", 
        page_icon=":potted_plant:", 
        layout="wide", 
        initial_sidebar_state="expanded"
    )

    st.title('PaudhaYodha :potted_plant:')
    st.subheader('Hello, Learn the best way to treat your favourite plants! :wave:')
    st.write("PaudhaYodha is a web app that helps you identify and treat your plants. It uses machine learning to identify the plant and provide you with the best care tips. Just upload a picture of your plant and let PodhaYodha do the rest!")
    st.write("Upload a picture of your plant and let PaudhaYodha identify it for you. Once the plant is identified, PaudhaYodha will provide you with the best care tips for your plant.")

    model = load_plant_disease_model()

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


if __name__ == "__main__":
    main()
