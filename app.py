#Q/A Chatbot Using Streamlit and Google's Gemini Generative API

from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown



load_dotenv()

genai_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=genai_api_key)

#Functioon to interact with the gemini generative ai model and get a aresponse
def get_gemini_response(question):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(question)
    return response.text

#Initialize the streamlit app with a custom page title
st.set_page_config(page_title="Question & Answer bot")

#Display the Header for the Application
st.header("Gemini Chatbot")

input = st.text_input("Input:", key="input")
sumbit=st.button("Ask the question")


if sumbit:
    response=get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)
