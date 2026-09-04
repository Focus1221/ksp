import streamlit as st
import google.generativeai as genai
API_KEY = st.secrets["GEMINI_KEY"]
genai.configure(api_key=API_KEY)
