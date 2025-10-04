import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")

prompt = st.text_input("프롬프트 입력")
if st.button("테스트 실행"):
    response = model.generate_content(prompt)
    st.write(response.text)
