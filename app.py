import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved model
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data['model']
feature_names = model_data['feature_names']

st.set_page_config(page_title="Rainfall Prediction App", layout="wide")

st.title("🌧️ Rainfall Prediction Web App")

st.sidebar.header("User Input Parameters")

def user_input_features():
    pressure = st.sidebar.slider('Pressure (hPa)', 990.0, 1035.0, 1015.0)
    dewpoint = st.sidebar.slider('Dewpoint (°C)', -5.0, 35.0, 15.0)
    humidity = st.sidebar.slider('Humidity (%)', 10, 100, 80)
    cloud = st.sidebar.slider('Cloud (%)', 0, 100, 50)
    sunshine = st.sidebar.slider('Sunshine (hours)', 0.0, 12.0, 4.0)
    winddirection = st.sidebar.slider('Wind Direction (°)', 0, 360, 90)
    windspeed = st.sidebar.slider('Wind Speed (km/h)', 0.0, 60.0, 20.0)

    data = {
        'pressure': pressure,
        'dewpoint': dewpoint,
        'humidity': humidity,
        'cloud': cloud,
        'sunshine': sunshine,
        'winddirection': winddirection,
        'windspeed': windspeed
    }
    features = pd.DataFrame([data])
    return features

input_df = user_input_features()

st.subheader('User Input Parameters')
st.write(input_df)

# Prediction
prediction = model.predict(input_df)
prediction_label = "🌧️ Rainfall" if prediction[0] == 1 else "☀️ No Rainfall"

st.subheader('Prediction Result')
st.success(prediction_label)
