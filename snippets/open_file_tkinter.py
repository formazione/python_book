try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog


root = tk.Tk()

style = ttk.Style(root)
style.theme_use("clam")


def c_open_file_old():
    rep = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='/',
    	initialfile='tmp',
    	filetypes=[
    		("PNG", "*.png"),
    		("JPEG", "*.jpg"),
    		("All files", "*")])
    print(rep)
    try:
	    os.startfile(rep[0])
    except IndexError:
        print("No file selected")

ttk.Button(root, text="Open files", command=c_open_file_old).grid(row=1, column=0, padx=4, pady=4, sticky='ew')

root.mainloop()