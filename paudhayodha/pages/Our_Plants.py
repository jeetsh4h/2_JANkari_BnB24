import streamlit as st

# all the plants we support
plants = [
    'Apple :apple:', 
    'Blueberry :blueberries:', 
    'Cherry :cherries:', 
    'Corn :corn:', 
    'Grape :grapes:',
    'Orange :tangerine:',
    'Peach :peach:',
    'Bell Pepper :bell_pepper:',
    'Potato :potato:',
    'Raspberry',
    'Soybean',
    'Squash',
    'Strawberry :strawberry:',
    'Tomato :tomato:'
]

diseases = [
    'Apple Scab; Black Rot; Cedar Apple Rust',
    'None',
    'Powdery Mildew',
    'Cercospora; Common Rust; Northern Leaf Blight',
    'Black Rot; Esca (Black Measles); Leaf Blight',
    'Haunglongbing',
    'Bacterial Spot',
    'Bacterial Spot', 
    'Early Blight; Late Blight',
    'None',
    'None',
    'Powdery Mildew',
    'Powdery Mildew; Leaf Scorch',
    'Bacterial Spot; Early Blight; Late Blight; Leaf Mold; Septoria; Spider Mites; Target Spot; Yellow Leaf Curl Virus'
]


# page niceties
st.header('Plants Under Our Care')
st.sidebar.success('These are all the plants we currently support.')

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('List of Plants:')
        st.markdown('- ' + '\n- '.join(plants))

# issues with alignment,,, TODO: fix
    # with col2:
    #     st.subheader('Corresponding Diseases:')
    #     st.markdown('- ' + '\n- '.join(diseases))
