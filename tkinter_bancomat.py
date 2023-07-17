import pickle
from tkinter import *
import tkinter as tk

movimenti = []
class Contocorrente:
    def __init__(self, username, id, saldo):
        self.username = username
        self.id = id
        self.saldo = saldo
        self.listamovimenti = []

    def __str__(self):
        return f"Username: {self.username}, ID conto: {self.id}, Saldo: € {self.saldo}\n"


class Bancomat:
    def __init__(self, conti):
        self.conti = conti

    def __str__(self):
        return self.conti

    def prelievo(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo > cifra:
                    i.saldo -= cifra
                    stampa = (f"Prelievo effettuato con successo\nIl saldo aggiornato è di € {i.saldo}")
                    i.listamovimenti.append(stampa)
                    return stampa
                else:
                    stampa = "saldo non disponibile"
                    return stampa

    def versamento(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                i.saldo += cifra
                stampa = (f"Versamento effettuato con successo\nIl saldo aggiornato è di € {i.saldo}")
                i.listamovimenti.append(stampa)
                return stampa

    def bonifico(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo > cifra:
                    i.saldo -= cifra + 1.50
                    stampa = (f"Bonifico effettuato con successo\nIl saldo aggiornato è di € {i.saldo}")
                    i.listamovimenti.append(stampa)
                    return stampa
                else:
                    stampa = "saldo non disponibile"
                    return stampa

    def stampa_saldo(self, id):
        for i in self.conti:
            if i.id == id:
                stampa = (f"Il saldo aggiornato è di € {i.saldo}")
                return stampa

    def stampa_movimenti(self, id):
        for i in self.conti:
            if i.id == id:
                stampa = (f"Di seguito la lista dei suoi ultimi movimenti: {i.listamovimenti}")
                return stampa

"""
utente1 = Contocorrente("User 1", "01", int(10000))
utente2 = Contocorrente("User 2", "02", int(30000))
lista_utenti = []
lista_utenti.append(utente1)
lista_utenti.append(utente2)
b1 = Bancomat(lista_utenti)
b1.versamento(400, "02")
b1.prelievo(200, "02")
b1.stampa_movimenti("02")
f = open("testBancomat1.pkl", "wb")
pickle.dump(lista_utenti, f)
f.close()
"""


# Start code to center the window

def centerWindow(window):
    width = 600  # Width
    height = 400  # Height

    screen_width = window.winfo_screenwidth()  # Width of the screen
    screen_height = window.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


# End code to center the window


print("Benvenuto nella tua home banking.")

f = open("testBancomat1.pkl", "rb")
unpickler = pickle.Unpickler(f)
lista_utenti = unpickler.load()
b1 = Bancomat(lista_utenti)
f.close()

validation = False
'''
while validation == False:
    user = input("digita il tuo username: ")
    idcode = input("digita il tuo ID utente: ")
    for el in lista_utenti:
        if user == el.username and idcode == el.id:
            print("Utente convalidato.")
            utente_attivo = el
            validation = True
            scelta = 0
            while scelta != "6":
                scelta = input("Digitare\n"
                               "1 per prelevare\n"
                               "2 per versare\n"
                               "3 per effettuare un bonifico\n"
                               "4 per visualizzare il saldo\n"
                               "5 per visualizzare l'elenco movimenti\n"
                               "6 per terminare: ")
                if scelta == "1":
                    importo = int(input("\nInserisci la cifra da prelevare: "))
                    b1.prelievo(importo, utente_attivo.id)
                elif scelta == "2":
                    importo = int(input("\nInserisci la cifra da versare: "))
                    b1.versamento(importo, utente_attivo.id)
                elif scelta == "3":
                    importo = int(input("\nInserisci l'importo del bonifico: "))
                    b1.bonifico(importo, utente_attivo.id)
                elif scelta == "4":
                    b1.stampa_saldo(utente_attivo.id)
                elif scelta == "5":
                    b1.stampa_saldo(utente_attivo.id)
                elif scelta == "":
                    f = open("testBancomat1.pkl", "wb")
                    pickle.dump(lista_utenti, f)
                    f.close()
                    exit()
                else:
                    print("Scelta non valida.")

    if validation == False:
        print("Utente non trovato. Riprova.")
'''

from tkinter import *

def open():
    user = password_entry.get()
    password = password_entry1.get()
    for el in lista_utenti:
        if user == el.username and password == el.id:
            # Define the function p inside the open function
            def p():
                importo = int(password_entry2.get())
                output = b1.prelievo(importo, password)
                display_label.configure(text=output)

            def v():
                importo = int(password_entry2.get())
                output = b1.versamento(importo, password)
                display_label.configure(text=output)

            def b():
                importo = int(password_entry2.get())
                output = b1.bonifico(importo, password)
                display_label.configure(text=output)

            def s():
                output = b1.stampa_saldo(password)
                display_label.configure(text=output)

            def m():
                output = b1.stampa_movimenti(password)
                display_label.configure(text=output)



            Preleva = Button(root, text="Preleva", command=p)
            Preleva.pack()
            Versa = Button(root, text="Versa", command=v)
            Versa.pack()
            Bonifico = Button(root, text="Bonifico", command=b)
            Bonifico.pack()
            Saldo = Button(root, text="Saldo", command=s)
            Saldo.pack()
            Movimenti = Button(root, text="Movimenti", command=m)
            Movimenti.pack()
            password_entry2.pack()


# create root window
root = Tk()
root.geometry('300x300')
# root window title and dimension
root.title("Bancomat Talentform")
# Set geometry(widthxheight)
# Creazione del pulsante di login
login_button = Button(root, text="Login", command=open)
login_button.pack()
password_label = Label(root, text="Username:")
password_label.pack()
password_entry = Entry(root)
password_entry.pack()
password_label1 = Label(root, text="Password:")
password_label1.pack()
password_entry1 = Entry(root, show="*")
password_entry1.pack()


password_entry2 = Entry(root)
password_entry2.pack_forget()
display_label = Label(root)
display_label.pack()

centerWindow(root)

# Execute Tkinter
root.mainloop()
