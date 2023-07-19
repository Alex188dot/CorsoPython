import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

pwd = "your-db-pwd"





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



"""
Creiamo una classe menu ogni menu è rappresentato da un primo, un secondo, un contorno e la frutta. Inoltre ogni menu ha un prezzo a seconda che il menu sia di carne, pesce o da bambini. Il programma chiede all’utente quale menu desidera ordinare e dopo aver chiesto la mail dell’utente va a registrare su una tabella con database dedicato il tipo di menu, la mail del cliente e il prezzo del menu. Quando il programma termina, (l’utente preme 0) il programma stampa tutti gli ordini effettuati presenti sulla tabella, e il totale dell’incasso (somma dei prezzi presenti nella tabella)

Creare una interfaccia grafica per il programma precedente.
Il programma prevede una finestra dove l’utente inserisce la mail. una volta inserita la mail si apre una nuova finestra dove l’utente può scegliere il menu. Scelto il menu questo viene registrato nella tabella mysql.

"""


class Menu:
    def __init__(self, prezzo):
        self.prezzo = prezzo

    def __str__(self):
        return f"{self.prezzo}"


menuPesce = Menu(30)
menuCarne = Menu(25)
menuBambini = Menu(15)

# Created new database restaurant_menu
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE restaurant_menu")

print(mydb)
"""

# Created Customers Table and added Email, Choice and Price columns
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="restaurant_menu"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customers (Email VARCHAR(255), Choice VARCHAR(255), Price VARCHAR(255))")
"""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pwd,
    database="restaurant_menu"
)
mycursor = mydb.cursor()

# GUI code starts here

master = Tk()

# root window title and dimension
master.title("Login")


# Start code to center the window

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

centerWindow(master)

# adding a label to the root window
lbl1 = Label(master, text="Inserire il proprio indirizzo email: ")
lbl3 = Label(master)

lbl1.grid()
lbl3.grid()

# adding Entry Field
txt1 = Entry(master, width=10)
txt1.grid(column=1, row=0)
lbl3.grid(column=1, row=2)


def show_login(x):
    messagebox.showinfo("Login", x)


def show_alert(x):
    messagebox.showinfo("Result", x)


def logout():
    # mycursor.execute("SELECT * FROM customers")
    # myresult = mycursor.fetchall()
    # sum = 0
    #for x in myresult:
    #    sum += int(x[2])
    #    print(x)
    print("Il totale incassi è:", sum)
    master.destroy()


def clicked():
    email = txt1.get()
    cart = []
    text_cart = []
    res = "Email registrata con successo"
    lbl3.configure(text=res)
    show_login(res)
    # open a new window
    new_window = tk.Toplevel(master)
    new_window.title("Nuova Finestra")
    centerWindow(new_window)

    def mPesce():
        inp = "1"
        sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
        val = (email, inp, menuPesce.prezzo)
        mycursor.execute(sql, val)
        mydb.commit()
        cart.append(int(menuPesce.prezzo))
        text_cart.append("1 Menu di Pesce")
        show_alert("Scelta registrata")
        print(mycursor.rowcount, "Scelta registrata")

    def mCarne():
        inp = "2"
        sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
        val = (email, inp, menuCarne.prezzo)
        mycursor.execute(sql, val)
        mydb.commit()
        cart.append(int(menuCarne.prezzo))
        text_cart.append("1 Menu di Carne")
        show_alert("Scelta registrata")
        print(mycursor.rowcount, "Scelta registrata")

    def mBimbi():
        inp = "3"
        sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
        val = (email, inp, menuBambini.prezzo)
        mycursor.execute(sql, val)
        mydb.commit()
        cart.append(int(menuBambini.prezzo))
        text_cart.append("1 Menu Bambini")
        show_alert("Scelta registrata")
        print(mycursor.rowcount, "Scelta registrata")

    def done():
        new_cart = ", ".join(text_cart)
        subj = "Il suo ordine presso il Ristorante Python"
        body = f"Grazie per il suo ordine!\nDi seguito trova i dettagli di ciò che ha ordinato:\n{new_cart}\nTotale: {sum(cart)}€\n\nSe non riconosce questo ordine, invii immediatamente una mail a info@ristopython.com"
        invia_email(email, subj, body)
        new_window.destroy()

    btn1 = Button(new_window, text="Menu Pesce 🐟️",
                  fg="blue", command=mPesce)
    btn2 = Button(new_window, text="Menu Carne 🥩",
                  fg="blue", command=mCarne)
    btn3 = Button(new_window, text="Menu Bimbi 👧🧒",
                  fg="blue", command=mBimbi)
    btn4 = Button(new_window, text="Fatto! ✅",
                  fg="blue", command=done)
    btn1.place(relx=0.5, rely=0.15, anchor=CENTER)
    btn2.place(relx=0.5, rely=0.30, anchor=CENTER)
    btn3.place(relx=0.5, rely=0.45, anchor=CENTER)
    btn4.place(relx=0.5, rely=0.6, anchor=CENTER)

    new_window.mainloop()


button = tk.Button(master, command=show_alert)

# button widget with blue color text inside
btn = Button(master, text="Entra",
             fg="blue", command=clicked)
btn_2 = Button(master, text="Logout",
               fg="blue", command=logout)
# Set Button Grid
btn.place(relx=0.5, rely=0.45, anchor=CENTER)
btn_2.place(relx=0.5, rely=0.6, anchor=CENTER)

# Execute Tkinter
master.mainloop()
