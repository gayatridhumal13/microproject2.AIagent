"""
Simple LangChain Agent — Calculator + Web Search
--------------------------------------------------
Uses LangChain Messages + AgentExecutor with two types of tools:

1. Calculator tools:
   - add
   - subtract
   - multiply
   - divide

2. DuckDuckGo web search

Install:
    pip install langchain langchain-huggingface langchain-community duckduckgo-search python-dotenv

Make sure your Hugging Face API token is available in your .env file:
    HUGGINGFACEHUB_API_TOKEN=your_token
"""

from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.tools import tool
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate



load_dotenv()




@tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@tool
def divide(a: float, b: float):
    """Divide the first number by the second."""

    if b == 0:
        return "Error: Cannot divide by zero."

    return a / b




search = DuckDuckGoSearchRun()




endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=256,
    temperature=0
)

model = ChatHuggingFace(
    llm=endpoint
)




tools = [
    add,
    subtract,
    multiply,
    divide,
    search
]



prompt = ChatPromptTemplate.from_messages([
    
    SystemMessage(
        content="""
You are a helpful AI assistant.

You have access to calculator tools and a web search tool.

Rules:
- Use calculator tools whenever mathematical calculation is needed.
- Use web search for current information or facts you are unsure about.
- If no tool is needed, answer directly.
"""
    ),

    
    ("human", "{input}"),

    
    ("placeholder", "{agent_scratchpad}")
])


agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""You are a helpful AI assistant.

Use calculator tools whenever mathematical calculation is needed.
If no tool is needed, answer directly.
"""
)




if __name__ == "__main__":

    print("Simple AI Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        try:
            result = agent.invoke({
                "messages": [
                    HumanMessage(content=user_input)
                ]
            })

            final_message = result["messages"][-1]

            print("\nAssistant:", final_message.content, "\n")

        except Exception as e:
            print("\nError:", e, "\n")