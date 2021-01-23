import tkinter as tk
from tkinter import messagebox
import os

popup = messagebox.showinfo


def message():
    "Message shown by the menu item 'About' "
    popup("Hello", "Visit my site")

def visit():
    "Message shown by the menu item 'About' "
    os.startfile("https://pythonprogramming.altervista.org")

root = tk.Tk()
root.title("Window and menubar")
root.geometry("400x400+100+100")

# create the menu
menubar = tk.Menu()
root.config(menu=menubar)
# adding a voice to the menu with add_command
menubar.add_command(label="About", command=message)
menubar.add_command(label="Visit", command=visit)


root.mainloop()



































