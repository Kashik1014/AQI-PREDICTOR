import streamlit as st
import pickle

# Load trained model
with open(r"C:\Users\VYSHNAVI\Desktop\internship\projectrf.pkl", 'rb') as file:
    rf_regressor = pickle.load(file)

# Set page layout and theme
st.set_page_config(page_title="🌏 AQI Prediction", layout="wide")
# Custom background colors
st.markdown(
    """
    <style>
        .main { background-color: #F5F7FA; }
        h1 { color: #2E86C1; }
        h2 { color: #117A65; }
        .stMetric { font-size: 22px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🌏 AQI Prediction Project")
st.write("🔍 **Enter atmospheric gas concentrations to predict air quality.**")

# Sidebar for Inputs
st.sidebar.title("💨 Enter Pollutant Levels")
SO2 = st.sidebar.number_input("🟡 SO2 (Sulfur Dioxide in ppm)", min_value=0.0, value=0.0, format="%.2f")
CO = st.sidebar.number_input("🔴 CO (Carbon Monoxide in ppm)", min_value=0.0, value=0.0, format="%.2f")
NO = st.sidebar.number_input("🟠 NO (Nitric Oxide in ppm)", min_value=0.0, value=0.0, format="%.2f")
NO2 = st.sidebar.number_input("🟣 NO2 (Nitrogen Dioxide in ppm)", min_value=0.0, value=0.0, format="%.2f")
NOX = st.sidebar.number_input("⚫ NOX (Nitrogen Oxides in ppm)", min_value=0.0, value=0.0, format="%.2f")
NH3 = st.sidebar.number_input("🟢 NH3 (Ammonia in ppm)", min_value=0.0, value=0.0, format="%.2f")
O3 = st.sidebar.number_input("💙 O3 (Ozone in ppm)", min_value=0.0, value=0.0, format="%.2f")
WS = st.sidebar.number_input("🌬️ WS (Wind Speed in m/s)", min_value=0.0, value=0.0, format="%.2f")
WD = st.sidebar.number_input("🧭 WD (Wind Direction in degrees)", min_value=0.0, value=0.0, format="%.2f")
RH = st.sidebar.number_input("💦 RH (Relative Humidity in %)", min_value=0.0, value=0.0, format="%.2f")
SR = st.sidebar.number_input("☀️ SR (Solar Radiation in W/m²)", min_value=0.0, value=0.0, format="%.2f")
TC = st.sidebar.number_input("🌡️ TC (Temperature in °C)", min_value=0.0, value=0.0, format="%.2f")

# Prediction Logic
if st.sidebar.button("🔎 Predict AQI"):
    input_data = [[SO2, CO, NO, NO2, NOX, NH3, O3, WS, WD, RH, SR, TC]]
    prediction = rf_regressor.predict(input_data)[0]

    st.subheader("📝 Predicted AQI Level:")
    st.metric(label="AQI Score", value=round(prediction, 2))

    # Display AQI Category and Visual Indicators
    if prediction <= 50:
        category = "✅ Good Air Quality 🌿"
        color = "green"
        bar_level = 0.2
    elif prediction <= 100:
        category = "🟡 Moderate Air Quality 😷"
        color = "blue"
        bar_level = 0.4
    elif prediction <= 150:
        category = "🟠 Unhealthy for Sensitive Groups 😵‍💫"
        color = "orange"
        bar_level = 0.6
    elif prediction <= 200:
        category = "🔴 Unhealthy Air Quality 🚨"
        color = "red"
        bar_level = 0.8
    else:
        category = "☠️ Hazardous Air Quality ⚠️"
        color = "darkred"
        bar_level = 1.0

    # Styled Output with Colors
    st.markdown(f"<h3 style='color:{color};'>{category}</h3>", unsafe_allow_html=True)
    st.progress(bar_level)

    st.warning("🚨 **Health Advisory**: Take precautions based on AQI level.")
