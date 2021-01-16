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

def popup():
	articolo = simpledialog.askstring("Quale articolo vuoi?","Uno della lista", parent=root)
	art(articolo)

root = tk.Tk()
root.title("Links launcher")
root.geometry("250x400")

#                 MENU
menubar = tk.Menu(root)
menubar.add_command(label="Popup", command=popup)
root.config(menu=menubar)

# ============== gently offered by python_book menu.py


lbx = tk.Listbox(root)
lbx.pack(fill="both", expand=True)
for k in art_dic:
	lbx.insert("end", k)
lbx.bind("<Double-Button>", lambda x: run(lbx))
# articolo = simpledialog.askstring("Quale articolo vuoi?",keys, parent=root)
root.mainloop()