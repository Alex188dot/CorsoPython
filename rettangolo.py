import pickle

"""
Scrivere una classe Rettangolo i cui oggetti rappresentano rettangoli. Lo stato interno di un rettangolo è dato dai valori della base e dell’altezza. Un rettangolo deve mettere a disposizione tre operazioni: ridimensiona() che prende come parametri due nuovi valori di base e altezza e aggiorna lo stato, perimetro() che restituisce il perimetro e area() che restituisce l’area. Prevedere inoltre un costruttore che inizializza base e altezza del rettangolo.
Successivamente chiede in maniera iterativa all’utente:
1 di inserire base e altezza e aggiungerlo a una lista di rettangoli
2 di stampare la somma dei perimetri
3 di stampare la somma delle aree
4 di salvare la lista su un file
5 di leggere la lista da un file
6 uscire dal programma
"""

class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def __str__(self):
        return f"Base: {self.base} - Altezza: {self.altezza}"

    def ridimensiona(self, base, altezza):
        self.base = base
        self.altezza = altezza
        return f"Base: {self.base} - Altezza: {self.altezza}"

    def perimetro(self):
        return (self.base * 2) + (self.altezza * 2)

    def area(self):
        return self.base * self.altezza


r1 = Rettangolo(8, 8)
r2 = Rettangolo(5, 5)
print(r1.ridimensiona(10, 10)) # this is to check that the ridimensiona function works
lista = []
lista.append(r1)
lista.append(r2)


inp = input("Benvenuto nel Programma di Geometria, premere invio per continuare")

while inp != "6":
    inp = input(
    """
    1) Inserire base e altezza e aggiungerlo a una lista di rettangoli
    2) Stampare la somma dei perimetri
    3) Stampare la somma delle aree
    4) Salvare la lista su un file
    5) Leggere la lista da un file
    6) Uscire dal programma
    """
    )
    if inp == "1":
        base = int(input("Inserisci la base del triangolo: "))
        altezza = int(input("Inserisci l'altezza del triangolo: "))
        lista.append(Rettangolo(base, altezza))
    elif inp == "2":
        sum = 0
        for r in lista:
            print(r.perimetro())
            sum += r.perimetro()
        print("La somma dei perimetri è:", sum)
    elif inp == "3":
        sum = 0
        for r in lista:
            print(r.area())
            sum += r.area()
        print("La somma delle aree è:", sum)
    elif inp == "4":
        f = open("lista.pkl", "wb")
        pickle.dump(lista, f)
        f.close()
        print("File salvato con successo")
    elif inp == "5":
        f = open("lista.pkl", "rb")
        unpickler = pickle.Unpickler(f)
        lista = unpickler.load()
        f.close()
        for i in lista:
            print(i)
    elif inp == "6":
        print("Logout effettuato con successo")
        break
    else:
        print("Scelta non valida")
