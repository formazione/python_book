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





texttime(text)
input("Fine")






