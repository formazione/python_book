# -*- encoding: utf-8 -*-
import os

# this is the start of the code


def head():
    "This goes into the head"
    return """</html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
    .blue {
    color : blue;
    }

    h2 {
    color: darkgray;
    }

    </style>
    </head>"""


class Div:
    collector = {}  # this collect all the istances of the class

    def __init__(self, title, paragraph="", img=""):
        self.title = title
        self.paragraph = paragraph
        self.img = img
        self.button = ""
        self.divcontent()
        Div.collector[self.title] = self

    def divcontent(self):
        "Each section is made with this code"
        # Here is the title of the section, the paragraph and buttons
        return """<div class="container">
        <h2>""" + self.title + """</h2>
            <p>""" + self.paragraph + """</p>""" \
            + self.button + """</div>"""

    def add_paragraph(self, content):
        self.paragraph += "<p>" + content + "</p>"

    def add_list(self, lista):
        "* after the : and # after ,"
        '''  === Istruzioni per aggiungere un elenco puntato ===
    per creare una lista, inserisci un asterisco dopo i due punti
    e un # dopo ogni virgola o punto e virgola di ogni item
        '''
        lista = lista.split("*")
        self.paragraph += "<b class='blue'>" + lista[0] + "</b><ul>"
        for items in lista[1].split("#"):
            # Visualizza ciò che è tra parentesi non in bold e in italic
            if "(" in items:
                items = items.replace("(", "</b>(<i>").replace(")", "</i>)</b>")
            self.paragraph += "<li><b>" + items + "</b></li>"
        self.paragraph += "</ul></p>"

    def add_image(self, img):
        self.paragraph += """<center><img src=\"""" + img + """"\" / ></center>"""

    def add_button(self, caption):
        self.buttonbody(self.buttonround(caption))

    def buttonround(self, caption):
        return("""<button type="button" class="btn btn-success">""" + caption + """</button> """)

    def buttonquare(self):
        return("""<button type="button" class="btn btn-default">Rounded corners</button>""")

    def buttonbody(self, newbutton):
        "This is the collection of elements into the body"
        self.button += newbutton
        return self.button

# the final part of the code


def end():
    return "\n</html>"


# this showe at console the code
def print_at_console():
    testo = head()
    for k, v in Div.collector.items():
        testo += v.divcontent()
    testo += end()
    print(testo)
# ===== FINE =====

# This saves the file in every self.paragraph into htmlfile


def create_html_file(htmlfile, see=0):
    with open(htmlfile, 'w', encoding='utf-8') as file:
        testo = head()
        for k, v in Div.collector.items():
            testo += v.divcontent()
        testo += end()
        file.write(testo)
    if see == 1:
        os.system(htmlfile)
    return htmlfile


class ExternalFile:
    def __init__(self, _file, _titolo):
        with open(_file, 'r', encoding='utf-8') as file:
            l = Div(_titolo)
            for line in file.readlines()[2:]:
                l.add_paragraph(line)

# here I add the content


class Paragraph:
    "Crea un oggetto Div e aggiunge i parametri per add_paragraph e add_list ecc."

    def __init__(self, title, paragraph, lista='', img='', end=''):
        self.div0 = Div(title)
        self.div0.add_paragraph(paragraph)
        if lista != "":
            self.div0.add_list(lista)
        if img != '':
            self.div0.add_image(img)
        if end !='':
            self.div0.add_paragraph(end)


"""
Put here all your paragraph
if you want to make more book create another Book class
"""

lista1 = [

    ["L'executive summary del business plan",
     "Il business plan è un documento che consente al management e ai finanziatori di conoscere i piani per la realizzazione di un nuovo prodotto o di una nuova attività, attraverso una descrizione del progetto affiancata da prospetti che ne quantificano la fattibilità."],

    ["Il contenuto del business plan",
     "Il business plan è composto da una sintesi del progetto, dalla sua espozizione dettagliata (comprensiva del marketing plan) e da una parte finale tecnica con la valutazione del progetto grazie all'elaborazione di prospetti che permettono di quantificare gli obiettivi esposti nelle prime due parti."],

    ["Esempio di sintesi (executive summary)",      # paragrafo
     "L'executive summary viene redatto in forma libera ed espone in modo sintetico idea di business (business idea) così da dare  chi lo legge una visione d'insieme ottimistica del progetto che si vuole realizzare, catturando l'attenzione del lettore. Viene inserito all'inizio del business plan, ma dovrebbe venir scritto alla fine. Non dobrebbe superare le 2 pagine.",
     # lista
     "La sintesi deve contenere:* le informazioni sui soggetti che vogliono realizzare il progetto,# le motivazioni di base,# la forma giuridica dell'impresa,# la mission e la vision,# il prodotto e il mercato,# l'organizzazione,# la localizzazione",
     # image
     "http://www.itprotoday.com/sites/itprotoday.com/files/styles/article_featured_standard/public/uploads/2015/07/win-exec-summary_0.png?itok=_8ce9cWD"],

     ["Esempio1",
     "Esempio tratto da https://www.thebalance.com/business-plan-executive-summary-example-2948007"],
     [     "La società e il management",
     "La società Amici a quattro zampe ha la sede centrale a Salerno. La società è di proprietà dei soci Roberto Rossi e Marta Serra. Roberto ha una consolidata esperienza nel settore della cura degli annimali, mentre Marta si è occupata di marketing e vendite per dieci anni. Il management è a cura dei due soci. I due soci si avvarranno della consulenza del commercialista Arturo Somma e del veterinario Giorgio De Rosa."],
     ["I nostri servizi",
     "I nostri clienti sono i padroni di cani e gatti che decidono di lasciare i loro animali a casa quando viaggiano o che vogliono lasciarli in compagnia quando sono al lavoro.",
     " La Amici a 4 zampe offre una varietà servizi per la cura degli animali che includono:* passeggiate,# visite quotidiane,# gestione delle cure mediche,# trattamenti di emergenza,# cura delle piante.# gestione della posta"],

     ["Il mercato",
     "Nella città di Salerno l'economia che ruota intorno alla cura degli animali ha avuto un'esplosione negli ultimi anni. La città di Salerno ha un grande numero di animali domestici. Una notra ricerca di mercato ha mostrato che 9 proprietari di animali su 10 preferirebbero ricevere le cure dei loro anumali nelle loro case piuttosto che nei canili e 6 su 10 pensano di far accudire gli aminali da un dog sitter mentre sono al lavoro."],
     ["Il nostro vantaggio competitivo",
     "Sono presenti otto società che si occupano di cura degli animali a Salerno.",
     "* di cui solo tre di questi offrono le cure sul posto,# nessuna prevede la visita agli animali da parte dei proprietari al lavoro,# la strategia di Amici a 4 zampe consiste nel sottolilneare la nostra attenzione alla qualità delle cure che forniamo ('amici dei vostri amici') e la disponibilità dei nostri servizi ('al vostro servizio 24 ore su 24'). I proprietari degli animali torneranno a casa e troveranno degli animali contenti e ben esercitati e già portati a spasso piuttosto che animali tristi e lamentosi,# tutti i servizi saranno resi da personale competente,# tutti gli impiegati sono assicurati"],

     ["Proiezioni finanziarie",
     "In base alle dimensioni del nostro mercato e la nostra area di mercato, le nostre proiezioni di vendita per il primo anno sono di 340.000 euro. Prevediamo un tasso di crescita del 10% per anno per i primi tre anni. Lo stipendio di ogni socio sarà di 40.000 euro. Avremo 6 impiegati formati e abbiamo in programma di assumerne altri 4 dopo aver avviato l'attività per un certo periodo. All'inizio uno dei soci si occuperà di organizzare gli impegni, ma abbiamo in programma di impiegare un receptionist a tempo pieno entro l'anno. Abbiamo già richieste da 40 clienti e abbiamo un piano per costruire velocemente una base di clienti attraverso inserzioni su riviste, siti web, social media e tramite direct mail. Le cure amorevoli e professionali di Amici a 4 zampe richiameranno sicuramente l'attenzione dei proprietari di cani e gatti di tutta la città di Salerno e zone limitrofe."],

     ["Start-up e fabbisogno finanziario",
     "Cerchiamo una linea di credito di 150.000 euro per finanziare il nostro primo anno. Insieme, i soci hanno investito 62.000 euro per andare incontro al fabbisogno finanziario iniziale."]


     ]


lista2 = [
    ["Esempio di esposizione dettagliata del progetto",
     ""],


    ["Esempio di marketing plan",
     ""],

    ["Esempio dei prospetti del business plan",
     ""]

]  # end of paragraphs


class Book:
    "Per ogni item della lista inviata, crea un paragrafo con titolo e contenuto"

    def __init__(self, lista):
        for item in lista:
            Paragraph(*item)  # This reads the content (prima parte)


# invia la lista con i paragrafi a book
Book(lista1)  # passa la lista di paragrafi che vuoi
titolo = "_".join(lista1[0][0].split()) + ".html"
create_html_file(htmlfile=titolo, see=1)  # This write the file
# listaparagrafi1[0][0] è il primo titolo, unito con _ per permettere a os.system di aprirlo

