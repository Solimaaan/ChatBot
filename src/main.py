from graph import run_chat_graph
from dotenv import load_dotenv
import os


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

def main():
    print("ChatBot is ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Bye :(")
            break

        if not user_input:
            print("please enter a message")
            continue
        

        try:
            response = run_chat_graph(user_input)
            print(f"Bot: {response}\n")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__": #ensures that main() only runs when this file is executed as the main script not imported.
    main()

