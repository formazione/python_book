import os
import tkinter as tk
import tkinter.ttk as ttk

print(os.getcwd())

class Window():
	"The main window"

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Resizable Buttons")
		self.b_data = [

		 {"text": "Notepad 1",
		 "command": "example.txt",
		 "image": "notepad.png"},

		  {"text": "Notepad 2",
		 "command": "example2.txt",
		 "image": "notepad.png"},

		]
		self.buttons()

	def buttons(self):
		for b in self.b_data:
			b = Button(self.root, b)


row = 0
col = 0
class Button:

	def __init__(self, root, bdict):
		self.root = root
		self.data = bdict
		self.image = self.data["image"]
		print(self.image)
		self.text = self.data["text"] 
		self.command = self.data["command"] 
		try:
			image = tk.PhotoImage(file = self.image)
		except tk.TclError:
			print(f"Need {self.image}")
		self.configure()
		self.create_button()

	def configure(self):
		tk.Grid.rowconfigure(self.root, row, weight=1)
		tk.Grid.rowconfigure(self.root, col, weight=1)

	def create_button(self):
		self.image = self.data["image"]
		self.button = tk.Button(
			master=self.root,
			text= self.text,
			image=self.data["image"],
			compound= tk.LEFT, # put an image into the button with text
			command=lambda:self.open(self.command))
		self.button.grid(sticky="nswe")
		self.button.row += 1

	def open(self, text):
		try:
			os.startfile(self.text)
		except FileNotFoundError:
			print(f"There in no {self.text}")


app = Window()







