import streamlit as st
import joblib
import pandas as pd


model = joblib.load('model.pkl')  

def predict(text):
    """Untuk memprediksi hate speech dan offensive language."""
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]

st.title("Hate Speech and Offensive Language Detection")

st.write("Masukkan teks untuk mendeteksi apakah terdapat hate speech atau offensive language.")

user_input = st.text_area("Teks:", "")

if st.button("Deteksi"):
    if user_input:
        result = predict(user_input)
        if result == 1:
            st.error("Teks ini mengandung hate speech atau offensive language!")
        else:
            st.success("Teks ini aman!")
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")

