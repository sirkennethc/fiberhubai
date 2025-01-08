import openai
import streamlit as st

# Set OpenAI API Key
openai.api_key = st.secrets[sk-AUu6PX8Kn8y7phzdpiIiLXNGridtYSgS-s6JOzoEx3T3BlbkFJ5iD0Uk3Ow1O_KrgBVJ_BGFo9Ja4MRLlfZmXTsJKygA]  # Secure your key using Streamlit secrets

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
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use GPT-4 if you have access
        messages=[
            {"role": "system", "content": "You are an AI assistant for Allo Fiber Hub Technicians. Provide clear and actionable advice."},
            {"role": "user", "content": user_query}
        ],
        max_tokens=500
    )

    # Display the Response
    st.write("### Response:")
    st.write(response["choices"][0]["message"]["content"])
