# LangChain Groq Chatbot

A simple Python chatbot built using **LangChain** and the Groq-hosted `openai/gpt-oss-120b` model. This project includes both a command-line chatbot and a web-based chat interface built with Streamlit.

## Features

- Generate responses using a Groq-hosted large language model
- Run prompts through a command-line interface
- Interact with the chatbot through a Streamlit web application
- Display response metadata, token usage, model name, and finish reason
- Securely load API credentials using environment variables and a `.env` file

## Screenshots

### Chatbot Web Interface

![LangChain Groq Chatbot Interface](screenshots/chatbot-interface.png)

### AI-Generated Response

![LangChain Groq Chatbot Response](screenshots/chatbot-response.png)

## Project Structure

```text
first_llm/
│
├── app.py                       # Streamlit web interface
├── main.py                      # Command-line chatbot example
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── .env                          # API credentials (not committed)
├── .gitignore                    # Git ignore rules
│
└── screenshots/
    ├── chatbot-interface.png     # Chatbot interface screenshot
    └── chatbot-response.png      # Chatbot response screenshot
```

## Tech Stack

- **Python**
- **LangChain**
- **Groq API**
- **OpenAI GPT-OSS 120B**
- **Streamlit**
- **python-dotenv**

## Prerequisites

- Python 3.10 or newer
- A Groq API key
- Internet connection

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```powershell
cd first_llm
```

Alternatively, if you have already downloaded the project, navigate to its folder:

```powershell
cd "C:\Users\BEDANTO BOSE\Desktop\Gen & Agentic AI\first_llm"
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation scripts, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If Streamlit is not included in your `requirements.txt`, install it separately:

```bash
pip install streamlit
```

### 4. Configure the API key

Create a `.env` file in the project root directory and add your Groq API key:

```dotenv
GROQ_API_KEY=gsk_your_api_key_here
```

Replace `gsk_your_api_key_here` with your actual Groq API key.

**Important:** Never commit your `.env` file or expose your API key publicly.

## Usage

### Streamlit Web Application

Run the following command:

```bash
streamlit run app.py
```

Streamlit will launch the application in your browser.

Enter your prompt in the interface and click **Generate Response** to receive an AI-generated answer.

### Command-Line Application

Run:

```bash
python main.py
```

The script sends a predefined prompt about parrots to the language model and prints:

- Generated response
- Message type
- Token usage
- Model name
- Finish reason

## Model Configuration

The model is initialized using LangChain's `init_chat_model` function:

```python
model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    temperature=0
)
```

### Temperature

The `temperature` parameter controls the variability of generated responses.

- `temperature=0` produces more focused and deterministic responses.
- Higher temperature values generally produce more varied and creative responses.

## Troubleshooting

| Issue | Solution |
|---|---|
| Missing API key | Ensure that `.env` exists in the project root and contains `GROQ_API_KEY`. |
| Module not found | Activate your virtual environment and install the required dependencies. |
| Streamlit command unavailable | Install Streamlit using `pip install streamlit`. |
| Groq authentication error | Verify that your API key is valid and has not been revoked. |
| Application fails to launch | Check that all dependencies are installed and that you are running the command from the project directory. |

## Security

- Store API keys in a `.env` file.
- Add `.env` to `.gitignore`.
- Never hardcode API keys in Python source files.
- Never upload your API credentials to GitHub.

---

Built using Python, LangChain, Groq, and Streamlit.
