from state import ChatState
import requests
from dotenv import load_dotenv
import os

load_dotenv()
def search_web(state: ChatState) -> dict:
    """demo results Atttempt

    search_results = [
        "Search results 1: Demo result",
        "Search results 2: Another result"
    ]
    """

    tavily_key = os.getenv("TAVILY_API_KEY")
    query = state.user_input or ""

    if not tavily_key:
        return {"search_results": ["Tavily Key missing"]}
    
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            headers={"Content-Type": "application/json"},
            json={
                "api_key": tavily_key,
                "query": query,
                "max_results": 3
            }
        )
        data = response.json()
        results = [r["content"] for r in data.get("results", [])] #for each result in Extract the content field and store it in a new list called results

        return {"search_results": results if results else ["No results found."]}
    except Exception as e:
        return {"search_results": [f"Search failed: {str(e)}"]}
