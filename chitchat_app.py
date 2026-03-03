import tkinter as tk

class ChitchatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chitchat Application")
        self.create_widgets()

    def create_widgets(self):
        self.chat_area = tk.Text(self.root, state='disabled', width=50, height=20)
        self.chat_area.pack(pady=10)

        self.user_input = tk.Entry(self.root, width=50)
        self.user_input.pack(pady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        message = self.user_input.get()
        if message:
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"You: {message}\n")
            self.chat_area.config(state='disabled')
            self.user_input.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = ChitchatApp(root)
    root.mainloop()