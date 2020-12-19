# tkinter advanced: pysnippets


'''sdasd

Started: 03.12.2020 - v. 0.1

- chapter
	- chapter1.txt
	- chapter1img1.png

This is how the GUI appears

            --- GUI ---

   |---------------------------------|
   |PyEbookGen                       |
   |---------------------------------|
   | chapter1  |                     |
   |           |    some text        |
   |           |                     |
   |           |                     |
   |---------------------------------|

'''
# module for the gui
import tkinter as tk
# module to check files
import os


class Win:
	def __init__(self, title, version, extension):
		self.extension = extension
		self.root = tk.Tk()
		self.root.title(f"{title}.{version}")
		self.window()

	def window(self):
		"Contains all the widgets"
		def frame():
			"Contains the list of chapter names in listbox"
			self._frame = tk.Frame(self.root, bg="gold")
			self._frame.grid(column=0, row=0,
				sticky="nswe") # adapt the fram to the window

		def listbox():
			"The book chapter name list goes here"
			self._lbx = tk.Listbox(self._frame, bg="yellow")
			self._lbx.grid(column=0, row=0,
				sticky="nswe") # adapt the listbox to the frame
			
			def insert():
				for file in os.listdir("snippets"):
					if file.endswith(self.extension):
						self._lbx.insert(0, file)
			
			def showcontent(evt):
				filenum = self._lbx.curselection()
				self.filename = self._lbx.get(filenum)
				with open(f"snippets/{self.filename}") as file:
					content = file.read()
				self._text.delete("0.0", tk.END)
				self._text.insert(tk.END, content)

			self._lbx.bind("<<ListboxSelect>>", showcontent)
			insert()

		def frame2():
			"Contains the text"
			self._frame2 = tk.Frame(self.root, bg="gold")
			self._frame2.grid(column=1, row=0)


		def save(evt):
			with open(f"snippets/{self.filename}", "w") as file:
				file.write(self._text.get("0.0", tk.END))
		
		def text():
			"Contains the text of selected chapter in listbox"
			self._text = tk.Text(self._frame2)
			self._text.grid(column=1, row=0)
			self._text.bind("<Control-s>", save)

		
		def widgets_order():
			"The widgets on the screen"
			frame()
			frame2()
			listbox()
			text()


		widgets_order()


def create_chapters_folder():
	"Create the folder for the chapters if not exists"
	if "chapters" not in os.listdir():
		os.mkdir("chapters")
		print("Created a folder named chatpters")

def console_intro():
	print("""
Save your chapters in chapters folder
""")

# ================ main ============
if __name__ == "__main__":
	console_intro()
	create_chapters_folder()
	ver = "0.1"
	win = Win("PySnippets", "0.01", extension=".py")
	win.root.mainloop()






