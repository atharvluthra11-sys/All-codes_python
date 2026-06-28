import streamlit as st
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6Lq_0aIIH2ww2FgeLn-HTA-bJEkSU3DoYg_pEbZFpD_Tg")
st.title(" Your Joke Bot")

name = st.text_input("Enter your name")

if st.button("Generate Joke"):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Tell me one short, funny joke."
    )
    st.success(response.text)
else:
    st.warning("Please give a command.") 