def winput(title, sentence):
    import tkinter as tk
    from tkinter import simpledialog
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y


x = winput("Hello", "How is 5 + 5?")
print(x)
