
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load API key from .env
load_dotenv()

# Initialize the Groq model
model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    temperature=0
)

# Send a prompt to the model
reply = model.invoke(
    "Why do parrots talk? Answer in two sentences."
)

# Print the response
print(reply.text)

# Print response type, e.g; AIMessage
print(type(reply).__name__)

# Print token usage info like Input tokens, Output tokens, Total tokens.
print(reply.usage_metadata)

# Print model name(openai/gpt-oss-120b) and finish reason(stop)
print(
    reply.response_metadata.get("model_name"),
    reply.response_metadata.get("finish_reason")
)
