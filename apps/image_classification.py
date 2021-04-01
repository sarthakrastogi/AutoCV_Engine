import streamlit as st
from torchvision import models, transforms
import torch
from PIL import Image

def app():

    st.title('Image Classification')
    arch = st.radio("Choose a model architecture",
                    ('VGG16', 'ResNet', 'DenseNet', 'Inception', 'Wide ResNet')
                    )

    st.write("Upload an image below to classsify in between 1000 classes.")

    file_up = st.file_uploader("Make sure it's a jpg!", type="jpg")

    def predict(image_path):
        if arch == 'VGG16':
            model = models.vgg16(pretrained=True)
        elif arch == 'ResNet':
            model = models.resnet18(pretrained=True)
        elif arch == 'DenseNet':
            model = models.densenet161(pretrained=True)
        elif arch == 'Inception':
            model = models.inception_v3(pretrained=True)
        elif arch == 'Wide ResNet':
            model = models.wide_resnet50_2(pretrained=True)

        transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
                            mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225]
                            )])

        img = Image.open(image_path)
        batch_t = torch.unsqueeze(transform(img), 0)

        model.eval()
        out = model(batch_t)

        with open('imagenet_classes.txt') as f:
            classes = [line.strip() for line in f.readlines()]

        prob = torch.nn.functional.softmax(out, dim=1)[0] * 100
        _, indices = torch.sort(out, descending=True)
        return [(classes[idx], prob[idx].item()) for idx in indices[0][:5]]

    if file_up is not None:
        image = Image.open(file_up)
        st.image(image, caption='uploaded image', use_column_width=True)
        st.write("")
        st.write("Processing your image now.")
        st.write("Please allow a few seconds if running for the first time; the app needs to download the model weights as cache. 🤷‍♀️")
        labels = predict(file_up)

        for i in labels:
            st.write("Prediction (index, name)", i[0], ",   Score: ", i[1])
