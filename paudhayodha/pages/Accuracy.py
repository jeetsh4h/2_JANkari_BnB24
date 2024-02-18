import streamlit as st
apple_scab = './assets/apple_scab.jpeg'
cherry_disease = './assets/Cherry_disease.jpeg'
potato_healthy = './assets/potato_healthy.jpeg'
unclear_tomato = './assets/unclear_tomato.jpeg'
blurry  = './assets/blurrry.jpeg'
full_plant = './assets/full_plant.jpeg'
st.header('How to achieve accurate results')
st.sidebar.write('The accuracy of the model depends highly on the quality of the photo. Here are some tips to get the best results')
with st.container():
    st.markdown(
                 '''
                    ### Dos:

                '''

                )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(apple_scab, width=200)
        st.write('Take clear photos and close up shots of the affected area')
    with col2:
        st.image(cherry_disease, width=200)
        st.write('Take photos in natural light')
    with col3:
        st.image(potato_healthy, width=200)
        st.write('Clear photos of leaves will outperform photos of entire plants')


with st.container():
    st.markdown(
                 '''
                    ### Donts:

                '''

                )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(unclear_tomato, width=200)
        st.write('Leaves are not visible')
    with col2:
        st.image(blurry, width=200)
        st.write('Avoid blurry photos')
    with col3:
        st.image(full_plant, width=200)
        st.write('Avoid zoomed out photos of entire plants')


# table_data = [st.image('./assets/apple_scab.jpeg',width=100), st.image('./assets/apple_scab.jpeg',width=100), st.image('./assets/apple_scab.jpeg',width=100)]
# st.table(table_data)

