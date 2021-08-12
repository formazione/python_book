text = """
LA COSTITUZIONE

E' COMPOSTA DA 139 ARTICOLI.

Entrata in vigore nel 1948, rappresenta il vertice del nostro sistema legislativo.

"""

import sys, time
from random import randrange



def texttime(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        # if c == " ":
        if randrange(1, 5) == 3:
            time.sleep(0.1)


def ask(q, rm):
    # rm è una stringa trasformata in lista con separatore ","
    rm = rm.split(",")
    texttime(q)
    for r in rm:
        textime(r)
    ya = input("> ")
    if ya == rm[0]:
        print("Bravo/a")
    else:
       print("No. Riprova")


texttime(text)

# Lista con domande e risposta esatta
qna = [
    
    # 1

    ["Quale articolo riconosce il diritto alla salute?",
    # =================================================
    # Scegli una delle seguenti risposte
    "32, 31, 30",
    # Risposta esatta
    "32"
    ]
]














