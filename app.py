
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load API key from .env
load_dotenv()

# Initialize the model
model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    temperature=0
)

# Page configuration
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Frontend title
st.title("🤖LangChain Chatbot")

st.write("Ask me anything!")

# Input box for user
user_prompt = st.text_input(
    "Enter your question:",
    placeholder="Why is C.P.U?"
)

# Button
if st.button("Generate Response"):

    if user_prompt:

        with st.spinner("AI is thinking..."):

            # Send prompt to LLM
            reply = model.invoke(user_prompt)

            # Display response
            st.subheader("AI Response")
            st.write(reply.text)

            # Display additional information
            st.subheader("Response Information")

            st.write("Message Type:", type(reply).__name__)

            st.write("Token Usage:", reply.usage_metadata)

            st.write(
                "Model:",
                reply.response_metadata.get("model_name")
            )

            st.write(
                "Finish Reason:",
                reply.response_metadata.get("finish_reason")
            )

    else:
        st.warning("Please enter a question first.")
