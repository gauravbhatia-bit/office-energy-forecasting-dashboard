
import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("energy_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("⚡ Office Energy Consumption Forecasting")
st.markdown("Predict energy consumption and calculate CO₂ savings for any office building.")

st.sidebar.header("Building & Weather Parameters")
t_out = st.sidebar.slider("Outside Temperature (°C)", -10.0, 40.0, 15.0)
rh_out = st.sidebar.slider("Outside Humidity (%)", 10.0, 100.0, 60.0)
windspeed = st.sidebar.slider("Wind Speed (m/s)", 0.0, 15.0, 4.0)
hour = st.sidebar.slider("Hour of Day", 0, 23, 9)
day_of_week = st.sidebar.selectbox("Day of Week", [0,1,2,3,4,5,6],
                format_func=lambda x: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][x])
month = st.sidebar.slider("Month", 1, 12, 6)
is_weekend = 1 if day_of_week >= 5 else 0
is_office_hours = 1 if 8 <= hour <= 18 else 0

st.sidebar.header("Recent Consumption (Wh)")
lag_1 = st.sidebar.number_input("10 min ago", value=100.0)
lag_6 = st.sidebar.number_input("1 hour ago", value=110.0)
lag_144 = st.sidebar.number_input("24 hours ago", value=105.0)

rolling_mean_6 = (lag_1 + lag_6) / 2
rolling_std_6 = abs(lag_1 - lag_6) / 2

features = ['T_out','RH_out','Windspeed','hour','day_of_week',
            'month','is_weekend','is_office_hours',
            'lag_1','lag_6','lag_144','rolling_mean_6','rolling_std_6']

input_data = pd.DataFrame([[t_out, rh_out, windspeed, hour, day_of_week,
                            month, is_weekend, is_office_hours,
                            lag_1, lag_6, lag_144,
                            rolling_mean_6, rolling_std_6]],
                          columns=features)

if st.button("⚡ Predict Energy Consumption"):
    pred = model.predict(input_data)[0]
    co2 = pred * 0.000233

    col1, col2 = st.columns(2)
    col1.metric("Predicted Consumption", f"{pred:.1f} Wh")
    col2.metric("CO₂ Emitted", f"{co2:.4f} kg")

    st.subheader("💡 CO₂ Savings Calculator")
    reduction = st.slider("If consumption is reduced by (%)", 5, 50, 15)
    saved_wh = pred * (reduction / 100)
    saved_co2_monthly = saved_wh * 0.000233 * 30 * 24 * 6
    st.success(f"💚 Reducing by {reduction}% saves {saved_co2_monthly:.2f} kg CO₂ per month!")

    if hour < 8 or hour > 18:
        st.warning("⚠️ High consumption outside office hours — possible energy waste!")
    else:
        st.info("✅ Consumption within normal office hours.")
