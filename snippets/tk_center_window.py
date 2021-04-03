import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Centered window')

window_height = 530
window_width = 800

def center_screen():
	""" gets the coordinates of the center of the screen """
	global screen_height, screen_width, x_cordinate, y_cordinate

	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
	x_cordinate = int((screen_width/2) - (window_width/2))
	y_cordinate = int((screen_height/2) - (window_height/2))
	root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

center_screen()

root.mainloop()