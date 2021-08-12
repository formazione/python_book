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

root = tk.Tk()
root.withdraw()
keys = ""
for k in art_dic:
	keys += k + "\n"

articolo = simpledialog.askstring("Quale articolo vuoi?",keys, parent=root)
art(articolo)
root.mainloop()


