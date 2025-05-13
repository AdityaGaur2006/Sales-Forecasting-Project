# app.py

import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objects as go

# App title
st.title("🧠 Sales Forecasting App using Prophet")

# Sidebar
st.sidebar.header("Configuration")
periods_input = st.sidebar.slider("How many days to forecast?", 7, 90, 30)

# Step 1: File Upload
st.sidebar.header("Upload Your Sales Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Function to process uploaded CSV
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)
        # Ensure the columns are correctly named for Prophet
        df = df.rename(columns={'Date': 'ds', 'Sales': 'y'})
        return df
    return None

# If a file is uploaded, process and forecast
if uploaded_file is not None:
    df = load_data(uploaded_file)

    # Show raw data
    with st.expander("📊 View Uploaded Data"):
        st.write(df.head())

    # Step 2: Train Prophet model
    model = Prophet()
    model.fit(df)

    # Step 3: Make future dataframe
    future = model.make_future_dataframe(periods=periods_input)
    forecast = model.predict(future)

    # Step 4: Plot forecast
    st.subheader(f"📈 Forecast for next {periods_input} days")
    fig = plot_plotly(model, forecast)
    st.plotly_chart(fig)

    # Optional: Show forecast components
    with st.expander("🔍 Forecast Components (Trend, Weekly Seasonality)"):
        fig2 = model.plot_components(forecast)
        st.write(fig2)

else:
    st.write("Please upload a CSV file to begin.")
