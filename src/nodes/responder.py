import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from state import ChatState
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(state: ChatState) -> dict:
    user_input = state.user_input or ""
    search_data = state.search_results or []

    if search_data:
        user_input = "Here is what I found:\n" + "\n".join(search_data)

    messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
    ]
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=250
        )
        content = resp.choices[0].message.content or ""
        user_input = content.strip() or "⚠️ No response from model."
    except Exception as e:
            user_input = f"❌ OpenAI error: {e}"

    #Append to history
    new_messages = state.messages + [f"User: {user_input}", f"Bot: { user_input}"]
    return {
        "final_response": user_input,
        "messages": new_messages
    }
