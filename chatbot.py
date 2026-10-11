
# Project: Basic Chatbot
# Internship Task 4
# Concepts: if-elif-else, functions, loops, input/output

def chatbot_response(user_input):
    # Convert input to lowercase for easier matching
    message = user_input.lower().strip()

    # Predefined chatbot responses
    if message == "hello" or message == "hi":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message == "bye":
        return "Goodbye! Have a great day!"

    elif message == "thanks" or message == "thank you":
        return "You're welcome!"

    elif message == "what is your name":
        return "I'm Python Bot, your friendly chatbot!"

    elif message == "what can you do":
        return "I can respond to simple messages. Try saying hello!"

    else:
        return "Sorry, I don't understand that message."


def main():
    print("=" * 40)
    print("       WELCOME TO PYTHON BOT")
    print("=" * 40)
    print("Type 'hello', 'how are you', or 'bye'.")
    print("Type 'bye' to end the conversation.")
    print("-" * 40)

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break

    print("Chat ended. Thank you for using Python Bot!")


if __name__ == "__main__":
    main()
