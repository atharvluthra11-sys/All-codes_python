import streamlit as st
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6Lq_0aIIH2ww2FgeLn-HTA-bJEkSU3DoYg_pEbZFpD_Tg")
st.title("🤖 Your Everyday Bot")

name = st.text_input("Enter your name")
question = st.text_input("Ask me anything!")

if st.button("Generate Response!"):
    if question:
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",
                contents=question
            )

            st.write(f"Hello {name}!")
            st.write(response.text)
    else:
        st.warning("Please enter a question.") 