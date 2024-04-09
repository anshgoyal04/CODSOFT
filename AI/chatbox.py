def chatbot_response(user_input):
    # Predefined rules and responses
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm just a chatbot, but thanks for asking!",
        "goodbye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "default": "I'm sorry, I don't understand. Can you please rephrase?",
    }

    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if user input matches any predefined rules
    if user_input in responses:
        return responses[user_input]
    elif "help" in user_input:
        return "Sure, how can I assist you?"
    else:
        return responses["default"]

# Main loop for interacting with the chatbot
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
