import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.configure(bg="#003C43")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#003C43")
        self.frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.label = tk.Label(self.frame, text="Enter password length:", bg="#003C43", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'))
        self.label.pack(pady=10, fill=tk.X)
        
        self.length_entry = tk.Entry(self.frame, font=('Times New Roman', 18, 'bold'), bd=0, bg="#77B0AA", fg="#003C43")
        self.length_entry.pack(pady=10, fill=tk.X, ipady=5)
        
        self.generate_btn = tk.Button(self.frame, text="Generate Password", command=self.generate_password, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.generate_btn.pack(pady=10, fill=tk.X)
        
        self.password_label = tk.Label(self.frame, text="", bg="#77B0AA", fg="#003C43", font=('Times New Roman', 18, 'bold'))
        self.password_label.pack(pady=10, fill=tk.X)
    
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            password = self.create_password(length)
            self.password_label.config(text=password)
        except ValueError as e:
            messagebox.showwarning("Warning", f"Invalid input: {e}")
    
    def create_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
