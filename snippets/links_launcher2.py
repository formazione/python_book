import os
import tkinter as tk
from tkinter import simpledialog


# os.startfile("https://leggi.amazon.it/?asin=B07T3FVKNF")

# Dizionario degli articoli
art_dic = {
"python" : "https://pythonprogramming.altervista.org",
"google" : "www.google.com",
"python_org" : "https://python.org",
}

def art(link):
    os.startfile(art_dic[link])


def run(self):
	art(self.get(self.curselection()))


root = tk.Tk()
root.title("Links launcher")
root.geometry("250x400")
lbx = tk.Listbox(root)
lbx.pack(fill="both", expand=True)
for k in art_dic:
	lbx.insert("end", k)
lbx.bind("<Double-Button>", lambda x: run(lbx))
# articolo = simpledialog.askstring("Quale articolo vuoi?",keys, parent=root)
root.mainloop()