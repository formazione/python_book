''' get_filename
This function opens a filedialog.askopenfilename
window and returns the name of the filepicked.
With the messagebox.showinfo, it shows you the name you
picked if you run this script as the main file (you launch it
and do not call it from outside)
'''

from tkinter import filedialog
from tkinter import messagebox 


def get_filename(_type=""):
	"Returns the path and name of file selected"
	#_type=".txt" to get txt file name
	
	filename = filedialog.askopenfilename(
		initialdir = ".",           # same dir of this script
		title = "Select file",
		filetypes = (
			("pdf files", _type),
			("all files", "*.*")))
	return filename


if __name__ == "__main__":
	import sys
	filename = get_filename("")
	name = messagebox.showinfo(
		title="Name of the file you picked" , message=filename)


























