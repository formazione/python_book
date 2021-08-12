# crea un compito dalle domande
import os
from random import shuffle
import sys
from tkinter import *


class Ex:
	def __init__(self):
		elenco = [_ for _ in os.listdir()  if _.endswith(".txt")]
		[print(n,i) for n,i in enumerate(elenco)]
		_range = f"0-{len(elenco)-1}"
		scelta = int(input(f"------\n>Scegli compito num.[{_range}]>>>"))
		file_scelto = elenco[scelta]
		print(f"{file_scelto=}")
		with open(file_scelto, "r", encoding="utf-8") as file:
			file = file.read()
		domande = [x for x in file.split("\n\n")]
		self.dnr = []
		for i in domande:
			self.dnr.append(i.split("\n"))
		risposte_esatte = []
		random_list = []
		for n, l in enumerate(self.dnr):
			risposte_esatte.append(l[1])
			a = l[1:]
			shuffle(a)
			self.dnr[n] = [l[0]]
			self.dnr[n].extend(a)

	def print_domande_risposte(self):
		print(self.dnr)
		print(risposte_esatte)

	def print_exercise_shuffled(self):
		for d in self.dnr:
			for i in d:
				print(i)
			print()

	def insert(self, word):
		self.text.insert(END, word + "\n")

	def open(self, lst):
		num = lst.curselection()
		filename = lst.get(num) 
		with open(filename) as file:
			file = file.read()
		return file

	def get_file(self):
		root = Tk()
		lst = Listbox(root)
		lst.pack()
		for i in os.listbox:
			if i.endswith("txt")
			lst.insert(END, i)
		file_content = lst.bind("<SelectListbox>", lambda: self.open(lst))
		root.mainloop()
		return file_content

	def show(self):
		self.root = Tk()
		self.text = Text(self.root)
		self.text.pack()
		for i in self.dnr:
			for q in i:
				self.insert(q)
			self.insert("")
		self.root.mainloop()


app = Ex()
app.show()