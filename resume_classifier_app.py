import streamlit as st
import joblib
from bs4 import BeautifulSoup
import re

# Load model, vectorizer, label encoder
model = joblib.load("resume_classifier.pkl")
vectorizer = joblib.load("vectorizer.pkl")
le = joblib.load("label_encoder.pkl")

# Cleaning functions
def clean_html(text):
    return BeautifulSoup(text, "html.parser").get_text()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# Prediction function
def predict_resume_category(resume_text):
    cleaned_resume = clean_text(clean_html(resume_text))
    resume_vector = vectorizer.transform([cleaned_resume])
    predicted_label = model.predict(resume_vector)
    predicted_category = le.inverse_transform(predicted_label)
    return predicted_category[0]

# Streamlit UI
st.title("📄 Resume Classification Tool")
st.write("Upload or paste a resume to get its predicted job category.")

# Option 1: Paste resume text
resume_text = st.text_area("Paste your resume here:")

# Option 2: Upload resume file
uploaded_file = st.file_uploader("Or upload a resume file (.txt)", type=["txt"])

if uploaded_file is not None:
    resume_text = uploaded_file.read().decode("utf-8")

# Predict button
if st.button("Predict Category"):
    if resume_text and resume_text.strip() != "":
        prediction = predict_resume_category(resume_text)
        st.success(f"Predicted Category: {prediction}")
    else:
        st.error("Please enter or upload a resume to predict.")
