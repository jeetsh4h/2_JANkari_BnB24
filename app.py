import streamlit as st
import numpy as np
from PIL import Image
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, ClientSettings
import cv2
import os
from plant_care_tips import plant_care_tips


def process_species(species):
    # Check if the input species exists in the dictionary
        if species in plant_care_tips:
        # Display the care tips for the input species
            st.write('Care tips for', species, ':', plant_care_tips[species])
        else:
            st.write('Species not found in the database.')
def main():
    st.set_page_config(page_title="PodhaYodha", page_icon=":potted_plant:", layout="wide", initial_sidebar_state="expanded")
    #header
    st.title('PodhaYodha :potted_plant:')
    st.subheader('Hello, Learn the best way to treat your favourite plants! :wave:')
    st.write("PodhaYodha is a web app that helps you identify and treat your plants. It uses machine learning to identify the plant and provide you with the best care tips. Just upload a picture of your plant and let PodhaYodha do the rest!")
    st.write("Upload a picture of your plant and let PodhaYodha identify it for you. Once the plant is identified, PodhaYodha will provide you with the best care tips for your plant. It will also provide you with the best plant shops near you.")

    
    picture = st.camera_input("First, take a picture...")

    if picture:
        with open ('test.jpg','wb') as file:
          file.write(picture.getbuffer())

    species = st.text_input('Enter the species name (e.g., Apple, Tomato, etc.):')

     # Button to submit the input
    if st.button('Submit'):
        # Process the input
        process_species(species)

   

if __name__ == "__main__":
    main()
    

    # img_file_buffer = None
# img_array = np.array([])
# def take_photo(img_file_buffer,img_array):
#     if st.button("Process Image"):
#         img_file_buffer = (st.camera_input("Upload a picture"))
#     if img_file_buffer is not None:
#         # To read image file buffer as a PIL Image:
#         img = Image.open(img_file_buffer)

#         # To convert PIL Image to numpy array:
#         img_array = np.array(img)

#         # Check the type of img_array:
#         # Should output: <class 'numpy.ndarray'>
#         st.write(type(img_array))

#     # Check the shape of img_array:
#     # Should output shape: (height, width, channels)
#     st.write(img_array.shape)
#     return img_array
# img = take_photo(img_file_buffer,img_array=img_array)
# img = Image.fromarray(img)
# img.save('image.jpg')
# img.show()



