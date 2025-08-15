import tkinter as tk
from tkinter import scrolledtext

# Function to get bot response
def get_bot_response(user_input):
    user_input = user_input.lower()

    # if user_input in  == "hello","hi","hey":
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you?"
    elif user_input == "how are you":
        return "I'm doing great! How about you?"
    elif user_input == "i am fine,thanks":
        return "🤗"
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    elif user_input == "what is your name":
        return "I am your friendly chatbot."
    elif user_input == "tell me a joke":
        return "Why did the scarecrow win an award?...Because he was outstanding in his field😂"
    elif user_input == "thank you":
        return "You're welcome!"
    elif user_input == "help":
        return "You can ask me simple questions like 'hello', 'how are you', 'tell me a joke', etc."
    else:
        return "Sorry, I don't understand that."

# Function to send message
def send_message(event=None):  # event=None allows binding Enter key
    user_message = user_entry.get()
    if user_message.strip() != "":
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {user_message}\n")
        bot_reply = get_bot_response(user_message)
        chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)
        user_entry.delete(0, tk.END)

# Function to clear chat
def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0, tk.END)
    chat_area.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Rule-Based Chatbot")
root.configure(bg="#2E2E2E")  # Grayish black background

# Welcome message label
welcome_label = tk.Label(root, text="Hello, ask anything!", font=("Arial", 14), bg="#2E2E2E", fg="white")
welcome_label.pack(pady=5)

# Frame for user input and buttons (at top)
input_frame = tk.Frame(root, bg="#2E2E2E")
input_frame.pack(pady=5)

user_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=5)
user_entry.bind("<Return>", send_message)  # Bind Enter key

send_button = tk.Button(input_frame, text="Send", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(input_frame, text="Clear Chat", command=clear_chat, font=("Arial", 12), bg="#f44336", fg="white")
clear_button.pack(side=tk.LEFT)

# Chat display area (below input field)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, font=("Arial", 12), bg="#1E1E1E", fg="white")
chat_area.pack(pady=5)
chat_area.config(state=tk.DISABLED)

root.mainloop()
