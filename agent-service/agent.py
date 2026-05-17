
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from tools import search_web, summarize_url
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

@tool
def web_search(query: str) -> str:
    """Search the web for current information. Input must be a simple search query string only."""
    return search_web(query)
@tool
def read_url(url: str) -> str:
    """Read and extract text content from a webpage URL. Use this to get detailed information from a specific website."""
    return summarize_url(url)

agent = create_react_agent(
    model=llm,
    tools=[web_search, read_url],
    prompt="You are a research assistant. When searching, always use a simple short query string. Never add extra parameters."
)

def run_agent(task: str) -> str:
    result = agent.invoke({
        "messages": [{"role": "user", "content": task}]
    })
    return result["messages"][-1].content