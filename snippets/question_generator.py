# Question generator
from random import shuffle


FIX = "in quale prospetto di Bilancio andrà?"

sp ="""Denaro in cassa
Banca x c/c
Merci in magazzino
Risconti attivi
Debiti v/fornitori
Crediti v/clienti
Mutui passivi
Capitale sociale""".splitlines()

ce ="""Merci c/acquisti
Prodotti c/vendite
Ammortamenti
Interessi passivi
Fitti passivi""".splitlines()

all = sp + ce
shuffle(all)


prospetti = ["Stato patrimoniale",
    "Conto Economico"]

qna = []
for i in all:
    if i in sp:
        r, w = "Stato patrimoniale", "Conto economico"
    if i in ce:
        r, w = "Conto economico", "Stato patrimoniale"
    qna.append([f"{i}: {FIX}", r, w])

text = ""
for d in qna:
    text += f"{d[0]}\n{d[1]}\n{d[2]}\n\n"
print(text)