
class Canzone:
    def __init__(self, titolo, autore, pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.pubblicazione = pubblicazione

    def __str__(self):
        return f"{self.titolo} - {self.autore} - {self.pubblicazione}"


listaCanzoni = []

c1 = Canzone("Volare", "Mario", "2019")
listaCanzoni.append(c1)
c2 = Canzone("Cantare", "Luigi", "2020")
listaCanzoni.append(c2)
c3 = Canzone("Oh oh oh oh", "Mario", "1998")
listaCanzoni.append(c3)

inp = input("Benvenuto nel programma, premi invio per continuare: ")

while inp != "5":
    inp = input("""
Cosa vuoi fare? Inserisci il tasto corrispondente:
1 aggiungere una nuova canzone
2 cercare una canzone dalla lista per titolo
3 stampare tutte le canzoni di un autore
4 rimuovere una canzone dal titolo
5 uscire dal programma
""")
    if inp == "1":
        titolo = input("Inserisci il titolo della canzone: ")
        autore = input("Inserisci il nome dell'autore: ")
        pubblicazione = input("Inserisci la data di pubblicazione: ")
        listaCanzoni.append(Canzone(titolo, autore, pubblicazione))
    elif inp == "2":
        titolo = input("Inserisci il titolo della canzone: ")
        found = False
        for canzone in listaCanzoni:
            if canzone.titolo == titolo:
                print(f"La canzone è presente nella raccolta: { canzone } ")
                found = True
        if not found:
            print("Canzone non presente nella raccolta, provare con un altro titolo")
    elif inp == "3":
        autore = input("Inserisci il nome dell'autore: ")
        found = False
        for canzone in listaCanzoni:
            if canzone.autore == autore:
                print(f"{ canzone } ")
                found = True
        if not found:
            print("Autore non presente nella raccolta, provare con un altro autore")
    elif inp == "4":
        titolo = input("Inserisci il titolo della canzone: ")
        for canzone in listaCanzoni:
            if canzone.titolo == titolo:
                listaCanzoni.remove(canzone)
    elif inp == "5":
        break
    else:
        print("Scelta non valida")



