def run_chatbot():
    responses = {
        "hello": "Hey! How can I help you today?",
        "hi": "Hi there! What's up?",
        "how are you": "I'm a bot, but I'm running perfectly!",
        "what is ai": "AI is the simulation of human intelligence by machines.",
        "bye": "Goodbye! Have a great day.",
        "help": "I can answer questions about AI, greet you, or just chat!",
        "who made you": "I was built as part of DecodeLabs Project 1.",
        "what can you do": "I can respond to predefined inputs using rule-based logic."
    }

    print("Chatbot: Hello! I'm online. Type 'bye' or 'exit' to quit.\n")

    while True:
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()

        if clean_input in ("exit", "quit"):
            print("Chatbot: Session terminated. Goodbye!")
            break

        reply = responses.get(clean_input, "I don't understand that yet. Try asking something else!")
        print(f"Chatbot: {reply}\n")

if __name__ == "__main__":
    run_chatbot()
