import streamlit as st

def app():
    st.title("Computer Vision Portfolio")
    st.write("This app was built using PyTorch, TensorFlow Keras and StreamLit, to allow a user to perform the following computer vision tasks without coding:")
    st.write("""● Image Classification                ● Object Detection
            ● Semantic Segmentation               ● Facial Recognition
            ● GANs                                ● Neural Style Transfer
            ● Image Colourisation                 ● Pose Estimation""")

    st.write("Navigate to your task using the drop-down menu above. Note that some of the pages are under construction!")

    st.header("Designed, built and deployed by")
    st.header("Sarthak Rastogi | thesarthakrastogi@gmail.com")
    st.write("I'm good at data science, machine learning and deep learning too! See my complete portfolio at [sarthakrastogi.github.io](http://sarthakrastogi.github.io).")
