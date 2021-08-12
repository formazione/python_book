import os
import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("Lanch my Programs")


class Button:
    """button1 = Button("Testo", "4ce", 0, 0)"""
    row = 0
    def __init__(self, text, func, image=""):
        image = tk.PhotoImage(file=image)
        tk.Grid.rowconfigure(root, Button.row, weight=1)
        tk.Grid.columnconfigure(root, 0, weight=1)

        self.button = tk.Button(
            root,
            text=text,
            image=image,
            compound = tk.LEFT,
            command=func)
        # self.button.pack()
        self.button.grid(sticky="nswe")
        self.button.image = image
        Button.row += 1

    def open(text):
        os.startfile(text)


data = [
    ["Notepad n.1", lambda: Button.open("example.txt"), "notepad.PNG"],
    ["Notepad n. 2", lambda: Button.open("example2.txt"), "notepad.PNG"],
]

for d in data:
    b = Button(*d)

root.mainloop()

