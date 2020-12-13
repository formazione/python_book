# tkinter advanced: pybookgen

'''
Started: 03.12.2020 - v. 0.1

- chapter
	- chapter1.txt
	- chapter1img1.png

GUI
---------------------------------
PyEbookGen
---------------------------------
 chapter1  | text
           |

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
		self.controls()

	def controls(self):
		self.root.bind("<Control-n>", self.newfile)
		self._lbx.bind("<<ListboxSelect>>", self.showcontent)

	def newfile(self, evt):
		newfilename = input("Name : ") + ".py"
		with open(f"snippets/{newfilename}", "w") as file:
			pass
		self._lbx.insert(0, newfilename)

	def newfile2(self):
		newfilename = input("Name : ") + ".py"
		with open(f"snippets/{newfilename}", "w") as file:
			pass
		self._lbx.insert(0, newfilename)

	def insert(self):
		for file in os.listdir("snippets"):
			if file.endswith(self.extension):
				self._lbx.insert(0, file)
	
	def window(self):
		"Contains all the widgets"
		
		def frame0():
			"Contains the text"
			self._frame0 = tk.Frame(self.root, bg="gold")
			self._frame0.grid(column=0, columnspan=2, row=0)
		
		def frame():
			"Contains the list of chapter names in listbox"
			self._frame = tk.Frame(self.root, bg="gray")
			self._frame.grid(column=0, row=1,
				sticky="NESW")
			self._frame.grid_columnconfigure(0, weight=0)
		
		def frame2():
			"Contains the text"
			self._frame2 = tk.Frame(self.root, bg="gold")
			self._frame2.grid(column=1, row=1)
		
		def label_banner():
			img = tk.PhotoImage(file="snippets/banner.png")
			self.lb_banner = tk.Label(self._frame0, image=img, bg="yellow")
			self.lb_banner.image = img
			self.lb_banner.grid(column=0, columnspan=2, row=0)



		def listbox():
			"The book chapter name list goes here"
			self._lbx = tk.Listbox(self._frame, bg="yellow")
			self._lbx.grid(
				column=0,
				row=0,
				sticky="NESW"
				) # adapt the listbox to the frame
			
			self.insert()
			
		def button_new():
			"The book chapter name list goes here"
			self.but1 = tk.Button(self._frame, text="New", bg="yellow", command=self.newfile2)
			self.but1.grid(
				column=0,
				row=1,
				sticky="NESW"
				) # adapt the listbox to the frame

		def button_save():
			"The book chapter name list goes here"
			self.but2 = tk.Button(self._frame, text="Save", bg="yellow", command=save)
			self.but2.grid(
				column=0,
				row=2,
				sticky="NESW"
				) # adapt the listbox to the frame



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
			frame0()
			frame()
			frame2()
			label_banner()
			listbox()
			button_new()
			button_save()
			text()

		widgets_order()

	def showcontent(self, evt):
		filenum = self._lbx.curselection()
		self.filename = self._lbx.get(filenum)
		with open(f"snippets/{self.filename}") as file:
			content = file.read()
		self._text.delete("0.0", tk.END)
		self._text.insert(tk.END, content)


def create_chapters_folder():
	"Create the folder for the snippets if not exists"
	if "snippets" not in os.listdir():
		os.mkdir("snippets")
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