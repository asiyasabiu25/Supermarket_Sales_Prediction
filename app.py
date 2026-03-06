
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("supermarket_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

st.set_page_config(page_title="Supermarket Sales Predictor", page_icon="🛒")
st.title("🛒 Supermarket Sales Predictor")
st.markdown("Predict transaction sales using machine learning.")

col1, col2 = st.columns(2)

with col1:
    unit_price = st.slider("Unit Price ($)", 10.0, 100.0, 50.0)
    quantity = st.slider("Quantity", 1, 10, 3)
    rating = st.slider("Customer Rating", 4.0, 10.0, 7.0)
    hour = st.slider("Hour of Purchase", 10, 20, 14)

with col2:
    branch = st.selectbox("Branch", ["A", "B", "C"])
    customer_type = st.selectbox("Customer Type", ["Member", "Normal"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    payment = st.selectbox("Payment Method", ["Cash", "Credit card", "Ewallet"])
    product_line = st.selectbox("Product Line", [
        "Health and beauty", "Electronic accessories",
        "Home and lifestyle", "Sports and travel",
        "Food and beverages", "Fashion accessories"])
    day_of_week = st.selectbox("Day of Week", ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

if st.button("🔮 Predict Sales", use_container_width=True):
    day_map = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
    is_weekend = 1 if day_map[day_of_week] >= 5 else 0

    input_dict = {
        "Unit price": unit_price, "Quantity": quantity, "Rating": rating,
        "hour": hour, "day_of_week": day_map[day_of_week],
        "month": 1, "is_weekend": is_weekend,
        "Branch_B": 1 if branch=="B" else 0,
        "Branch_C": 1 if branch=="C" else 0,
        "Customer type_Normal": 1 if customer_type=="Normal" else 0,
        "Gender_Male": 1 if gender=="Male" else 0,
        "Payment_Credit card": 1 if payment=="Credit card" else 0,
        "Payment_Ewallet": 1 if payment=="Ewallet" else 0,
    }
    for line in ["Electronic accessories","Fashion accessories","Food and beverages",
                 "Health and beauty","Home and lifestyle","Sports and travel"]:
        key = f"Product line_{line}"
        input_dict[key] = 1 if product_line == line else 0

    input_df = pd.DataFrame([input_dict])
    for col in feature_cols:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[feature_cols]

    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Sales: **${prediction:,.2f}**")
    st.balloons()
