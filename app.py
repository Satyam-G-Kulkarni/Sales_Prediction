import streamlit as st import pandas as pd import numpy as np import pickle

Load trained model (make sure the model file is in the same directory)

with open("best_rf_model.pkl", "rb") as f: model = pickle.load(f)

st.title("Sales Prediction App")

st.markdown(""" This app predicts the number of products sold based on country, store, product, and date details. """)

Sidebar inputs

st.sidebar.header("Input Features")

country = st.sidebar.selectbox("Country", options=[0, 1, 2, 3, 4, 5]) store = st.sidebar.selectbox("Store", options=[0, 1, 2]) product = st.sidebar.selectbox("Product", options=[0, 1, 2, 3, 4]) day = st.sidebar.selectbox("Day", options=list(range(1, 32))) month = st.sidebar.selectbox("Month", options=list(range(1, 13))) year = st.sidebar.selectbox("Year", options=[2010, 2011, 2012, 2013, 2014, 2015, 2016])

Create input dataframe

input_df = pd.DataFrame({ 'country': [country], 'store': [store], 'product': [product], 'day': [day], 'month': [month], 'year': [year] })

Show input

st.subheader("Input Data") st.write(input_df)

Prediction

if st.button("Predict Sales"): prediction = model.predict(input_df) st.subheader("Predicted Number of Products Sold") st.success(f"{int(prediction[0])} units")
