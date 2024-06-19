import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("🧥 TeesGPT 🧥")

st.subheader("Smart Analytics for T-Shirt Businesses")

question = st.text_input("Need insights on your T-Shirt business? Your AI assistant is ready! ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.subheader("The Answer to your Question is: ")
    st.write(response)






