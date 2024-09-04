import streamlit as st
import mlflow
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import pickle
# Load the dataset to get unique values for dropdowns
df_loaded = pd.read_csv("model/df_loaded.csv")  # Adjust this path to your dataset
# Create a dictionary to hold unique values for each feature
unique_values = {
    "brand": df_loaded["brand"].unique().tolist(),
    "display": df_loaded["display"].unique().tolist(),
    "operating_system": df_loaded["operating_system"].unique().tolist(),
    "processor": df_loaded["processor"].unique().tolist(),
    "ram_type": df_loaded["ram_type"].unique().tolist(),
    "rom_type": df_loaded["rom_type"].unique().tolist(),
    "ram": df_loaded["ram"].unique().tolist(),
    "rom": df_loaded["rom"].unique().tolist()
}
# Streamlit app
st.title("Laptop Price Prediction")
# Create dropdowns for each feature except ratings
brand = st.selectbox("Brand", unique_values["brand"])
display = st.selectbox("Display", unique_values["display"])
operating_system = st.selectbox("Operating System", unique_values["operating_system"])
processor = st.selectbox("Processor", unique_values["processor"])
ram_type = st.selectbox("RAM Type", unique_values["ram_type"])
rom_type = st.selectbox("ROM Type", unique_values["rom_type"])
ram = st.selectbox("RAM", unique_values["ram"])
rom = st.selectbox("ROM", unique_values["rom"])
# Manual input for ratings
ratings = st.number_input("Ratings", min_value=0.0, max_value=5.0, step=0.01)
with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)
# Predict button
if st.button("Predict Price"):
    # Create a dataframe with the input values
    input_data = pd.DataFrame({
        "ratings": [ratings],
        "brand": [brand],
        "display": [display],
        "operating_system": [operating_system],
        "processor": [processor],
        "ram_type": [ram_type],
        "rom_type": [rom_type],
        "ram": [ram],
        "rom": [rom]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    st.write(f"Predicted Price: {prediction[0]:.2f}")