import tkinter as tk
import time
from tkinter import messagebox

root = tk.Tk()
root.title("Window and menubar")
root.geometry("400x400+100+100")

def message():
    messagebox.showinfo("MESSAGE",
        "This is pythonprogramming.altervista.org",
        parent=root)

menubar = tk.Menu(root)
menubar.add_command(label="Click me",
    command=message)
root.config(menu=menubar)
root.mainloop()








