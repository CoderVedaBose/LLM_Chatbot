# LangChain Groq Chatbot

A simple Python chatbot that uses LangChain with the Groq-hosted
`openai/gpt-oss-120b` model. The project includes both a command-line example and
a Streamlit web interface.

## Features

- Generate responses through a Groq-hosted language model
- Run prompts from the command line
- Use a browser-based chat interface with Streamlit
- Display response metadata, token usage, model name, and finish reason
- Load API credentials securely from a `.env` file

## Project Structure

```text
first_llm/
|-- app.py            # Streamlit web interface
|-- main.py           # Command-line chatbot example
|-- requirements.txt  # Python dependencies
`-- new_env/          # Optional local virtual environment
```

## Prerequisites

- Python 3.10 or newer
- A Groq API key
- Internet access

## Installation

1. Clone or download this repository and open its directory:

   ```powershell
   cd "C:\Users\BEDANTO BOSE\Desktop\Gen & Agentic AI\first_llm"
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation scripts, allow them for the current process:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

3. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   pip install streamlit
   ```

4. Create a `.env` file in the project root and add your Groq API key:

   ```dotenv
   GROQ_API_KEY=gsk_your_api_key_here
   ```

   Do not commit `.env` or share the API key publicly.

## Usage

### Streamlit web app

Run:

```powershell
streamlit run app.py
```

Streamlit will open the app in your browser. Enter a question and click
**Generate Response**.

### Command-line app

Run:

```powershell
python main.py
```

The script sends a predefined prompt about parrots and prints the response,
message type, token usage, model name, and finish reason.

## Configuration

The model configuration is in both Python files:

```python
model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    temperature=0
)
```

Change `temperature` to adjust response variability. Lower values produce more
focused and deterministic answers.

## Troubleshooting

- **Missing API key:** confirm that `.env` exists in the project root and contains
  `GROQ_API_KEY`.
- **Module not found:** activate the virtual environment and reinstall dependencies.
- **Streamlit command unavailable:** install Streamlit with
  `pip install streamlit`.
- **Groq authentication error:** verify that the key is valid and has not been revoked.
