from fastapi import FastAPI, Path , HTTPException, Query
from fastapi.responses import JSONResponse
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel
from typing import  Annotated , TypedDict
from langraph_chatbot import chatbot
import operator
import json

from langgraph.graph import add_messages

app = FastAPI()

class ChatRequest(BaseModel):
    message: str    

def user_message(user_input:str):
    response = chatbot.invoke(
        {'messages': [HumanMessage(content=user_input)]}
    )
    return response

@app.get("/")
def home_page():
    return {'message': 'Welcome to the Chatbot API!'}

@app.get('/health')
def health_check():
    return{'status':'ok'}


@app.post('/chat')
def chat(request: ChatRequest):
    try:
        user_input = request.message
        response = user_message(user_input) 
        ai_reply = response['messages'][-1].content
        return JSONResponse(status_code=200, content={'reply': ai_reply})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




    