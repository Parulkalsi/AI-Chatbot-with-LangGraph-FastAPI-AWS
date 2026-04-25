import streamlit as st
import requests

API_URL = "http://3.104.35.80:8000/chat"

st.title("Chatbot")

user_message = st.chat_input("Ask something")

if user_message:
    st.write("You:", user_message)

    response = requests.post(API_URL, json={"message": user_message})
    st.write("AI:", response.json()["reply"])


