import tkinter as tk
from tkinter import simpledialog

def input_text(
    title="Title",
    prompt="Question",
    feedback="ok"):

    tk.Tk().withdraw()
    name = simpledialog.askstring(title, prompt)
    print(feedback.format(name))

if __name__ == "__main__":
    input_text(
        "Question",
        "What is your name?",
        feedback="So your name is {}!")
