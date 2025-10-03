# 📄 Resume Classification Tool

This project is a **Resume Classification App** built with **Streamlit** that predicts the job category of a resume.  
It supports **both pasting resume text and uploading resume files (.txt)** for instant classification.

---

## 🎯 Project Objective

The aim of this project is to automate the resume screening process by using a trained machine learning model to classify resumes into their appropriate categories.  
This saves time for HR professionals and improves accuracy in shortlisting candidates.

---

## ⚙ How It Works

1. Load trained ML model files:
    - `resume_classifier.pkl`
    - `vectorizer.pkl`
    - `label_encoder.pkl`

2. Streamlit UI allows users to:
    - Paste resume text
    - Upload a `.txt` resume file

3. The app cleans the resume text and predicts the category.

---

## 📁 Project Files

| File Name                  | Description                                    |
|----------------------------|-----------------------------------------------|
| resume_classifier_app.py  | Main Streamlit app code                      |
| resume_classifier.pkl      | Trained machine learning model               |
| vectorizer.pkl            | TF-IDF vectorizer used for text processing   |
| label_encoder.pkl         | Label encoder for categories                  |
| requirements.txt          | Required Python libraries                     |
| README.md                 | This project documentation                     |

---

## 🚀 How to Run

### **Step 1 — Clone Repository**
```bash
git clone https://github.com/kb879135-del/resume-classifier-app.git
cd resume-classifier-app
