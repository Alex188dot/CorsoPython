import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt

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
# Created Manager Table and added Username and Pwd columns
"""

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="autosalone"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM restaurant_menu.Manager")
myresult = mycursor.fetchall()


mycursor.execute("CREATE TABLE Manager (Username VARCHAR(255), Pwd VARCHAR(255))")

# Added Username and PWD for Restaurant Manager

UID = "Admin1"
Admin_Pwd = "01"

sql = "INSERT INTO Manager (Username, Pwd) VALUES (%s, %s)"
val = (UID, Admin_Pwd)
mycursor.execute(sql, val)
mydb.commit()
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



def show_alert(x):
    messagebox.showinfo("Result", x)


def quit():
    master.destroy()

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
    subj = "Il suo Preventivo presso il Concessionario Solenghi"
    body = f"\nDi seguito i dettagli del preventivo riguardanti la sua scelta\n\nMacchina selezionata: {marca}\nColore: {colore}\nOptional: {optional}\nPrezzo: {prezzo}\n\nQuesto messaggio e gli eventuali allegati sono destinati esclusivamente al destinatario indicato e possono contenere informazioni confidenziali o riservate. Se avete ricevuto questa mail per errore, vi preghiamo di cancellarla immediatamente e di informare il mittente al seguente indirizzo: info@solenghiauto.com. Qualsiasi uso non autorizzato del contenuto di questa mail è vietato e può costituire una violazione della legge."
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


def admin_section():
    def admin_login():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=pwd,
            database="autosalone"
        )
        admin_UID = uid_entry1.get()
        admin_pwd = password_entry1.get()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM autosalone.Manager")
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

                    def mostra_grafici():
                        #Inizio conteggio Fiat base e full optional
                        count_Fiat_base = []
                        count_Fiat_fo = []
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="autosalone"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Marca ='Fiat'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            if x[4] == "Base":
                                count_Fiat_base.append(1)
                            elif x[4] == "Full Optional":
                                count_Fiat_fo.append(1)
                        # Fine conteggio Fiat base e full optional
                        # Inizio conteggio Ford base e full optional
                        count_Ford_base = []
                        count_Ford_fo = []
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="autosalone"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Marca ='Fiat'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            if x[4] == "Base":
                                count_Ford_base.append(1)
                            elif x[4] == "Full Optional":
                                count_Ford_fo.append(1)
                        # Fine conteggio Ford base e full optional
                        #Inizio conteggio Wolkswagen base e full optional
                        count_Ww_base = []
                        count_Ww_fo = []
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="autosalone"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Marca ='Wolkswagen'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            if x[4] == "Base":
                                count_Ww_base.append(1)
                            elif x[4] == "Full Optional":
                                count_Ww_fo.append(1)
                        # Fine conteggio Wv base e full optional
                        #Inizio conteggio Nissan base e full optional
                        count_Nissan_base = []
                        count_Nissan_fo = []
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="autosalone"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Marca ='Nissan'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            if x[4] == "Base":
                                count_Nissan_base.append(1)
                            elif x[4] == "Full Optional":
                                count_Nissan_fo.append(1)
                        # Fine conteggio Nissan base e full optional
                        # Inizio conteggio Renault base e full optional
                        count_Renault_base = []
                        count_Renault_fo = []
                        mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password=pwd,
                            database="autosalone"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Customers WHERE Marca ='Nissan'"
                        mycursor.execute(sql)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            if x[4] == "Base":
                                count_Renault_base.append(1)
                            elif x[4] == "Full Optional":
                                count_Renault_fo.append(1)
                        # Fine conteggio Renault base e full optional

                        # First graph

                        # Dati da visualizzare
                        categories = ["Fiat (Base)", "Fiat (FO)", "Ford (Base)", "Ford (FO)", "Ww (Base)", "Ww (FO)", "Nissan (Base)", "Nissan (FO)", "Renault (Base)", "Renault (FO)"]
                        fig, axes = plt.subplots(1, 2, figsize=(14, 10))
                        values = [len(count_Fiat_base), len(count_Fiat_fo), len(count_Ford_base), len(count_Ford_fo), len(count_Ww_base), len(count_Ww_fo), len(count_Nissan_base), len(count_Nissan_fo), len(count_Renault_base), len(count_Renault_fo)]
                        axes[0].bar(categories, values)
                        axes[0].set_title("Interesse preventivi per macchina")
                        axes[0].set_xlabel("Auto")
                        axes[0].set_ylabel("Preventivi richiesti")
                        axes[0].set_xticks(categories)
                        axes[0].set_xticklabels(categories, fontsize=8)  # Imposta le etichette e la dimensione del font
                        axes[0].tick_params(axis='x', which='major', rotation=20)  # Ruota i tick principali dell'asse x di 20 gradi

                        # End first graph

                        # Second graph
                        # Dati da visualizzare
                        labels = categories
                        sizes = values
                        colors = ['red', 'blue', 'green', 'brown', 'white', 'yellow', 'lightblue', 'purple']
                        # Creazione del grafico a torta
                        axes[1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
                        axes[1].set_title("Interesse in percentuale")
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

                    def m_g():
                        mostra_grafici()
                        plt.show()


                    def salva_grafici_pdf():
                        fig = mostra_grafici()
                        with PdfPages('grafici_autosalone.pdf') as pdf:
                            pdf.savefig(fig)
                            show_alert("PDF salvato con successo!")


                    def logout_admin_home():
                        new_window3.destroy()

                    graphs = Button(new_window3, text="Mostra Grafici 📊", fg="blue", command=m_g)
                    graphs.place(relx=0.5, rely=0.20, anchor=CENTER)
                    print_pdf = Button(new_window3, text="Stampa PDF 📄", fg="blue", command=salva_grafici_pdf)
                    print_pdf.place(relx=0.5, rely=0.30, anchor=CENTER)
                    logout = Button(new_window3, text="Logout", fg="blue", command=logout_admin_home)
                    logout.place(relx=0.5, rely=0.50, anchor=CENTER)
                    new_window3.mainloop()


    new_window2 = tk.Toplevel(master)
    centerWindow(new_window2)
    new_window2.title("Area Riservata")
    def admin_esci():
        new_window2.destroy()

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


master = tk.Tk()
centerWindow(master)
master.title("Autosalone Solenghi")


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
txt1 = Entry(master, width=20)
txt1.pack()
mostra_pulsante = ttk.Button(master, text="Invia", command=mostra_selezione)
mostra_pulsante.pack()
btn_area_r = Button(master, text="Area Riservata", fg="blue", command=admin_section)
btn_area_r.pack()
btn1 = Button(master, text="Esci", fg="blue", command=quit)
btn1.pack()





master.mainloop()