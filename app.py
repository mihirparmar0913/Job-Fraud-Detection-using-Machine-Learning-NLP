import streamlit as st
import pickle
import numpy as np

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

# App title
st.set_page_config(page_title="Job Fraud Detector", layout="centered")
st.title("🚨 Job Fraud Detection System")
st.write("Paste a job description to check whether it is potentially fraudulent.")

# Text input
job_text = st.text_area(
    "Job Description",
    height=250,
    placeholder="Paste the full job description here..."
)

# Threshold
THRESHOLD = 0.3

if st.button("Check Fraud Risk"):
    if job_text.strip() == "":
        st.warning("Please enter a job description.")
    else:
        # Vectorize input
        X = tfidf.transform([job_text])

        # Predict probability
        prob = model.predict_proba(X)[0][1]
        prediction = int(prob >= THRESHOLD)

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error(f"⚠️ This job is likely FRAUDULENT\n\nFraud Probability: {prob:.2f}")
        else:
            st.success(f"✅ This job appears GENUINE\n\nFraud Probability: {prob:.2f}")
