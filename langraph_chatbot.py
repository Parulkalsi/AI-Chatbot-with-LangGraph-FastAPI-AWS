from typing import Annotated, List , TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
import operator
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
llm= ChatOpenAI()
search_tool = DuckDuckGoSearchRun(region = "us-en")

@tool
def get_stock_price(symbol:str) -> dict:
    """

    Fetch latest stock price for a given symbol ( eg: "AAPL","TSLA")
    Using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=MN6H719586ZZ4VF1"
    r = requests.get(url)
    return r.json()

tools = [get_stock_price, search_tool]
llm_with_tools = llm.bind_tools(tools)


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
   

def chat_node(state:State):
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return{'messages': [response]}

tool_node = ToolNode(tools)

graph = StateGraph(State)

graph.add_node("chat_node",chat_node)
graph.add_node("tools", tool_node)
graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node",tools_condition)
graph.add_edge("tools","chat_node")


chatbot = graph.compile()

# response = chatbot.invoke({'messages':[HumanMessage(content = 'Tell me the latest news')]},config = CONFIG)
# print(response['messages'][-1].content)

