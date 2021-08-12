import tkinter as tk

'''
placeholder [      ]    Text     
start value [      ]   
end [    ]
step[    ]

List of placeholders
....
....
....
[] New placeholder
[] Replace all
[] Create html quiz
'''


def window():
	''' The window and the call to function '''
	root = tk.Tk()
	mk_frame1(root)
	mk_frame2(root)
	root.mainloop()
	

def mk_frame1(root):
	frame1 = mk_frame(root)
	
	label1 = mk_label(frame1, "Placeholder to substitute")
	entry1 = mk_entry(frame1)
	
	label2 = mk_label(frame1, "Starting value")
	entry2 = mk_entry(frame1)
	
	label3 = mk_label(frame1, "Ending value")
	entry3 = mk_entry(frame1)
	
	label4 = mk_label(frame1, "Step")
	entry4 = mk_entry(frame1)

	button1 = mk_button(frame1, "Enter")
	button2 = mk_button(frame1, "Show the Exercise")

	label4 = mk_label(frame1, "Operations for result")
	entry5 = mk_entry(frame1)

def mk_frame2(root):
	frame2 = mk_frame(root)
	text = mk_text(frame2)


def mk_entry(root):
	entry = tk.Entry(master=root,
		bg="gold")
	entry.pack()
	return entry


def mk_label(root, text=""):
	label = tk.Label(master=root,
		text=text,
		bg="cyan")
	label.pack()
	return label

def mk_button(root, text=""):
	button = tk.Button(master=root,
		text=text,
		bg="gold")
	button.pack()
	return button

def mk_frame(root, side="left"):
	frame = tk.Frame(master=root,
		bg="cyan")
	frame.pack(side=side, fill="both")
	return frame


def mk_text(root):
	''' '''
	text = tk.Text(master=root,
		bg="gold")
	text.pack()
	text.insert(tk.END,
		"""How is [n1] + [n2]?
The result is [result]
""")
	return text

window()