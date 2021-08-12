# in darm 2 ho fatto in modo che si possa usare l'apostrofo (codice 18-21)

import glob
from random import choice
from files.createfile import createfile
from files.darm_start import *
from files.darm_end import *
# from dati.browser3 import *
import os

os.chdir("snippets")


class Start:

	def __init__(self):
		"a menu to choose a file in the directory 'dati'"
		self.images()
		self.show_files()
		self.inputfilename() # self.filename contains the txt file with questions you choose
		self.create_list_of_dict(self.filename)
		self.create_test()

	def images(self):
		self.imgslist = [
			"https://picsum.photos/200"
			]

	def create_list_of_dict(self, filename):
		"takes the data from filename and convert them into a dictonary"

		'''
		from

		what is...
		is ...
		is ...
		is ...
		
		to this

		{
		question = "What is....",
		image = "",
		choice = ["is...", "is...", "is..."],
		correct = "",
		explation = ""
		}


		'''

		qdic = {}
		flist = []
		def list_of_questions():
			# read the file and splits every qna in a string
			# file is a list of strings each with a qna
			with open(filename, 'r', encoding='utf-8') as file:
				file = file.read()
				file = file.split("\n\n")
			# every string in the list becomes a list with [q,a,a...]
			return file

		def list_of_list_with_qna(file):
			for eachstring in file:
				flist.append(eachstring.split("\n"))

		def delete_empty_items(): 
			for eachsublist in flist:
				for e in eachsublist:
					if e == '':
						eachsublist.pop(eachsublist.index(e))
				question = eachsublist[0]
				eachsublist.pop(0)
				qdic[question] = eachsublist
		file = list_of_questions()
		list_of_list_with_qna (file)
		delete_empty_items()

		self.qdic = qdic

	def show_files(self):
		text = "File di testo nella cartella: dati"
		text += "------------------------------------"
		for number,eachfile in enumerate(glob.glob("dati/*.txt")):
			print(number, eachfile.replace("dati\\",""))
		text += "------------------------------------"
		print(text)

	def inputfilename(self):
		file_number = int(input("Scegli il numero del file? > "))
		self.filename = glob.glob("dati/*.txt")[file_number]

	def convert_for_template(self, question, answers):
		html = f"""{{
			"question"      :   "{question}",
			"image"         :   "{choice(self.imgslist)}",
			"choices"       :   {answers},
			"correct"       :   "{answers[0]}",
			"explanation"   :   "", }},"""
		return html

	def create_test(self):
		global htmlpage

		for question in self.qdic:
			answers = self.qdic[question]
			htmlpage += self.convert_for_template(question, answers)
		htmlpage += endpage
		filename = f"{input('nome del file: ')}.html"
		createfile(filename, htmlpage)



test = Start()






