import random
import sys
from tkinter import messagebox    


def sorteggio(max):
    r = [x for x in range(max)]
    random.shuffle(r)
    elenco = ""
    for i in r:
        elenco += i
    Win.popup("Elenco", elenco)
        

class Win:
    def popup(self,
        title="...",
        sentence="..."):

        #tk.Tk().withdraw()
        name = messagebox.showinfo(
            title=title, message=sentence)

sorteggio(15)














