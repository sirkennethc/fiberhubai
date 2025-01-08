import openai
import streamlit as st

# Use Streamlit Secrets to securely access the API key
openai.api_key = st.secrets["openai_api_key"]

# App Title
st.title("Allo Fiber Hub Technician AI Assistant")

# Sidebar Description
st.sidebar.header("About")
st.sidebar.write("""
This AI assistant helps Allo Fiber Hub Technicians troubleshoot, configure, and maintain fiber hub equipment.
Ask a question to get started!
""")

# User Input
user_query = st.text_input("Enter your question or describe your problem:")

# Generate a Response
if user_query:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant for Allo Fiber Hub Technicians. Provide clear and actionable advice."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=500
        )
        st.write("### Response:")
        st.write(response["choices"][0]["message"]["content"])
    except Exception as e:
        st.error(f"An error occurred: {e}")


