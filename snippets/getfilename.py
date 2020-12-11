from tkinter import filedialog

# root = tk.Tk()
def getfilename(_type=""):
	"Returns the path and name of file selected"
	# Ex. arg: _type=".txt" if you need only txt files
	filename = filedialog.askopenfilename(
		initialdir = ".",
		title = "Select file",
		filetypes = (
			("pdf files", _type),
			("all files", "*.*")))
	return filename

print(getfilename(""))
