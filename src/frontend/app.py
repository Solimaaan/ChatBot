# src/frontend/app.py
import sys
import os

# Ensure the parent src directory is on the module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from graph import run_chat_graph

st.set_page_config(page_title="ChatBot UI", page_icon="🤖", layout="centered")
st.title("🧠 ChatBot – LangGraph x Tavily x OpenAI")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history
for user_msg, bot_msg in (st.session_state.history):
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Bot:** {bot_msg}")

#Input and Send button
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_text")
    submitted = st.form_submit_button("Send")

if submitted:
    if user_input.strip():
        # Show a spinner while awaiting the response
        with st.spinner("🤖 Thinking..."):
            bot_response = run_chat_graph(user_input)

        # Append to history after obtaining response
        st.session_state.history.append((user_input, bot_response))
    else:
        st.warning("❌ Cannot send empty input.")
