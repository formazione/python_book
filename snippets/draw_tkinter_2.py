import tkinter as tk
from PIL import ImageGrab
import os



lastx, lasty = 0, 0


def xy(event):
    """Takes the coordinates of the mouse when you click the mouse"""
    global lastx, lasty
    lastx, lasty = event.x, event.y


def addLine(event):
    """Creates a line when you drag the mouse
    from the point where you clicked the mouse to where the mouse is now"""
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    # this makes the new starting point of the drawing
    lastx, lasty = event.x, event.y

def save(event, test=0):
    """ Save the image in the canvas """
    x = root.winfo_rootx()+canvas.winfo_x() # x pos of canvas
    y = root.winfo_rooty()+canvas.winfo_y() # y pos of canvas
    x1 = x + canvas.winfo_width() # width of canvas
    y1 = y + canvas.winfo_height() # height of canvas
    im = ImageGrab.grab((x, y, x1, y1))
    if test:
        print(f"{root.winfo_width()=}")
        print(f"{root.winfo_height()=}")
        print(f"{root.winfo_y()=}")
        print(f"{root.winfo_x()=}")
        print(f"{root.winfo_rooty()=}")
        print(f"{root.winfo_rootx()=}")
        print(f"{root.winfo_width()=}")
        print(x, y, x1, y1)

    if test == 0:
        im.save("captured.png")
        os.system("captured.png")

root = tk.Tk()
root.geometry("800x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = tk.Canvas(root)
canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
root.bind("<Control-s>", lambda evt: save(evt, test=0))

root.mainloop()
