import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -----------------------------
# Load Model Files
# -----------------------------
model = pickle.load(open("churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

st.title("📊 Telecom Customer Churn Prediction")
st.markdown("Machine Learning powered churn prediction system")

st.divider()

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Customer Information")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
Partner = st.sidebar.selectbox("Has Partner", ["Yes", "No"])
Dependents = st.sidebar.selectbox("Has Dependents", ["Yes", "No"])

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
MonthlyCharges = st.sidebar.slider("Monthly Charges", 0, 150, 70)

Contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

InternetService = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No"])
TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No"])

PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# -----------------------------
# Custom Threshold Control
# -----------------------------
st.sidebar.divider()
st.sidebar.subheader("Model Settings")

threshold = st.sidebar.slider(
    "Churn Decision Threshold",
    min_value=0.1,
    max_value=0.5,
    value=0.2,
    step=0.05
)

# -----------------------------
# Create Input Dictionary
# -----------------------------
input_dict = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": tenure * MonthlyCharges,
    "Contract": Contract,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "TechSupport": TechSupport,
    "PaymentMethod": PaymentMethod
}

input_df = pd.DataFrame([input_dict])

# -----------------------------
# One-Hot Encoding (Same as Training)
# -----------------------------
input_df = pd.get_dummies(input_df)

# Match training features exactly
input_df = input_df.reindex(columns=features, fill_value=0)

# Scale
input_scaled = scaler.transform(input_df)

# -----------------------------
# Prediction Section
# -----------------------------
if st.button("🚀 Predict Churn"):

    probability = model.predict_proba(input_scaled)[0][1]
    prediction = 1 if probability > threshold else 0

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")

    # Probability Display
    st.subheader("Churn Probability")
    st.progress(int(probability * 100))
    st.write(f"Probability of Churn: **{probability:.2f}**")
    st.write(f"Current Decision Threshold: **{threshold:.2f}**")

    # Risk Level
    if probability < 0.2:
        st.info("🟢 Low Risk Customer")
    elif probability < 0.5:
        st.warning("🟡 Medium Risk Customer")
    else:
        st.error("🔴 High Risk Customer")





