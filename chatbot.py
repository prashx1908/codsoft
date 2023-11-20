# Define a dictionary of rules for the chatbot
rules = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm always fine if there are no malwares in me !!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that."
}

# Function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()
    response = rules.get(user_input, rules["default"])
    return response

# Main chat loop
print("Chatbot: Hello! I'm a simple chatbot. You can say 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
