from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I am CodTechBot, your assistant.",]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Apologies accepted"]
    ],
    [
        r"i need help with (.*)",
        ["Sure, I can help you with %1. Please tell me more.",]
    ],
    [
        r"quit|exit|bye",
        ["Goodbye! Have a great day.", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?"]
    ],
]

def chatbot():
    print("Hi! I'm CodTechBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
