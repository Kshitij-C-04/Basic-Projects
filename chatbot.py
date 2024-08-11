import tkinter as tk
from tkinter import scrolledtext

# Dictionary of responses
responses = {   
    "hello": "Hello! How can I assist you?",
    "hi": "Hi there! How can I help?",
    "how are you": "I'm just a computer program, but I'm doing fine. How about you?",
    "what's your name": "I'm a chatbot. You can call me ChatBot.",
    "who are you": "I'm a simple chatbot designed to assist with basic questions.",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! How can I help?",
    "tell me a joke": "Why did the chicken cross the road? To get to the other side!",
    "tell me a fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "tell me a quote": "Here's a famous quote: 'The only way to do great work is to love what you do.' - Steve Jobs",
    "how old are you": "I don't have an age. I'm just a computer program.",
    "bye": "Goodbye! If you have more questions in the future, feel free to come back.",
    "thank you": "You're welcome! If you need further assistance, don't hesitate to ask.",
    "help": "I'm here to answer your questions. Feel free to ask anything.",
    "default": "I'm not sure I understand. Could you please rephrase your question?"
}

# Function to generate a response from the chatbot
def generate_response(message):
    message = message.lower()
    response = responses.get(message, responses["default"])
    return response

# Function to send a message and get a response from the chatbot
def send_message():
    message = message_entry.get()
    if message:
        chat_area.insert(tk.END, "You: " + message + "\n")
        response = generate_response(message)
        chat_area.insert(tk.END, "Bot: " + response + "\n")
        message_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot with Tkinter")

# Create a text area to display the chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=15)
chat_area.pack()

# Create an entry field for typing messages
message_entry = tk.Entry(root, width=40)
message_entry.pack()

# Create a "Send" button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start the Tkinter main loop
root.mainloop()