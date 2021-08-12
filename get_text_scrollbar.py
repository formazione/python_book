import tkinter as tk
import tkinter.ttk as ttk

def get_text():
	tx = str(t.selection_get())
	print(tx)
	whole = t.get("1.0", "end")
	# print(whole)
	print(whole.index(tx), len(tx) + whole.index(tx) - 1)
	# print(t.index("1.0", tx))


root = tk.Tk()

t = tk.Text(root, width = 40, height = 5, wrap = "none")
t.tag_configure('red', foreground='red')
t.tag_configure('blue', foreground='blue')
t.tag_configure('green', foreground='gold', background='black')
ys = ttk.Scrollbar(root, orient = 'vertical', command = t.yview)
xs = ttk.Scrollbar(root, orient = 'horizontal', command = t.xview)
t['yscrollcommand'] = ys.set
t['xscrollcommand'] = xs.set

t.insert('2.0', "Lorem ipsum...", ('blue'))
t.insert('3.0', "Lorem ipsum...", ('green'))
t.grid(column = 0, row = 0, sticky = 'nwes')
xs.grid(column = 0, row = 1, sticky = 'we')
ys.grid(column = 1, row = 0, sticky = 'ns')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
# t = tk.Text()
# t.pack()
def popupImportantMenu(event):
	print("Hello")
t.tag_bind('green', '<1>', popupImportantMenu)
t.bind("<Control-c>", lambda x: get_text())
for n in range(5):
	t.tag_add("red", f"{n}.0 + 1 chars")
# canvas = tk.Canvas()
# canvas.itemconfigure('important', fill='red')
# canvas.create_rectangle(10, 10, 40, 40, tags=('important'))
t.insert('1.0', 'START\n ', ('red'))
t.insert('end', '\n Fine del testo', ('blue'))
root.mainloop()

