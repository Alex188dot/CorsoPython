"""
scrivere una classe contocorrente che rappresenta un conto corrente bancario. Il conto è rappresentato da uno username, un id e un saldo. Successivamente scrivere la classe bancomat che inizializza una lista di contocorrente e permette di prelevare dal conto, versare sul conto, fare un bonifico, visualizzare il saldo (plus se nel saldo riusciamo a visualizzare la lista movimenti). Inoltre scrivere un programma che permette all'utente di usufruire del bancomat dopo aver digitato lo username e l'id corretto associato al conto

"""

class Contocorrente:
    def __init__(self, username, id, saldo):
        self.username = username
        self.id = id
        self.saldo = saldo

    def __str__(self):
        return f"Username: {self.username} - ID: {self.id} - Saldo: {self.saldo}"

class Bancomat:
    def __init__(self, lista):
        lista = []
        self.lista = lista

    def __str__(self):
        return f"{self.lista}"

    def prelevare(self, importo):
        pass

    def versare(self, importo):
        pass

    def bonifico(self, importo):
        pass

    def visualizzare(self, importo):
        pass