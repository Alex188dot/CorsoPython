"""
Creare un programma distributore. Ogni distributore ha associato un oggetto di tipo conto, con proprietà saldo, che rappresenta il saldo del conto, e id che rappresenta l'id del conto. L'oggetto distributore può invece: erogare caffè, erogare the, erogare acqua, erogare cioccolata a prezzi variabili, versare dei soldi nel conto. Il programma nel menu utente permette anche di creare un nuovo id con un nuovo saldo
"""


class Conto:
    def __init__(self, saldo, id):
        self.saldo = saldo
        self.id = id

    def __str__(self):
        return f"Saldo: {self.saldo} - ID: {self.id}"

class Distributore:
    def __init__(self, lista):
        self.lista = lista

    def erogazioneCaffe(self, id):
        for el in self.lista:
            if el.id == id:
                if el.saldo >= 1:
                    el.saldo -= 1
                    print(f"Ecco il suo caffè! Il suo saldo rimanente è: {el.saldo}. Buona giornata")
                else:
                    print("Saldo non sufficiente")
    def erogazioneThe(self, id):
        id.saldo -= 1.8

    def erogazioneAcqua(self, id):
        id.saldo -= 1.5

    def erogazioneCioccolata(self, id):
        id.saldo -= 2.5

    def ricaricaChiavetta(self, importo, id):
        id.saldo += importo




c1 = Conto(10, 1)
c2 = Conto(10, 2)

lista_conti = [c1, c2]
d1 = Distributore(lista_conti)

inp = input("Benvenuto")
id = int(input("Prego inserisca l'ID della sua chiavetta: "))
while inp != "7":
    inp = input(
    """
    Inserisca il numero corrispondente all'operazione che vuole effettuare:
    1) Caffè
    2) Thè
    3) Acqua
    4) Cioccolata
    5) Crea nuova utenza
    6) Ricarica chiavetta
    7) Esci
    """
    )
    if inp == "1":
        d1.erogazioneCaffe(id)


