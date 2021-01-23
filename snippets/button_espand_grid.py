import os
import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("Lanch my Programs")


class Button:
    """button1 = Button("Testo", "4ce", 0, 0)"""
    row = 0
    def __init__(self, dic):
        self.dic = dic
        try:
            image = tk.PhotoImage(file=self.dic["icon"])
        except tk.TclError:
            print(f"you need the {dic['icon']} image in the folder")
            image = ""
        tk.Grid.rowconfigure(root, Button.row, weight=1)
        tk.Grid.columnconfigure(root, 0, weight=1)
        self.button = tk.Button(
            root,
            text=self.dic["text"],
            image=image,
            compound = tk.LEFT,
            command=lambda : self.open(self.dic["command"]))
        self.button.grid(sticky="nswe")
        self.button.image = image
        Button.row += 1

    def open(self, text):
        try:
            os.startfile(text)
        except FileNotFoundError:
            print(f"there is no file {self.dic['text']} here")


button_data = [
    {"text" : "Notepad 1",
     "command" : "example.txt",
     "icon" : "notepad.PNG"}

     ,
    
    {"text" : "Notepad n. 2",
    "command" : "example2.txt",
    "icon" : "notepad.PNG"}
]

for d in button_data:
    b = Button(d)

root.mainloop()

