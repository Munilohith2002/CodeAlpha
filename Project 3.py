
# Online Python - IDE, Editor, Compiler, Interpreter
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey|greetings', ['Hello!', 'Hi there!', 'Hey!', 'Greetings!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am good, thanks for asking.', 'I am fine, how about you?']),
    (r'(.*) your name?', ['My name is Chatbot.', 'I am called Chatbot.', 'You can call me Chatbot.']),
    (r'(.*) help (.*)', ['I can assist you with various topics. Feel free to ask me anything.']),
    (r'(.*) (age|old) are you?', ['I am just a computer program, so I don\'t have an age.']),
    (r'(.*) (love|like) (.*)', ['I am just a chatbot, so I don\'t have feelings.']),
    (r'(.*) (created|made) you?', ['I was created by an AI programmer.', 'I am a product of programming.']),
    (r'quit|bye|exit', ['Goodbye!', 'See you later!', 'Take care!'])
]

# Create and train the chatbot
chatbot = Chat(patterns, reflections)

# Start chatting with the user
print("Welcome to the Chatbot! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'quit':
        break