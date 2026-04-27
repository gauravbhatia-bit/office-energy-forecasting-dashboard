# ⚡ Office Energy Consumption Forecasting Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-Tuned-green?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat&logo=streamlit)
![Optuna](https://img.shields.io/badge/Optuna-50%20Trials-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_URL)

> Predict office energy consumption and calculate real-time CO₂ savings —  
> built for CleanTech and smart building applications.

## 🌐 Live Demo
👉 **[Click here to try the app](YOUR_STREAMLIT_URL)**

---

## 🌍 Problem Statement

Energy waste in office buildings is one of the most overlooked contributors 
to CO₂ emissions. Most buildings have no intelligent system to forecast 
consumption, detect waste outside office hours, or estimate savings from 
efficiency improvements.

This dashboard solves that — instantly.

---

## 🎯 What This App Does

Input current building and weather conditions → get:
- ⚡ Predicted energy consumption (Wh)
- 🌿 CO₂ emitted (kg)
- 💡 Monthly CO₂ savings if consumption is reduced by X%
- ⚠️ Alerts for energy waste outside office hours

---

## 📸 Results

### 📊 Model Performance
![Model Metrics](screenshots/model_metrics.png)

| Metric | Value |
|---|---|
| **MAE** | 22.98 Wh |
| **RMSE** | 50.96 Wh |
| **MAPE** | 22.28% |

---

### 📈 Actual vs Predicted Energy Consumption
![Actual vs Predicted](screenshots/actual_vs_predicted.png)

The model closely tracks real consumption patterns including peak 
usage spikes and overnight low-consumption periods.

---

### 🧠 SHAP Feature Importance
![SHAP Feature Importance](screenshots/shap_feature_importance.png)

**Key insight:** Recent consumption (`lag_1`, `rolling_mean_6`) 
dominates predictions — confirming that energy usage follows strong 
short-term momentum patterns. External weather (`T_out`, `RH_out`) 
and time-of-day (`hour`) are secondary but meaningful signals.

---

## ⚙️ Feature Engineering

| Feature | Type | Meaning |
|---|---|---|
| `lag_1` | Lag | Consumption 10 minutes ago |
| `lag_6` | Lag | Consumption 1 hour ago |
| `lag_144` | Lag | Consumption 24 hours ago |
| `rolling_mean_6` | Rolling | Average consumption last hour |
| `rolling_std_6` | Rolling | Volatility of last hour |
| `hour` | Time | Hour of day (0–23) |
| `is_office_hours` | Time | 1 if between 8am–6pm |
| `is_weekend` | Time | 1 if Saturday or Sunday |
| `T_out` | Weather | Outside temperature (°C) |
| `RH_out` | Weather | Outside humidity (%) |
| `Windspeed` | Weather | Wind speed (m/s) |

---

## 🤖 Model Pipeline
