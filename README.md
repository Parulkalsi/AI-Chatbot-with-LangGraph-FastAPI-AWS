# AI-Chatbot-with-LangGraph-FastAPI-AWS
This project is an end-to-end production-grade AI chatbot system built using modern LLM orchestration tools and deployed on the cloud.
It combines:

LangGraph for agentic workflows
FastAPI for backend APIs
Streamlit for a simple interactive UI
Docker for containerization
AWS EC2 for production deployment

The chatbot is capable of:

Answering general queries
Performing real-time web search
Fetching live stock market data

🧠 Architecture Overview
User (Streamlit UI)
        ↓
FastAPI Backend (/chat endpoint)
        ↓
LangGraph Agent (LLM + Tools)
        ↓
Tools Layer
   ↙           ↘
Stock API     Web Search

⚙️ Tech Stack
LLM & Orchestration: LangGraph, LangChain, OpenAI
Backend: FastAPI
Frontend: Streamlit
Tools Integration: DuckDuckGo Search, Alpha Vantage API
Deployment: Docker, AWS EC2
Environment Management: python-dotenv

✨ Key Features
🤖 Intelligent Agent (LangGraph)
Built using StateGraph workflow
Supports tool calling dynamically
Maintains conversation state

🔧 Tool Integrations
📈 Stock Price Tool
Fetches real-time stock data using Alpha Vantage API
🌐 Web Search Tool
Uses DuckDuckGo for real-time information retrieval

⚡ FastAPI Backend
/chat endpoint for AI interaction
/health endpoint for monitoring
Structured request/response handling

💬 Streamlit Frontend
Simple chat interface
Real-time communication with backend API

🐳 Dockerized Deployment
Lightweight container using Python slim image
Easy to deploy anywhere

☁️ AWS Deployment
Hosted on EC2 instance
Public API accessible via IP
📂 Project Structure
├── main.py                # FastAPI backend
├── langraph_chatbot.py   # LangGraph agent logic
├── streamlit_app.py      # Frontend UI
├── requirements.txt
├── Dockerfile
└── .env

🔌 API Endpoints
✅ Health Check
GET /health

Response:

{ "status": "ok" }
💬 Chat Endpoint
POST /chat

Request:

{
  "message": "What is Tesla stock price?"
}

Response:

{
  "reply": "Tesla stock is currently..."
}

🐳 Docker Setup
Build Image
docker build -t chatbot-app .

Run Container
docker run -p 8000:8000 chatbot-app

☁️ AWS Deployment
Deployed on EC2 instance
Configured Security Groups to allow port 8000
Application accessible via:
http://<EC2-PUBLIC-IP>:8000

🖥️ Frontend Usage

Run Streamlit app:

streamlit run streamlit_app.py

Make sure to update:

API_URL = "http://<EC2-IP>:8000/chat"
🔐 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here
