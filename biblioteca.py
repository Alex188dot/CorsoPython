import pickle


class Libro:
    def __init__(self, titolo, autore, pubblicazione, disponibile=True):
        self.titolo = titolo
        self.autore = autore
        self.pubblicazione = pubblicazione
        self.disponibile = disponibile

    def __str__(self):
        return f"{self.titolo} - {self.autore} - {self.pubblicazione} - {self.disponibile}"


class Biblioteca:
    def __init__(self, lista):
        lista = []
        self.lista = lista

    def __str__(self):
        return f"{self.lista}"

    def add(self, libro):
        self.lista.append(libro)

    def book(self, libro):
        libro.disponibile = False

    def printLista(self):
        print(self.lista)



biblio1 = Biblioteca("lista1")



inp = input("Benvenuto nel gestionale della Biblioteca, premere invio per continuare")

while inp != "7":
    inp = input(
        """
    1) aggiungere un nuovo libro
    2) prenotare un libro dal titolo
    3) ricercare i libri per autore
    4) riportare un libro per titolo
    5) salvare la biblioteca su un file
    6) leggere la biblioteca salvata
    7) uscire dal programma
    """
    )
    if inp == "1":
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci il nome dell'autore: ")
        pubblicazione = input("Inserisci la data di pubblicazione: ")
        biblio1.add(Libro(titolo, autore, pubblicazione))
    elif inp == "2":
        titolo = input("Inserisci il titolo del libro: ")
        for libro in biblio1.lista:
            if libro.titolo == titolo and libro.disponibile:
                print("Libro prenotato con successo!")
                biblio1.book(libro)
            elif libro.titolo == titolo and not libro.disponibile:
                print("Libro non disponibile")
    elif inp == "3":
        autore = input("Inserisci l'autore del libro: ")
        for libro in biblio1.lista:
            if libro.autore == autore:
                print(libro)
    elif inp == "4":
        titolo = input("Inserisci il titolo del libro da riportare: ")
        for libro in biblio1.lista:
            if libro.titolo == titolo and libro.disponibile:
                print("Libro già presente in Biblioteca!")
            elif libro.titolo == titolo and not libro.disponibile:
                print("Libro riportato con successo!")
                libro.disponibile = True
    elif inp == "5":
        f = open("biblioteca1.pkl", "wb")
        pickle.dump(biblio1.lista, f)
        f.close()
        print("File salvato con successo")
    elif inp == "6":
        f = open("biblioteca1.pkl", "rb")
        unpickler = pickle.Unpickler(f)
        biblio1.lista = unpickler.load()
        f.close()
        for i in biblio1.lista:
            print(i)
    elif inp == "7":
        print("Logout effettuato con successo")
        break
    else:
        print("Scelta non valida")
