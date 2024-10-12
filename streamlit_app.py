import streamlit as st

# Title for the app with color
st.markdown("<h1 style='color: orange;'>Simple Prompt App</h1>")

# Input text area for the prompt with a blue label
st.markdown("<h3 style='color: blue;'>Enter your prompt:</h3>")
prompt = st.text_area("", placeholder="Type your prompt here...")

# Button to submit the prompt with green color
st.button("Submit")

