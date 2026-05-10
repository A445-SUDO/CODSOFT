# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:53:28 2026

@author: hp
"""

import tkinter as tk
from tkinter import messagebox

class TodoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("450x500")
        self.root.config(bg="#f4f4f9")

        # Title Label
        self.title_label = tk.Label(
            self.root, 
            text="My To-Do List", 
            font=("Helvetica", 20, "bold"), 
            bg="#f4f4f9", 
            fg="#333"
        )
        self.title_label.pack(pady=15)

        # Input Frame for entry and add button
        self.input_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            self.input_frame, 
            font=("Helvetica", 14), 
            width=24, 
            bd=2, 
            relief=tk.GROOVE
        )
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(
            self.input_frame, 
            text="Add", 
            command=self.add_task, 
            bg="#4CAF50", 
            fg="white", 
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.add_button.pack(side=tk.LEFT)

        # Listbox Frame with scrollbar
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=15)

        self.task_listbox = tk.Listbox(
            self.list_frame, 
            font=("Helvetica", 13), 
            width=35, 
            height=12, 
            selectbackground="#cce5ff",
            selectforeground="black",
            activestyle="none",
            bd=0,
            highlightthickness=1,
            highlightcolor="#ccc"
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Action Buttons Frame
        self.action_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.action_frame.pack(pady=10)

        self.complete_button = tk.Button(
            self.action_frame, 
            text="Mark Completed", 
            command=self.mark_completed, 
            bg="#2196F3", 
            fg="white", 
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(
            self.action_frame, 
            text="Delete Task", 
            command=self.delete_task, 
            bg="#f44336", 
            fg="white", 
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.delete_button.pack(side=tk.RIGHT, padx=10)

        # Bind the Enter key to the add_task function
        self.root.bind('<Return>', lambda event: self.add_task())

    def add_task(self):
        """Retrieves text from entry widget and adds it to the listbox."""
        task = self.task_entry.get()
        if task.strip():
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task description.")

    def delete_task(self):
        """Deletes the currently selected task."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        """Visually updates a selected task to show it is finished."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_task_index)
            
            # Prevent double-marking if already completed
            if not task_text.startswith("✅ "):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f"✅ {task_text}")
                # Gray out the text to visually indicate completion
                self.task_listbox.itemconfig(selected_task_index, fg="gray")
                # Clear the selection highlight
                self.task_listbox.selection_clear(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def main():
    root = tk.Tk()
    app = TodoGUI(root)
    # This keeps the application window open and running
    root.mainloop()

if __name__ == "__main__":
    main()
