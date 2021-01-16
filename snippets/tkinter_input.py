from tkinter import simpledialog
import tkinter as tk


def new_filename(title="Enter a new name", sentence="Do not put the extension"):
    tk.Tk().withdraw()
    name = simpledialog.askinteger(title, sentence)
    return name


x = winput()












