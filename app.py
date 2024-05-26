import os
import openai
import streamlit as st
from openai import OpenAI
from functions import *
openai.api_key = os.getenv("sk-proj-c6mr4IsptbEPpYRwUoiaT3BlbkFJH87Ci5t3HjpbFjYVRl1T")


def main():

    st.title("PDF SCAN")

    uploaded_file = st.file_uploader("Choose a PDF file to upload", type="pdf")
    if uploaded_file is not None:
        if st.button("Read PDF"):
            save_uploaded_file(uploaded_file)
            st.write("Please wait while we learn the PDF.")
            learn_pdf(uploaded_file.name)
            st.write("PDF reading completed! Now you may ask a question")
            os.remove(uploaded_file.name)
    user_input = st.text_input("Enter your Query:")

    if st.button("Send"):
        st.write("You:", user_input)
        response = Answer_from_documents(user_input, "sk-proj-c6mr4IsptbEPpYRwUoiaT3BlbkFJH87Ci5t3HjpbFjYVRl1T")
        st.write("Bot: "+response)

def get_api_key():
    return os.getenv("sk-proj-c6mr4IsptbEPpYRwUoiaT3BlbkFJH87Ci5t3HjpbFjYVRl1T")

if __name__ == "__main__":
    main()
