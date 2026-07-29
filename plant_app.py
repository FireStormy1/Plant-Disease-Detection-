
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

IMG_SIZE = 128
CLASS_NAMES = ["Apple_Black_Rot", "Apple_Cedar_Rust", "Apple_Healthy",
               "Apple_Scab", "Corn_Common_Rust"]

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("plant_cnn.keras")

model = load_model()

st.title("Plant Disease Detector")
st.write("Upload a photo of a leaf and the model will predict its condition.")

uploaded = st.file_uploader("Choose a leaf image", type=["jpg", "jpeg", "png"])
if uploaded is not None:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Your image", width=300)

    arr = np.array(img.resize((IMG_SIZE, IMG_SIZE)), dtype="float32")[None, ...]
    probs = model.predict(arr, verbose=0)[0]
    pred = CLASS_NAMES[int(np.argmax(probs))]

    st.subheader("Prediction: " + pred.replace("_", " "))
    st.write("Confidence: {:.1f}%".format(probs.max() * 100))
    st.write("All class probabilities:")
    for c, p in sorted(zip(CLASS_NAMES, probs), key=lambda x: -x[1]):
        st.write("{}: {:.1f}%".format(c.replace("_", " "), p * 100))
        st.progress(float(p))
