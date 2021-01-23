import os
import tkinter as tk

root = tk.Tk()
root.title("Browser")
root.geometry("400x400")

def openfile(evt):
	pass

listbox = tk.Listbox(root, bg='yellow', fg='blue')
listbox.pack(expand=tk.YES, fill=tk.BOTH)
listbox.bind("<<ListBoxSelect>>", openfile)

for file in os.listdir():
	listbox.insert(0,file)

root.mainloop()