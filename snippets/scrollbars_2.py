#listbox scrollbar
from random import randint
import tkinter as tk


def scrolllistbox(event, lb):
	global switch
	if switch==1:
		lb.yview_scroll(int(-4*(event.delta/120)), "units")
		print(event)

def do_switch():
	global switch
	if switch:
		switch = 0
		label['text'] = "Not in sync"
	else:
		switch = 1
		label['text'] = "In sync"

def create_data(listbox1):
	for i in range(100):
	    rnd = str(randint(1,100))
	    listbox1.insert(tk.END, f"INCOMES day {i}:" + rnd)


def def_listbox():
	scrollbar1 = tk.Scrollbar(frame1)
	scrollbar1.pack(side=tk.LEFT, fill=tk.Y)
	listbox1 = tk.Listbox(frame1)
	scrollbar1.config(command=listbox1.yview)
	create_data(listbox1)
	listbox1.pack(expand=1, fill="both", side="left")
	listbox1.config(bg = "yellow", yscrollcommand=scrollbar1.set)
	return listbox1


def create_root():
	"Returns the main windows"
	root = tk.Tk()
	root.title("2 Listbox scolling in sync")
	root.geometry("400x400")
	return root


def create_frames():
	"Creates frames for widgets"

	# listboxes frame
	frame1 = tk.Frame(root)
	frame1.pack(expand=1, fill="both")
	# button and label frame
	frame2 = tk.Frame(root)
	frame2.pack()
	return frame1, frame2


def create_widgets():
	"Returns listboxes, button and label"
	# listboxes
	listbox1 = def_listbox()
	listbox2 = def_listbox()
	listbox1.bind("<MouseWheel>", lambda event: scrolllistbox(event, listbox2))
	listbox2.bind("<MouseWheel>", lambda event: scrolllistbox(event, listbox1))
	# ================== SWITCH BUTTON =========================
	button = tk.Button(frame2, text= "Sync/unsync", command=do_switch)
	button.pack()
	label = tk.Label(frame2, text = "In sync")
	label.pack()
	# ==========================================================
	pack = listbox1, listbox2, button, label
	return pack


switch = 1
root = create_root()
frame1, frame2 = create_frames()
listbox1, listbox2, button, label = create_widgets()
root.mainloop()