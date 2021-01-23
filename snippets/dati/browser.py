import os
import tkinter as tk

# window, title and size
root = tk.Tk()
root.title("Browser")
root.geometry("400x400")


listbox = tk.Listbox(root, bg='gray', fg="white")
listbox.pack(expand=tk.YES, fill=tk.BOTH)

for file in os.listdir():
	listbox.insert(0,file)

root.mainloop()
