from google import genai
import streamlit as st

api_key = st.secrets["gemini"]["api_key"
client = genai.Client(
    api_key = api_key,
)

def get_response(prompt):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=prompt,
    )
    print(response.text)
    return response.text
