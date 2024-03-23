import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great, thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries.", "No problem.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon.", "Goodbye, have a great day!",]
    ],
]

# Create a ChatBot with the pairs
chatbot = Chat(pairs, reflections)

def chat():
    print("Welcome! Ask me anything or just say hi.")
    print("Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    chat()
