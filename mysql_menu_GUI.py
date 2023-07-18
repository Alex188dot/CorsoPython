import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

pwd = "your-db-password"

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

inp = input("Benvenuto nel programma di Prenotazione Menu, premere invio per continuare")
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

def clicked():
    email = txt1.get()
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
                show_alert("Scelta registrata")
                print(mycursor.rowcount, "Scelta registrata")

            def mCarne():
                inp = "2"
                sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
                val = (email, inp, menuCarne.prezzo)
                mycursor.execute(sql, val)
                mydb.commit()
                show_alert("Scelta registrata")
                print(mycursor.rowcount, "Scelta registrata")

            def mBimbi():
                inp = "3"
                sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
                val = (email, inp, menuBambini.prezzo)
                mycursor.execute(sql, val)
                mydb.commit()
                show_alert("Scelta registrata")
                print(mycursor.rowcount, "Scelta registrata")

            def logout():
                new_window.destroy()


            def topUp():
                new_window2 = tk.Toplevel(master)
                new_window2.title("Nuova Finestra importo")
                centerWindow(new_window2)

                # adding a label to the root window
                lblImporto = Label(new_window2, text="Inserire l'importo da ricaricare: ")
                lbl3Ricevuta = Label(new_window2)

                lblImporto.grid()
                lbl3Ricevuta.grid()

                # adding Entry Field
                txtM = Entry(new_window2, width=10)
                txtM.grid(column=1, row=0)
                lbl3.grid(column=1, row=2)

                def money():
                    topUp1 = m1.addMoney(id1, int(txtM.get()))
                    stringa = f"{topUp1[0]}"
                    saldo = f"Saldo rimanente: {topUp1[1]}€"
                    show_alert(stringa)
                    show_alert(saldo)

                btn6 = Button(new_window2, text="Done",
                          fg="blue", command=money)
                btn6.place(relx=0.5, rely=0.5, anchor=CENTER)

                centerWindow(new_window2)

            btn1 = Button(new_window, text="Coffee ☕️",
                          fg="blue", command=coffee)
            btn2 = Button(new_window, text="Tea 🫖",
                          fg="blue", command=tea)
            btn3 = Button(new_window, text="Chocolate 🍫",
                          fg="blue", command=chocolate)
            btn4 = Button(new_window, text="Water 🚰",
                          fg="blue", command=water)
            btn5 = Button(new_window, text="Top up 💰",
                          fg="blue", command=topUp)
            btn1.place(relx=0.5, rely=0.15, anchor=CENTER)
            btn2.place(relx=0.5, rely=0.30, anchor=CENTER)
            btn3.place(relx=0.5, rely=0.45, anchor=CENTER)
            btn4.place(relx=0.5, rely=0.6, anchor=CENTER)
            btn5.place(relx=0.5, rely=0.75, anchor=CENTER)

            new_window.mainloop()


button = tk.Button(master, command=show_alert)

# button widget with red color text inside
btn = Button(master, text="Login",
             fg="blue", command=clicked)
# Set Button Grid
btn.grid(column=3, row=4)

# Execute Tkinter
master.mainloop()




email = ""
while email != "0":
    verification = True
    email = input("Inserire Email, oppure 0 per uscire: ")
    if email == "0":
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        sum = 0
        for x in myresult:
            sum += int(x[2])
            print(x)
        print("Il totale incassi è:", sum)
        verification = False
    while verification:
        inp = input(
        """
        Inserire Scelta del menu:
        1) Menu di pesce,
        2) Menu di carne,
        3) Menu bamibini
        0) Per uscire
        """)
        if inp == "1":
            sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
            val = (email, inp, menuPesce.prezzo)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Scelta registrata")
        if inp == "2":
            sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
            val = (email, inp, menuCarne.prezzo)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Scelta registrata")
        if inp == "3":
            sql = "INSERT INTO Customers (Email, Choice, Price) VALUES (%s, %s, %s)"
            val = (email, inp, menuBambini.prezzo)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Scelta registrata")
        if inp == "0":
            verification = False
    if email == "0":
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        sum = 0
        for x in myresult:
            sum += int(x[2])
            print(x)
        print("Il totale incassi è:", sum)
        verification = False
