import streamlit as st
from langchain_groq import ChatGroq

# Initialize the LLM with the Groq API key and model
llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.1-70b-versatile",
)

# Streamlit application title and description
st.title("Chat with Groq LLM")
st.markdown("Enter a question below, and get an answer from the model!")

# Text input field for the user to type their question
user_question = st.text_input("Ask a question:")

# Function to get the model's response
def get_response(question):
    if question:
        response = llm.invoke(question)
        return response.content
    return "Please enter a question to get an answer."

# Display the response when the user enters a question
if user_question:
    response_content = get_response(user_question)
    st.write("Model's response:")
    st.write(response_content)
