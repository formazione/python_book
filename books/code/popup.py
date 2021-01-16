import tkinter as tk

def popup(self,
    title="",
    sentence=""):
    "Simple wrapper function for messagebox.showinfo"

    tk.Tk().withdraw()
    name = messagebox.showinfo(
            title=title,
            message=sentence)