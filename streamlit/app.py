import streamlit as st

# Title of the app
st.title("💬 Simple Streamlit App")

# Text input
user_input = st.text_input("Enter your name:")

# Button
if st.button("Greet Me"):
    st.success(f"Hello, {user_input}! 👋 Welcome to Streamlit!")

# Display some static info
st.info("This is a basic Streamlit app. You can expand it with forms, charts, and more!")