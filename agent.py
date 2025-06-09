from datetime import datetime
from langgraph.prebuilt import create_react_agent
from langchain_deepseek import ChatDeepSeek
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
from langchain_core.tools import tool


# graph is here
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY") 

@tool
def get_current_time() -> dict:
    """Return the current UTC time in ISO‑8601 format.
    Example → {"utc": "2025‑05‑21T06:42:00Z"}"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")



llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

graph = create_react_agent(
    model=llm,
    tools=[get_current_time],
    prompt="""Respond normally, but if the user mentions 'time', 
           use the tool to get the current UTC time."""
)