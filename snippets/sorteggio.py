import random
import sys
from tkinter import messagebox    



    
class Win:
    def sorteggio(max):
        r = [x for x in range(1, max)]
        random.shuffle(r)
        elenco = ""
        for i in r:
            elenco += str(i) + "\n"
        return elenco
    
    def popup(self,
        title="...",
        sentence="..."):

        #tk.Tk().withdraw()
        name = messagebox.showinfo(
            title=title,
            message=sentence)

elenco = Win.sorteggio(21)
Win.popup("Elenco", "Elenco", elenco)




























