import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)

from multiapp import MultiApp
from apps import home, image_classification, object_detection, semantic_segmentation, facial_recognition, gans, neural_style_transfer, image_colourisation, pose_estimation # import your app modules here

app = MultiApp()

app.add_app("Home", home.app)

app.add_app("Image Classification", image_classification.app)
app.add_app("Object Detection", object_detection.app)
app.add_app("Semantic Segmentation", semantic_segmentation.app)
app.add_app("Facial Recognition", facial_recognition.app)
app.add_app("GANs", gans.app)
app.add_app("Neural Style Transfer", neural_style_transfer.app)
app.add_app("Image Colourisation", image_colourisation.app)
app.add_app("Pose Estimation", pose_estimation.app)
# The main app
app.run()
