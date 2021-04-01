import streamlit as st

def app():

    st.title('Facial Recognition')
    st.title('This app is still under construction :/')
    arch = st.radio("Choose a m",
                    ('V')
                    )

    st.write("Upload an image below.")

    file_up = st.file_uploader("Make sure it's a jpg!", type="jpg")
