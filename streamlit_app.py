import os
from const import mykey
from langchain.llms import OpenAI
import streamlit as st

os.environ["open_api_key"] = mykey

st.title('langchain demo with openAI')

input_text = st.text_input("ask question")

llm = OpenAI(temperature=0.9)

if input_text:
    st.write(llm(input_text))