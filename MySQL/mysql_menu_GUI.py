import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
1) Creiamo una classe menu. Ogni menu ha un prezzo a seconda che il menu sia di carne, pesce o da bambini. Il programma chiede all’utente quale menu desidera ordinare e dopo aver chiesto la mail dell’utente va a registrare su una tabella con database dedicato il tipo di menu, la mail del cliente e il prezzo del menu. 

2) Creare una interfaccia grafica per il programma precedente.
Il programma prevede una finestra dove l’utente inserisce la mail. una volta inserita la mail si apre una nuova finestra dove l’utente può scegliere il menu. Scelto il menu questo viene registrato nella tabella mysql.

3) Implementare l’interfaccia del gestore. L’interfaccia va fatta con tkinter: il gestore inserisce username e password (ad esempio “rossi” “1234”) quando questi dati vengono verificati si apre una nuova finestra dove sono stampate: la lista degli ordini effettuati, statistiche con grafici utilizzando la libreria matplotlib

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
# Created Manager Table and added Username and Pwd columns

"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="restaurant_menu"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Manager (Username VARCHAR(255), Pwd VARCHAR(255))")
"""
# Added Username and PWD for Restaurant Manager
"""
UID = "Admin1"
Admin_Pwd = "01"

sql = "INSERT INTO Manager (Username, Pwd) VALUES (%s, %s)"
val = (UID, Admin_Pwd)
mycursor.execute(sql, val)
mydb.commit()
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

lbl1.pack()
lbl3.pack()

# adding Entry Field
txt1 = Entry(master, width=20)
txt1.pack()


def show_login(x):
    messagebox.showinfo("Login", x)


def show_alert(x):
    messagebox.showinfo("Result", x)


def quit():
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
    new_window.title("Scelta Menu")
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
        subj = "Il suo ordine presso Ristorante Python"
        body = f"Grazie per il suo ordine!\nDi seguito trova i dettagli di ciò che ha ordinato:\n{new_cart}\nTotale: {sum(cart)}€\n\nSe non riconosce questo ordine, invii immediatamente una mail a info@ristopython.com"
        invia_email(email, subj, body)
        new_window.destroy()

    btn1 = Button(new_window, text="Menu Pesce 🐟️", fg="blue", command=mPesce)
    btn2 = Button(new_window, text="Menu Carne 🥩", fg="blue", command=mCarne)
    btn3 = Button(new_window, text="Menu Bimbi 👧🧒", fg="blue", command=mBimbi)
    btn4 = Button(new_window, text="Fatto! ✅", fg="blue", command=done)
    btn1.place(relx=0.5, rely=0.15, anchor=CENTER)
    btn2.place(relx=0.5, rely=0.30, anchor=CENTER)
    btn3.place(relx=0.5, rely=0.45, anchor=CENTER)
    btn4.place(relx=0.5, rely=0.6, anchor=CENTER)

    new_window.mainloop()



def admin_section():
    def admin_esci():
        new_window2.destroy()
    def admin_login():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=pwd,
            database="restaurant_menu"
        )

        admin_UID = uid_entry1.get()
        admin_pwd = password_entry1.get()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM restaurant_menu.Manager")
        myresult = mycursor.fetchall()
        conta = []
        for x in myresult:
            if admin_UID not in x and admin_pwd not in x:
                conta.append("0")
            elif admin_UID in x and admin_pwd in x:
                conta.append("1")
                if conta.count("1") == 1:
                    show_alert("Bentornato!")
                    # open a new window
                    new_window3 = tk.Toplevel(master)
                    new_window3.title("Sezione Admin")
                    centerWindow(new_window3)

                    def mostra_categorie():
                        # Seleziono tutti i menu Pesce e li sommo
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="restaurant_menu"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Choice ='1'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        sum = 0
                        for x in myresult:
                            sum += int(x[2])
                        sumPesce = sum
                        # Fine somma Menu Pesce
                        # Seleziono tutti i menu Carne e li sommo
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="restaurant_menu"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Choice ='2'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        sum = 0
                        for x in myresult:
                            sum += int(x[2])
                        sumCarne = sum
                        # Fine somma Menu Carne
                        # Seleziono tutti i menu Bimbi e li sommo
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="restaurant_menu"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Choice ='3'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        sum = 0
                        for x in myresult:
                            sum += int(x[2])
                        sumBimbi = sum
                        # Fine somma Menu Bimbi

                        # First graph

                        # Dati da visualizzare
                        categories = ["M. Pesce", "M. Carne", "M. Bimbi"]
                        fig, axes = plt.subplots(1, 2)
                        values = [sumPesce, sumCarne, sumBimbi]
                        axes[0].bar(categories, values)
                        axes[0].set_title("Vendite in € per menu")
                        axes[0].set_xlabel("Categorie")
                        axes[0].set_ylabel("Euro")
                        # End first graph

                        # Second graph
                        # Dati da visualizzare
                        labels = categories
                        sizes = values
                        colors = ['red', 'blue', 'green']
                        # Creazione del grafico a torta
                        axes[1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
                        axes[1].set_title("Vendite in percentuale")
                        # End second graph

                        # Codice per centrare la finestra del grafico
                        mngr = plt.get_current_fig_manager()
                        # get the screen size in pixels
                        root = mngr.window._root()
                        width = root.winfo_screenwidth()
                        height = root.winfo_screenheight()
                        # get the figure size in pixels
                        fig_width = fig.get_figwidth() * fig.dpi
                        fig_height = fig.get_figheight() * fig.dpi
                        # compute the x and y coordinates to center the figure
                        x = (width - fig_width) / 2
                        y = (height - fig_height) / 2
                        # set the figure position and size
                        mngr.window.geometry("%dx%d+%d+%d" % (fig_width, fig_height, x, y))
                        # fine codice per centrare la finestra del grafico

                        return fig

                    def m_c():
                        mostra_categorie()
                        plt.show()


                    def mostra_per_utente():
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="restaurant_menu"
                        )
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT * FROM customers")
                        myresult = mycursor.fetchall()
                        new_list = []
                        for x in myresult:
                            if x[0] not in new_list:
                                new_list.append(x[0])

                        customer_total = []
                        for customer in new_list:
                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password=pwd,
                                database="restaurant_menu"
                            )
                            mycursor = mydb.cursor()
                            mycursor.execute(f"SELECT * FROM Customers WHERE Email ='{customer}'")
                            myresult_2 = mycursor.fetchall()
                            sum = 0
                            for x in myresult_2:
                                sum += int(x[2])
                            customer_total.append(sum)
                        # Dati da visualizzare
                        categories = new_list
                        values = customer_total

                        # Creazione dell'istogramma
                        fig = plt.figure(figsize=(12, 8))  # create a figure object
                        plt.bar(categories, values)

                        # Personalizzazione dell'aspetto del grafico
                        plt.title("Vendite per utente")
                        plt.xlabel("Utenti")
                        plt.ylabel("€")
                        plt.xticks(fontsize=8, rotation=20)  # Imposta la dimensione del font a 12 e ruota le etichette di 45 gradi

                        # Codice per centrare la finestra del grafico
                        mngr = plt.get_current_fig_manager()
                        # get the screen size in pixels
                        root = mngr.window._root()
                        width = root.winfo_screenwidth()
                        height = root.winfo_screenheight()
                        # get the figure size in pixels
                        fig_width = fig.get_figwidth() * fig.dpi  # use the fig object here
                        fig_height = fig.get_figheight() * fig.dpi  # and here
                        # compute the x and y coordinates to center the figure
                        x = (width - fig_width) / 2
                        y = (height - fig_height) / 2
                        # set the figure position and size
                        mngr.window.geometry("%dx%d+%d+%d" % (fig_width, fig_height, x, y))
                        # fine codice per centrare la finestra del grafico

                        # Ritorna il grafico
                        return fig

                    def m_p_u():
                        mostra_per_utente()
                        plt.show()


                    def mostra_incassi():
                        mycursor.execute("SELECT * FROM customers")
                        myresult = mycursor.fetchall()
                        sum = 0
                        for x in myresult:
                            sum += int(x[2])
                        #    print(x)
                        show_alert(f"Il totale incassi è: {sum}€")


                    def salva_grafici_pdf2():
                        fig = mostra_categorie()
                        fig2 = mostra_per_utente()
                        with PdfPages('grafici.pdf') as pdf:
                            pdf.savefig(fig)
                            pdf.savefig(fig2)
                            show_alert("PDF salvato con successo!")


                    def logout_admin_home():
                        new_window3.destroy()

                    btn_5 = Button(new_window3, text="Mostra Grafici per Categoria 📊", fg="blue", command=m_c)
                    btn_5.place(relx=0.5, rely=0.1, anchor=CENTER)
                    btn_6 = Button(new_window3, text="Mostra Entrate per Utente 💰", fg="blue", command=m_p_u)
                    btn_6.place(relx=0.5, rely=0.2, anchor=CENTER)
                    btn_9 = Button(new_window3, text="Mostra Incassi Totali 💵", fg="blue", command=mostra_incassi)
                    btn_9.place(relx=0.5, rely=0.3, anchor=CENTER)
                    btn_7 = Button(new_window3, text="Logout", fg="blue", command=logout_admin_home)
                    btn_7.place(relx=0.5, rely=0.6, anchor=CENTER)
                    btn_10 = Button(new_window3, text="Stampa PDF 📄", fg="blue", command=salva_grafici_pdf2)
                    btn_10.place(relx=0.5, rely=0.4, anchor=CENTER)
                    new_window3.mainloop()

    # open a new window
    new_window2 = tk.Toplevel(master)
    new_window2.title("Area Riservata")

    uid_label = Label(new_window2, text="Username:")
    uid_label.pack()
    uid_entry1 = Entry(new_window2)
    uid_entry1.pack()
    password_label1 = Label(new_window2, text="Password:")
    password_label1.pack()
    password_entry1 = Entry(new_window2, show="*")
    password_entry1.pack()
    btn_4 = Button(new_window2, text="Login", fg="blue", command=admin_login)
    btn_4.pack()
    btn_8 = Button(new_window2, text="Esci", fg="blue", command=admin_esci)
    btn_8.pack()




    centerWindow(new_window2)


button = tk.Button(master, command=show_alert)

# button widget with blue color text inside
btn = Button(master, text="Entra", fg="blue", command=clicked)
btn_2 = Button(master, text="Esci", fg="blue", command=quit)
btn_3 = Button(master, text="Area Riservata", fg="blue", command=admin_section)
# Set Button Grid
btn.place(relx=0.5, rely=0.35, anchor=CENTER)
btn_2.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_3.place(relx=0.5, rely=0.65, anchor=CENTER)

# Execute Tkinter
master.mainloop()
