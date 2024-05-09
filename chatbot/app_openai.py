# Import the necessary classes from the LangChain library
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Import the Streamlit library for building the user interface
import streamlit as st

import os

# Import the load_dotenv function from the python-dotenv library to load environment variables
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Enable LangChain's tracing feature for debugging
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# Define a ChatPromptTemplate with a system message and a user message placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"),
    ("user", "Question:{question}")
])

#frontend
st.title("AI Chatbot with Langchain")
input_text = st.text_input("Search the topic you want")


# Initialize the language model with the GPT-3.5-turbo model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Initialize the output parser to handle string outputs
output_parser = StrOutputParser()

# Create a chain by combining the prompt, language model, and output parser
chain = prompt | llm | output_parser

# If the user has entered a query in the text input field
if input_text:
    # Invoke the chain with the user's query and display the result
    st.write(chain.invoke({'question': input_text}))