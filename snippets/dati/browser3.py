import os
import tkinter as tk


class Browser:
	def __init__(self):
		self.create_root_window()
		self.listbox()
		self.root.mainloop()

	def create_root_window(self):
		self.root = tk.Tk()
		self.root.title("Browser")
		self.root.geometry("400x400")

	def listbox(self):
		self.listbox = tk.Listbox(self.root, bg='yellow', fg='blue')
		self.listbox.pack(expand=tk.YES, fill=tk.BOTH)
		self.listbox.bind("<<ListboxSelect>>", self.openfile)
		self.get_files_in()

	def get_files_in(self):
		for file in os.listdir():
			if file.endswith(".py"):
				self.listbox.insert(0, file)

	def openfile(self, evt):
		filename = self.listbox.get(self.listbox.curselection())
		print(f"Selected {filename} - Now I will start this")
		os.startfile(filename)


app = Browser()