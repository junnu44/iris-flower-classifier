import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and encoder
model = joblib.load("iris_model.pkl")
le = joblib.load("label_encoder.pkl")

st.title("🌸 Iris Flower Species Predictor")

st.write("Enter the Sepal and Petal measurements:")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    species = le.inverse_transform(prediction)
    st.success(f"The predicted Iris species is: **{species[0]}**")
