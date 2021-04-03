import tkinter as tk

on = 1
def hide_frame(evt=""):
	global on, frame, lbx

	if on:
		# hide the frame and changes to + the button text
		button["text"] = "+"
		frame.pack_forget()
		on = 0
	else:
		# hide everything and repack all to put them in order
		button["text"] = "-"
		frame.pack_forget()
		frame1.pack_forget()
		create_frame()
		on = 1


# GLOBAL VARIABLES
root = tk.Tk()
button = tk.Button(root, text="-", command=hide_frame)
button.pack(side="left")


def create_frame():
	"""create frame to be hidden when we press k or -/+"""
	global lbx, lbx1, frame, frame1

	frame = tk.Frame(root)
	frame.pack(side="left")
	lbx = tk.Listbox(frame, bg="gold")
	lbx.pack()
	lbx.insert(0, 1)
	frame1 = tk.Frame(root)
	frame1.pack()
	lbx1 = tk.Listbox(frame1, bg="cyan")
	lbx1.pack(side="left")
	lbx1.insert(0, 2)



create_frame()
root.bind("<k>", hide_frame)
root.mainloop()