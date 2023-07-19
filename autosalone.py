import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

pwd = "your-db-pwd"

"""
Creiamo una classe auto: ogni auto possiede una marca, un colore e uno stato optional che può essere “base” o “full optional”.
Successivamente creare una finestra dove l’utente può scegliere (ATTRAVERSO UNA COMBOBOX) tra una serie di scelte es: “Fiat, Ford, etc.”. L’utente cliccando il pulsante riceverà una mail con il prezzo dell’auto da lui scelta (inserire una entry per la mai dell’utente). Inoltre l’auto opzionata sarà inserita in una tabella di nome autoOpzionata con queste intestazioni :id : (potete usare l’autoincrement), marca, colore e prezzo.

"""

class Auto:
    def __init__(self, marca, colore, prezzo, optional="Base"):
        self.marca = marca
        self.colore = colore
        self.optional = optional
        self.prezzo = prezzo



    def __str__(self):
        return f"Marca: {self.marca}, colore: {self.colore}, optional: {self.optional}, prezzo: {self.prezzo}"

"""
# Created new database autosalone
mydb = mysql.connector.connect(
  host="localhost",
  user="master",
  password=pwd
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE autosalone")

print(mydb)
"""

# Created Customers Table and added ID, Email, Marca, Colore, Optional and Prezzo columns
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="master",
  password=pwd,
  database="autosalone"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customers (Id INT AUTO_INCREMENT PRIMARY KEY, Email VARCHAR(255), Marca VARCHAR(255), Colore VARCHAR(255), Optional VARCHAR(255), Prezzo VARCHAR(255))")
"""


def centerWindow(window):
    width = 600  # Width
    height = 300  # Height

    screen_width = window.winfo_screenwidth()  # Width of the screen
    screen_height = window.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


# End code to center the window

def invia_email(destinatario, oggetto, corpo):
    # Configura il server SMTP per inviare l'email (in questo esempio utilizzo Gmail)
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your-email-address"  # Inserisci il tuo indirizzo email
    sender_password = "your-app-password"  # Inserisci la tua password email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = destinatario
    message["Subject"] = oggetto
    message.attach(MIMEText(corpo, "plain"))

    # Connessione e invio dell'email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, destinatario, message.as_string())
        print("Email inviata con successo!")
    except Exception as e:
        print("Errore nell'invio dell'email:", str(e))
    finally:
        server.quit()


def mostra_selezione():
    marca = combobox1.get()
    colore = combobox2.get()
    optional = combobox3.get()
    if marca == "Fiat" and optional =="Base":
        prezzo = "12000"
    elif marca == "Fiat" and optional =="Full Optional":
        prezzo = "15000"
    elif marca == "Ford" and optional == "Base":
        prezzo = "16000"
    elif marca == "Ford" and optional == "Full Optional":
        prezzo = "20000"
    elif marca == "Wolkswagen" and optional == "Base":
        prezzo = "22000"
    elif marca == "Wolkswagen" and optional == "Full Optional":
        prezzo = "29000"
    elif marca == "Nissan" and optional == "Base":
        prezzo = "18000"
    elif marca == "Nissan" and optional == "Full Optional":
        prezzo = "24000"
    elif marca == "Renault" and optional == "Base":
        prezzo = "20000"
    elif marca == "Renault" and optional == "Full Optional":
        prezzo = "25000"
    subj = "Il suo ordine presso il Concessionario Solenghi"
    body = f"Congratulazioni per il suo nuovo acquisto!\nDi seguito i dettagli della sua scelta\n\nMacchina selezionata: {marca}\nColore: {colore}\nOptional: {optional}\nPrezzo: {prezzo}\n\nSe non riconosce questo ordine, invii immediatamente una mail a info@solenghiauto.com"
    email = txt1.get()
    invia_email(email, subj, body)
    res = "Email inviata con successo"
    lbl3.configure(text=res)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="autosalone"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO Customers (Email, Marca, Colore, Optional, Prezzo) VALUES (%s, %s, %s, %s, %s)"
    val = (email, marca, colore, optional, prezzo)
    mycursor.execute(sql, val)
    mydb.commit()

def quit():
    master.destroy()

master = tk.Tk()
centerWindow(master)

marca = ["Fiat", "Ford", "Wolkswagen", "Nissan", "Renault"]
combobox1 = ttk.Combobox(master, values=marca)
combobox1.pack()
colore = ["Blue", "Black", "Grey", "White"]
combobox2 = ttk.Combobox(master, values=colore)
combobox2.pack()
optional = ["Base", "Full Optional"]
combobox3 = ttk.Combobox(master, values=optional)
combobox3.pack()

lbl1 = Label(master, text="Inserire il proprio indirizzo email: ")
lbl3 = Label(master)

lbl1.pack()
lbl3.pack()
mostra_pulsante = ttk.Button(master, text="Invia", command=mostra_selezione)
mostra_pulsante.pack()
txt1 = Entry(master, width=20)
txt1.pack()
btn1 = Button(master, text="Esci", fg="blue", command=quit)
btn1.pack()



master.mainloop()