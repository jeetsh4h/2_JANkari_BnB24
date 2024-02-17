import numpy as np
from PIL import Image
import streamlit as st
from keras.api._v2.keras.models import load_model
from plant_care_tips import plant_care_tips, class_code_to_label, label_to_name

@st.cache_resource(ttl=3600)
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
    label = class_code_to_label[class_pred]

    prediction_write_up = ""
    prediction_write_up += f"{label_to_name[label]} predicted with a confidence of {np.max(confidences) * 100:.2f}%  \n"
    prediction_write_up += f"Here are some care tips for your plant:  \n"
    prediction_write_up += plant_care_tips[label]

    return prediction_write_up


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
    st.write("PaudhaYodha is a web app that helps you identify and treat your plants. It uses machine learning to identify the plant and provide you with the best care tips. Just upload a picture of your plant and let PaudhaYodha do the rest!")
    st.write("Upload a picture of your plant and let PaudhaYodha identify it for you. Once the plant is identified, PaudhaYodha will provide you with the best care tips for your plant.")

    model = load_plant_disease_model()

    # setting up image input
    option = st.selectbox("Select an option:", ("Take a photo", "Upload an image"))

    if option == "Take a photo":
        # Use webcam to capture image
        image = st.camera_input("Capture image")
        if image is not None:
            image = process_file(image)
            prediction_write_up = process_image(model, image)
            st.write(prediction_write_up)

    elif option == "Upload an image":
        # Allow user to upload image
        uploaded_file = st.file_uploader("Choose an image:", type=["jpg", "png", "jpeg", "heic", "webp"])
        if uploaded_file is not None:
            image = process_file(uploaded_file)
            st.image(image)
            prediction_write_up = process_image(model, image)
            st.write(prediction_write_up)


if __name__ == "__main__":
    main()