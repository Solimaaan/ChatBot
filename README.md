A simple chatbot built with LangGraph, OpenAI, Tavily, and Streamlit.
Setup Instructions:

1. Install dependencies:
$ pip install -r requirements.txt
Or manually:
$ pip install streamlit langgraph pydantic requests

3. Set environment variables:
$ export OPENAI_API_KEY=your-openai-key
$ export TAVILY_API_KEY=your-tavily-key

Or manually:
Modify vairable assignments in the .env file.
OPENAI_API_KEY=your-openai-key
TAVILY_API_KEY=your-tavily-key

5. Run the chatbot:
$ streamlit run chatbot.py

Then open http://localhost:8501 in your browser to start chatting.
