# microproject2.AIagent
AI agent project2
microproject 2: Dual-Capability AI Agent

A smart AI agent built with LangChain that handles mathematical calculations and web-based information queries using external tools.

🚀 Features:
🧮 Arithmetic Engine — Addition, subtraction, multiplication, and division.
🌐 Web Search — DuckDuckGo integration for retrieving information from the web.
🧠 Intelligent Tool Routing — Selects the appropriate tool based on the user's query.
💬 Interactive CLI — Chat with the agent directly through the terminal.
🛡️ Error Handling — Handles errors such as division by zero.
🛠️ Tech Stack:
Python
LangChain
Llama 3.1 8B Instruct
Hugging Face
DuckDuckGo Search
📦 Installation:
pip install langchain langchain-huggingface langchain-community duckduckgo-search python-dotenv


Add your Hugging Face API token to .env:

HUGGINGFACEHUB_API_TOKEN=your_token_here

▶️ Run:
python AIagent.py


Type exit or quit to stop the agent.

