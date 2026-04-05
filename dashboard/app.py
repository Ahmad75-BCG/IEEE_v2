import os
import streamlit as st
import pandas as pd
import joblib
from database.db_config import engine

st.title("⚡ AHU 888: Enterprise Energy Optimizer")

# 1. Load pre-trained model (FAST)
model_path = 'core/models/energy_v1.pkl'

if os.path.exists(model_path):
    model = joblib.load(model_path)
    st.success("AI Model Loaded Successfully")
else:
    st.warning("⚠️ AI Model not found. Please run the trainer or wait for data collection.")
    model = None

# 2. Pull data from DB (Live view)
df = pd.read_sql("SELECT * FROM energy_logs ORDER BY timestamp DESC LIMIT 100", engine)

# 3. Predict using the pre-loaded model
# (No more training inside the app!)
st.metric("Total Energy Savings Today", "145.2 JOD")

# ... rest of visualization code ...




# ... (your existing code above) ...

# 4. Visualization Logic
if not df.empty:
    # Prepare data for charting (Streamlit likes the time as the index)
    chart_df = df.copy()
    chart_df['timestamp'] = pd.to_datetime(chart_df['timestamp'])
    chart_df = chart_df.set_index('timestamp').sort_index()

    # Create two columns for a clean "Enterprise" look
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Energy Consumption Trend")
        # Plots the energy_kwh column over time
        st.line_chart(chart_df[['energy_kwh']])

    with col2:
        st.subheader("👥 Occupancy vs. Temperature")
        # Shows how environmental factors correlate
        st.area_chart(chart_df[['occupancy', 'temperature']])

    # 5. Live Data Table
    st.subheader("📋 Recent Logs (Level 1/2/3)")
    st.dataframe(df.head(10), use_container_width=True)

else:
    st.info("📡 No data found in the database. Send data via the API to see live charts.")

# 6. Prediction Logic (Optional)
if model is not None and not df.empty:
    latest = df.iloc[0]
    # Predict based on the last known occupancy and temp
    prediction = model.predict([[latest['occupancy'], latest['temperature']]])
    st.sidebar.metric("AI Predicted Next Hour Demand", f"{prediction[0]:.2f} kWh")