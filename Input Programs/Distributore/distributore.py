import pickle
import time

"""
Creare un programma distributore. Ogni distributore ha associato un oggetto di tipo conto, con proprietà saldo, 
che rappresenta il saldo del conto, e id che rappresenta l'id del conto. L'oggetto distributore può invece: 
erogare caffè, erogare the, erogare acqua, erogare cioccolata a prezzi variabili, versare dei soldi nel conto. 
Il programma nel menu utente permette anche di creare un nuovo id con un nuovo saldo

Create a vending machine program. Each vending machine has an account type object associated with it, with 
the following properties: balance, which represents the account balance; and ID, which represents the account ID. 
The vending machine object can: distribute coffee, tea, water and chocolate at different prices. 
There is also a method to deposit money into the account. Furthermore, the program also allows you to create 
a new ID with a new balance.


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
                    print("Erogazione in corso...")
                    time.sleep(3)
                    print(f"Ecco il suo caffè! Il suo saldo rimanente è: {el.saldo}€. Buona giornata")
                else:
                    print("Saldo non sufficiente")
    def erogazioneThe(self, id):
        for el in self.lista:
            if el.id == id:
                if el.saldo >= 1.8:
                    el.saldo -= 1.8
                    print("Erogazione in corso...")
                    time.sleep(3)
                    print(f"Ecco il suo thè! Il suo saldo rimanente è: {el.saldo}€. Buona giornata")
                else:
                    print("Saldo non sufficiente")

    def erogazioneAcqua(self, id):
        for el in self.lista:
            if el.id == id:
                if el.saldo >= 1.5:
                    el.saldo -= 1.5
                    print("Erogazione in corso...")
                    time.sleep(1)
                    print(f"Ecco la sua acqua! Il suo saldo rimanente è: {el.saldo}€. Buona giornata")
                else:
                    print("Saldo non sufficiente")

    def erogazioneCioccolata(self, id):
        for el in self.lista:
            if el.id == id:
                if el.saldo >= 2.5:
                    el.saldo -= 2.5
                    print("Erogazione in corso...")
                    time.sleep(1)
                    print(f"Ecco la sua cioccolata! Il suo saldo rimanente è: {el.saldo}€. Buona giornata")
                else:
                    print("Saldo non sufficiente")

    def creaNuovaChiavetta(self, saldo, id):
        self.lista.append(Conto(saldo, id))
        print("Creazione in corso...")
        time.sleep(0.5)
        print("Chiavetta creata con successo!\nBuona giornata! ")
        f = open("distributore.pkl", "wb")
        pickle.dump(lista_chiavette, f)
        f.close()


    def ricaricaChiavetta(self, importo, id):
        for el in self.lista:
            if el.id == id:
                el.saldo += importo
                print("Ricarica in corso...")
                time.sleep(0.5)
                print(f"Ricarica effettuata con successo!Il suo saldo è: {el.saldo}€")

"""
c1 = Conto(10, 1)
c2 = Conto(10, 2)

lista_chiavette = [c1, c2]
d1 = Distributore(lista_chiavette)
"""

f = open("distributore.pkl", "rb")
unpickler = pickle.Unpickler(f)
lista_chiavette = unpickler.load()
d1 = Distributore(lista_chiavette)


accesso = False
while accesso != True:
    inp = input("Benvenuto")
    id = int(input("Prego inserisca l'ID della sua chiavetta, se non ne possiede una inserisca 0: "))
    if id == 0:
        accesso = True
        break
    for el in d1.lista:
        if el.id == id:
            print("Chiavetta riconosciuta")
            accesso = True

while inp != "7":
    inp = input(
    """
    Inserisca il numero corrispondente all'operazione che vuole effettuare:
    1) Caffè (1€)
    2) Thè (1.8€)
    3) Acqua (1.5€)
    4) Cioccolata (2.5€)
    5) Crea nuova utenza
    6) Ricarica chiavetta
    7) Esci
    """
    )
    if inp == "0":
        continue
    elif inp == "1":
        d1.erogazioneCaffe(id)
    elif inp == "2":
        d1.erogazioneThe(id)
    elif inp == "3":
        d1.erogazioneAcqua(id)
    elif inp == "4":
        d1.erogazioneCioccolata(id)
    elif inp == "5":
        saldo = int(input("Inserisca il denaro nella sua nuova chiavetta: "))
        id = (len(d1.lista) + 1)
        print("Questo è l'ID della sua nuova chiavetta:", id)
        d1.creaNuovaChiavetta(saldo, id)
        break
    elif inp == "6":
        importo = int(input("Inserisca il denaro che vuole ricaricare nella sua chiavetta: "))
        d1.ricaricaChiavetta(importo, id)
    elif inp == "7":
        print("Arrivederci e buona giornata")
        f = open("distributore.pkl", "wb")
        pickle.dump(lista_chiavette, f)
        f.close()
        break
    else:
        print("Scelta non valida, per favore scelga una opzioni qui sotto: ")
