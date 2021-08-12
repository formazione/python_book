from random import shuffle



import sys, time
from random import randrange



def text_time(words, sleep=0.05):
    "Shows a text one word at the time"
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        # if c == " ":
        if randrange(1, 5) == 3:
            time.sleep(sleep)


def ask(q_rm): # follow: get_users_answer
    "Shows the question, get the answer and check if it's right"
    # rm è una stringa trasformata in lista con separatore ","
    q, rm = q_rm
    rm = rm.split(",")
    correct = rm[0] # memorize the right one, before shuffling (from random import shuffle)
    shuffle(rm)
    text_time(q) # show_question
    for n, r in enumerate(rm): # shows_answers
        print()
        text_time(f"{n+1}) {r}")
    get_users_answer(rm, correct)


def get_users_answer(rm, correct): # called by ask
    print()
    text_time("Num. risposta esatta")
    ya = input("> ")
    # se l'item delle risposte multiple con indice che l'utente ha
    # inserito è uguale alla domanda corretta è giusta
    if rm[int(ya) - 1] == correct:
        text_time("Bravo/a")
    else:
       text_time("No. Riprova")
    print()
    print()



# Lista con domande e risposta esatta

modulo1 = """
LA COSTITUZIONE, 139 ARTICOLI, entrata in vigore nel 1948.
È al vertice del nostro sistema legislativo.
"""

qna1 = [
    ["Quando è entrata in vigore?", "48,47,49"],
    ["Quale articolo riconosce il diritto alla salute?","32,31,30"],
    ]

score = {} 
def nome():
    name = input("Chi fa il test?")
    score[name] = 0
    return name

def quiz(content, qna):
    name = nome()
    text_time(f"Ok {name}", 0.1)
    text_time(" vediamo quanto sei preparato.", 0.1)
    print()
    text_time("======================", 0.2)
    print(content)
    print()
    for n in qna:
        ask(n)

quiz(modulo1, qna1)

text_time("FINE DEL TEST")
time.sleep(2)
