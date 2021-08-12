import tkinter as tk


def get_text():
	tx = str(t.selection_get())
	print(tx)
	whole = t.get("1.0", "end")
	print(whole)
	print(whole.index(tx), len(tx) + whole.index(tx) - 1)
	print(t.index("1.0"))


root = tk.Tk()
t = tk.Text()
t.pack()
t.insert("1.0", "Ciao a tutti voi amici miei, come va? Qui tutto bene")
t.bind("<Control-c>", lambda x: get_text())
root.mainloop()

