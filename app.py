import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze/"

st.title("Text Analyzer")

url = st.text_input("Enter the URL:")

if st.button("Analyze"):
    if url:
        response = requests.post(API_URL, json={"url": url})

        if response.status_code == 200:
            analysis_result = response.json()
            st.write("### Analysis Result")
            result = "\n".join([f"**{key.replace('_', ' ').title()}**: {value} \n" for key, value in analysis_result.items()])
            st.write(result)
        else:
            st.error("Error analyzing the text. Please try again.")
    else:
        st.warning("Please enter a valid URL.")
