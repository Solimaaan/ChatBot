from state import ChatState

def route_user_input(state: ChatState) -> dict:
    return {} # We use this to satisfy langraph where each node has to output a dict


def router_decision(state: ChatState) -> str:
    query = (state.user_input or "").lower()
    triggers = ["search", "find", "look", "when", "where"] # triggering words that routes the model to search using Tavily
    return "search" if any(t in query for t in triggers) else "respond"