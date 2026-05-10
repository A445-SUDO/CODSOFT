# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:59:19 2026

@author: hp
"""

import tkinter as tk
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Calculator")
        self.root.geometry("350x500")
        self.root.config(bg="#f3f3f3")
        self.root.resizable(False, False)

        # Variables
        self.current_expression = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        # --- Display Screen ---
        display_frame = tk.Frame(self.root, bg="#f3f3f3")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.display = tk.Entry(
            display_frame, 
            textvariable=self.display_var, 
            font=("Segoe UI", 28), 
            bg="#f3f3f3", 
            fg="#000", 
            bd=0, 
            justify="right",
            state="readonly", # Prevent manual typing to force button use/bindings
            readonlybackground="#f3f3f3"
        )
        self.display.pack(expand=True, fill="both")

        # --- Button Grid ---
        buttons_frame = tk.Frame(self.root, bg="#f3f3f3")
        buttons_frame.pack(expand=True, fill="both")

        # Button layout defining the label and the action
        button_layout = [
            ('%', self.add_to_expression), ('CE', self.clear_entry), ('C', self.clear_all), ('⌫', self.backspace),
            ('1/x', self.reciprocal), ('x²', self.square), ('√', self.square_root), ('/', self.add_operation),
            ('7', self.add_to_expression), ('8', self.add_to_expression), ('9', self.add_to_expression), ('*', self.add_operation),
            ('4', self.add_to_expression), ('5', self.add_to_expression), ('6', self.add_to_expression), ('-', self.add_operation),
            ('1', self.add_to_expression), ('2', self.add_to_expression), ('3', self.add_to_expression), ('+', self.add_operation),
            ('+/-', self.negate), ('0', self.add_to_expression), ('.', self.add_to_expression), ('=', self.evaluate)
        ]

        row_val = 0
        col_val = 0

        # Create buttons dynamically
        for (text, command) in button_layout:
            # Styling based on button type
            bg_color = "#ffffff" # Default white for numbers
            if text in ['/', '*', '-', '+', '=']:
                bg_color = "#f9f9f9" # Light gray for operations
                if text == '=':
                    bg_color = "#8ab4f8" # Blue for equals
            elif text in ['%', 'CE', 'C', '⌫', '1/x', 'x²', '√']:
                bg_color = "#f9f9f9"

            btn = tk.Button(
                buttons_frame, text=text, font=("Segoe UI", 14), bg=bg_color, fg="#000",
                bd=1, relief="ridge", command=lambda t=text, c=command: c(t) if c == self.add_to_expression or c == self.add_operation else c()
            )
            btn.grid(row=row_val, column=col_val, sticky="nsew", ipadx=10, ipady=15)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid to expand evenly
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)

        # Keyboard bindings
        self.root.bind("<Return>", lambda event: self.evaluate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        for key in "0123456789.+-*/":
            self.root.bind(key, lambda event, char=key: self.add_to_expression(char) if char not in "+-*/" else self.add_operation(char))

    # --- Calculator Logic ---

    def update_display(self, value):
        self.display_var.set(value)

    def add_to_expression(self, value):
        if self.display_var.get() == "0" or self.display_var.get() == "Error":
            self.current_expression = str(value)
        else:
            self.current_expression += str(value)
        self.update_display(self.current_expression)

    def add_operation(self, operator):
        if self.current_expression and self.current_expression[-1] not in "+-*/.":
            self.current_expression += operator
            self.update_display(self.current_expression)

    def clear_all(self):
        self.current_expression = ""
        self.update_display("0")

    def clear_entry(self):
        # A simple implementation: clears the current line
        self.clear_all()

    def backspace(self):
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            self.update_display(self.current_expression if self.current_expression else "0")

    def negate(self):
        try:
            if self.current_expression:
                # If it's a simple number, just flip it
                val = float(self.current_expression)
                self.current_expression = str(-val)
                # Clean up formatting for integers
                if self.current_expression.endswith(".0"):
                    self.current_expression = self.current_expression[:-2]
                self.update_display(self.current_expression)
        except ValueError:
            pass # Ignore if it's a complex expression

    def square(self):
        try:
            val = float(eval(self.current_expression))
            self.current_expression = str(val ** 2)
            self.format_result()
        except Exception:
            self.update_display("Error")
            self.current_expression = ""

    def square_root(self):
        try:
            val = float(eval(self.current_expression))
            if val < 0:
                self.update_display("Error")
                self.current_expression = ""
            else:
                self.current_expression = str(math.sqrt(val))
                self.format_result()
        except Exception:
            self.update_display("Error")
            self.current_expression = ""

    def reciprocal(self):
        try:
            val = float(eval(self.current_expression))
            if val == 0:
                self.update_display("Error")
                self.current_expression = ""
            else:
                self.current_expression = str(1 / val)
                self.format_result()
        except Exception:
            self.update_display("Error")
            self.current_expression = ""

    def evaluate(self):
        try:
            if self.current_expression:
                # Evaluate the math string
                result = eval(self.current_expression)
                self.current_expression = str(result)
                self.format_result()
        except ZeroDivisionError:
            self.update_display("Cannot divide by zero")
            self.current_expression = ""
        except Exception:
            self.update_display("Error")
            self.current_expression = ""

    def format_result(self):
        """Removes trailing .0 from integers for a cleaner display."""
        if self.current_expression.endswith(".0"):
            self.current_expression = self.current_expression[:-2]
        self.update_display(self.current_expression)

def main():
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
