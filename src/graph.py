from langgraph.graph import StateGraph, END
from state import ChatState
from nodes.router import route_user_input
from nodes.search import search_web
from nodes.responder import generate_response
from nodes.router import router_decision

def build_graph():
    builder = StateGraph(ChatState)

    #Nodes
    builder.add_node("router", route_user_input)
    builder.add_node("search", search_web)
    builder.add_node("respond", generate_response)

    #Flow
    builder.set_entry_point("router")

    # Only one outgoing edge based on router’s decision:
    builder.add_conditional_edges("router", router_decision)

    builder.add_edge("search", "respond") # after search we use send information to respond node
    builder.add_edge("respond", END) # final response generated

    return builder.compile()



def run_chat_graph(user_input: str) -> str:

    state = ChatState(user_input = user_input, messages=[])

    graph = build_graph()
    result_dict = graph.invoke(state)
    final_state = ChatState(**result_dict)
    return final_state.final_response or "(No response generated)"