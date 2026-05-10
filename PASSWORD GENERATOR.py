# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:02:29 2026

@author: hp
"""

import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x450")
        self.root.config(bg="#f4f4f9")
        self.root.resizable(False, False)

        # Title
        tk.Label(
            root, 
            text="Password Generator", 
            font=("Helvetica", 18, "bold"), 
            bg="#f4f4f9", 
            fg="#333"
        ).pack(pady=15)

        # Output Display
        self.password_var = tk.StringVar()
        self.output_entry = tk.Entry(
            root, 
            textvariable=self.password_var, 
            font=("Consolas", 14), 
            justify="center", 
            state="readonly",
            readonlybackground="#ffffff",
            fg="#000"
        )
        self.output_entry.pack(pady=10, ipadx=10, ipady=8, fill="x", padx=40)

        # Length Slider
        length_frame = tk.Frame(root, bg="#f4f4f9")
        length_frame.pack(pady=10, fill="x", padx=40)
        
        tk.Label(length_frame, text="Password Length:", bg="#f4f4f9", font=("Helvetica", 11)).pack(anchor="w")
        
        self.length_scale = tk.Scale(
            length_frame, 
            from_=4, to_=32, 
            orient=tk.HORIZONTAL, 
            bg="#f4f4f9",
            highlightthickness=0,
            font=("Helvetica", 10)
        )
        self.length_scale.set(12) # Default length
        self.length_scale.pack(fill="x")

        # Complexity Checkboxes
        options_frame = tk.Frame(root, bg="#f4f4f9")
        options_frame.pack(pady=10, fill="x", padx=40)
        
        self.var_upper = tk.BooleanVar(value=True)
        self.var_nums = tk.BooleanVar(value=True)
        self.var_syms = tk.BooleanVar(value=True)

        tk.Checkbutton(options_frame, text="Include Uppercase (A-Z)", variable=self.var_upper, bg="#f4f4f9", font=("Helvetica", 10)).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Include Numbers (0-9)", variable=self.var_nums, bg="#f4f4f9", font=("Helvetica", 10)).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Include Symbols (!@#$)", variable=self.var_syms, bg="#f4f4f9", font=("Helvetica", 10)).pack(anchor="w")

        # Action Buttons
        button_frame = tk.Frame(root, bg="#f4f4f9")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame, 
            text="Generate", 
            command=self.generate_password, 
            bg="#4CAF50", 
            fg="white", 
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            width=10
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            button_frame, 
            text="Copy", 
            command=self.copy_to_clipboard, 
            bg="#2196F3", 
            fg="white", 
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            width=10
        ).pack(side=tk.LEFT, padx=10)

    def generate_password(self):
        """Builds the password based on selected UI options."""
        length = self.length_scale.get()
        character_pool = string.ascii_lowercase
        
        if self.var_upper.get():
            character_pool += string.ascii_uppercase
        if self.var_nums.get():
            character_pool += string.digits
        if self.var_syms.get():
            character_pool += string.punctuation

        if not character_pool:
            messagebox.showwarning("Warning", "Please select at least one character type.")
            return

        password = ''.join(random.choice(character_pool) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        """Copies the generated password to the system clipboard."""
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update() # Required to keep the clipboard content after the window closes
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated yet to copy.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
