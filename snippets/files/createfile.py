import os

def createfile(filename, content):
	"Create a file"
	try:
		with open(filename, "w", encoding="utf-8") as file:
			file.write(content)
		os.system(filename)
	except:
		print("You must use an argument for the filename ('prova.html') and another for the content ('<b>Hello</b> World')")

def create_file_no_open(f,c):
	with open(f, "w", encoding="utf-8") as file:
		file.write(c)

def gettext(filename, content):
	"Create a file"
	try:
		with open(filename, "r", encoding="utf-8") as file:
			file = file.read()
			return text
	except:
		print("File not found")

def readtext(filename, content):
	gettext(filename, content)

def append_to_file(filename, content):
	"""Create a file"""
	try:
		with open(filename, "a", encoding="utf-8") as file:
			file.write(content)
		os.system(filename)
	except:
		print("You must use an argument for the filename ('prova.html') and another for the content ('<b>Hello</b> World')")

if __name__ == "__main__":
	creafile("filediprova.html", "<b>Hello</b>World")
