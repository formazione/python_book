from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog
import tkinter as tk

def splitpdf():
               "a windows open to select pdf to split into single pages"
	try:
		filename = filedialog.askopenfilename(initialdir=".",
		filetypes = [("PDF", ".pdf")]
		)

		inputpdf = PdfFileReader(open(filename, "rb"))

		for i in range(inputpdf.numPages):
		    output = PdfFileWriter()
		    output.addPage(inputpdf.getPage(i))
		    with open("document-page%s.pdf" % i, "wb") as outputStream:
		        output.write(outputStream)
	except:
		print("No file selected")

splitpdf()
