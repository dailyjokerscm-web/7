import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.root, state='disabled', width=50, height=20)
        self.text_area.grid(row=0, column=0, columnspan=2)
        self.entry = tk.Entry(self.root, width=40)
        self.entry.grid(row=1, column=0)
        self.send_button = tk.Button(self.root, text='Send', command=self.send_message)
        self.send_button.grid(row=1, column=1)

    def send_message(self):
        user_input = self.entry.get()
        if user_input:
            self.display_message(f'You: {user_input}')
            self.entry.delete(0, tk.END)
            self.ai_response(user_input)

    def display_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f'{self.current_time()} - {message}\n')
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

    def ai_response(self, user_input):
        responses = [
            "Hello! How can I assist you today?",
            "I'm just a simple chat app. Tell me more!",
            "Did you know? Random fact: {random.choice(['Cats sleep 70% of their lives.', 'Honey never spoils.', 'Bananas are berries.'])}",
            "Interesting, tell me more!"
        ]
        response = random.choice(responses)
        self.display_message(f'AI: {response}')

    def current_time(self):
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    root = tk.Tk()
    chat_app = ChatApp(root)
    root.mainloop()