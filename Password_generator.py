import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("300x200")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master, width=20)
        self.length_entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, width=20)
        self.password_entry.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            return

        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()