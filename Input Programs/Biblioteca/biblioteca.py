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

    def printLista(self):
        for l in self.lista:
            print(l)

# The data below will be saved onto the biblioteca1.pkl file, so it is not necessary anymore. Leaving it here for reference.

"""
l1 = Libro("Test", "Mario", 2000, True)
l2 = Libro("Test2", "Luigi", 2001, True)
l3 = Libro("Test3", "Anna", 2002, True)
l4 = Libro("Test4", "Marco", 2001, True)
lista1 = [l1, l2, l3, l4]
"""
biblio1 = Biblioteca("lista1")

def save():
    f = open("biblioteca1.pkl", "wb")
    pickle.dump(biblio1.lista, f)
    f.close()
    print("File salvato con successo")

def read_library():
    f = open("biblioteca1.pkl", "rb")
    unpickler = pickle.Unpickler(f)
    biblio1.lista = unpickler.load()
    f.close()

inp = input("Benvenuto nel gestionale della Biblioteca, premere invio per continuare")

while inp != "6":
    read_library()
    inp = input(
        """
    1) aggiungere un nuovo libro
    2) prenotare un libro dal titolo
    3) ricercare i libri per autore
    4) riportare un libro per titolo
    5) leggere la biblioteca salvata
    6) uscire dal programma
    """
    )
    if inp == "1":
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci il nome dell'autore: ")
        pubblicazione = input("Inserisci la data di pubblicazione: ")
        biblio1.add(Libro(titolo, autore, pubblicazione))
        save()
    elif inp == "2":
        titolo = input("Inserisci il titolo del libro: ")
        found = False
        for libro in biblio1.lista:
            if libro.titolo == titolo and libro.disponibile:
                found = True
                print("Libro prenotato con successo!")
                libro.disponibile = False
                save()
            elif libro.titolo == titolo and not libro.disponibile:
                found = True
                print("Libro non disponibile")
        if not found:
            print("Libro non presente in biblioteca")
    elif inp == "3":
        autore = input("Inserisci l'autore del libro: ")
        found = False
        for libro in biblio1.lista:
            if libro.autore == autore:
                print(libro)
                found = True
        if not found:
                print("Libro non presente in biblioteca")
    elif inp == "4":
        titolo = input("Inserisci il titolo del libro da riportare: ")
        for libro in biblio1.lista:
            if libro.titolo == titolo and libro.disponibile:
                print("Libro già presente in Biblioteca!")
            elif libro.titolo == titolo and not libro.disponibile:
                print("Libro riportato con successo!")
                libro.disponibile = True
                save()
    elif inp == "5":
        biblio1.printLista()
    elif inp == "6":
        print("Logout effettuato con successo")
        break
    else:
        print("Scelta non valida")


