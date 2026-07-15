import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model and Scaler
# -----------------------------
model = joblib.load("best_house_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏠 California House Price Prediction")

st.write(
    "Enter the housing details below and click **Predict House Price**."
)

# -----------------------------
# User Inputs
# -----------------------------
medinc = st.number_input("Median Income", value=5.0)
houseage = st.number_input("House Age", value=20.0)
averooms = st.number_input("Average Rooms", value=5.0)
avebedrms = st.number_input("Average Bedrooms", value=1.0)
population = st.number_input("Population", value=1000.0)
aveoccup = st.number_input("Average Occupancy", value=3.0)
latitude = st.number_input("Latitude", value=34.0)
longitude = st.number_input("Longitude", value=-118.0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "MedInc": [medinc],
        "HouseAge": [houseage],
        "AveRooms": [averooms],
        "AveBedrms": [avebedrms],
        "Population": [population],
        "AveOccup": [aveoccup],
        "Latitude": [latitude],
        "Longitude": [longitude]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    st.success(
        f"🏡 Predicted Median House Value: {prediction[0]:.3f}"
    )