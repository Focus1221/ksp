import streamlit as st
# Вместо прямого ключа читаем его из настроек сайта
API_KEY = st.secrets["GEMINI_KEY"]
genai.configure(api_key=API_KEY)