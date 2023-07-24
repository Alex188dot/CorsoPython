import mysql.connector
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from PIL import Image


pwd = "your-db-pwd"

"""
Creare un file html con 4 select che rappresentano le scelte degli utenti per un ristorante.
Le select rappresentano il primo, il secondo, il contorno e il dolce.
Ogni select avrà valori diversi per il primo es. “lasagna”, “risotto” etc
per il secondo “cotoletta”, “spigola” etc.
"""


class Piatto:
    def __init__(self, id, prezzo):
        self.prezzo = prezzo
        self.id = id

    def __str__(self):
        return f"{self.prezzo}"

# Primi
pastaBoscaiola = Piatto(1, 12)
risottoZafferano = Piatto(2, 10)
pizzaMargherita = Piatto(3, 8)

# Secondi
cotoletta = Piatto(4, 11)
tagliata = Piatto(5, 15)
salmone = Piatto(6, 14)

# Contorni
cicoria = Piatto(7, 6)
patatine = Piatto(8, 5)
insalata = Piatto(9, 7)

# Dolci
tiramisu = Piatto(10, 6)
cremcaramel = Piatto(11, 6)
pannacotta = Piatto(12, 6)

# Created new database restaurant_menu_flask
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE restaurant_menu_flask")

print(mydb)

"""
# Created Customers Table and added Email, Primo, Secondo, Contorno, Dolce and Price columns
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="restaurant_menu_flask"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customers (Id INT AUTO_INCREMENT PRIMARY KEY, Email VARCHAR(255), Primo VARCHAR(255), Secondo VARCHAR(255), Contorno VARCHAR(255), Dolce VARCHAR(255), Price VARCHAR(255))")
"""

# Created Manager Table and added Username and Pwd columns
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="restaurant_menu_flask"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Manager (Username VARCHAR(255), Pwd VARCHAR(255))")

# Added Username and PWD for Restaurant Manager

UID = "Admin1"
Admin_Pwd = "01"

sql = "INSERT INTO Manager (Username, Pwd) VALUES (%s, %s)"
val = (UID, Admin_Pwd)
mycursor.execute(sql, val)
mydb.commit()
"""

# Created Accepted Orders Table and added Email, Primo, Secondo, Contorno, Dolce and Price columns
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="restaurant_menu_flask"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Accepted_Orders (Id INT AUTO_INCREMENT PRIMARY KEY, Email VARCHAR(255), Primo VARCHAR(255), Secondo VARCHAR(255), Contorno VARCHAR(255), Dolce VARCHAR(255), Price VARCHAR(255))")
"""


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
    message.attach(MIMEText(corpo, "html"))
    # Open the image file in binary mode
    fp = open('static/email-logo.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<email-logo>')
    message.attach(msgImage)

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




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/stamp', methods=['POST'])
def stamp():
    cart = []
    email = request.form['email']
    primo = request.form['primo']
    secondo = request.form['secondo']
    contorno = request.form['contorno']
    dolce = request.form['dolce']
    if primo == "1":
        primo = "Pasta Boscaiola"
        cart.append(int(pastaBoscaiola.prezzo))
    elif primo == "2":
        primo = "Risotto allo Zafferano"
        cart.append(int(risottoZafferano.prezzo))
    elif primo == "3":
        primo = "Pizza Margherita"
        cart.append(int(pizzaMargherita.prezzo))
    if secondo == "4":
        secondo = "Cotoletta alla milanese"
        cart.append(int(cotoletta.prezzo))
    elif secondo == "5":
        secondo = "Tagliata"
        cart.append(int(tagliata.prezzo))
    elif secondo == "6":
        secondo = "Salmone"
        cart.append(int(salmone.prezzo))
    if contorno == "7":
        contorno = "Cicoria"
        cart.append(int(cicoria.prezzo))
    elif contorno == "8":
        contorno = "Patatine fritte"
        cart.append(int(patatine.prezzo))
    elif contorno == "9":
        contorno = "Insalata"
        cart.append(int(insalata.prezzo))
    if dolce == "10":
        dolce = "Tiramisù"
        cart.append(int(tiramisu.prezzo))
    elif dolce == "11":
        dolce = "Crem Caramel"
        cart.append(int(cremcaramel.prezzo))
    elif dolce == "12":
        dolce = "Panna Cotta"
        cart.append(int(pannacotta.prezzo))
    prezzo = sum(cart)

    ordine = f"{primo}, {secondo}, {contorno}, {dolce}. Il totale è: {prezzo}€"


   # This code will add the order to the DB
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="restaurant_menu_flask"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO Customers (Email, Primo, Secondo, Contorno, Dolce, Price) VALUES (%(email)s, %(primo)s, %(secondo)s, %(contorno)s, %(dolce)s, %(prezzo)s)"
    data = {
        "email": email,
        "primo": primo,
        "secondo": secondo,
        "contorno": contorno,
        "dolce": dolce,
        "prezzo": prezzo
    }
    mycursor.execute(sql, data)
    mydb.commit()
    print(mycursor.rowcount, "Scelta registrata")
    return render_template('menu_result.html', ordine=ordine)


def stats1():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="restaurant_menu_flask"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Price FROM Accepted_Orders")
    myresult = mycursor.fetchall()
    tot = 0
    for x in myresult:
        tot += int(x[0])

    dishes_count = []
    # Get the total counts for Pasta Boscaiola
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Primo = 'Pasta Boscaiola'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    boscaiolaCount = [x[0] for x in myresult]
    dishes_count.append(boscaiolaCount)

    # Get the total counts for Risotto allo Zafferano
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Primo = 'Risotto allo Zafferano'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    risottoCount = [x[0] for x in myresult]
    dishes_count.append(risottoCount)

    # Get the total counts for Pizza Margherita
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Primo = 'Pizza Margherita'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    pizzaCount = [x[0] for x in myresult]
    dishes_count.append(pizzaCount)

    # Get the total counts for Cotoletta alla milanese
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Secondo = 'Cotoletta alla milanese'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    cotolettaCount = [x[0] for x in myresult]
    dishes_count.append(cotolettaCount)

    # Get the total counts for Tagliata
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Secondo = 'Tagliata'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    tagliata = [x[0] for x in myresult]
    dishes_count.append(tagliata)

    # Get the total counts for Salmone
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Secondo = 'Salmone'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    salmone = [x[0] for x in myresult]
    dishes_count.append(salmone)

    # Get the total counts for Cicoria
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Contorno = 'Cicoria'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    cicoria = [x[0] for x in myresult]
    dishes_count.append(cicoria)

    # Get the total counts for Patatine Fritte
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Contorno = 'Patatine Fritte'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    patatine = [x[0] for x in myresult]
    dishes_count.append(patatine)

    # Get the total counts for Insalata
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Contorno = 'Insalata'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    insalata = [x[0] for x in myresult]
    dishes_count.append(insalata)

    # Get the total counts for Tiramisù
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Dolce = 'Tiramisù'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    tiramisu = [x[0] for x in myresult]
    dishes_count.append(tiramisu)

    # Get the total counts for Crem Caramel
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Dolce = 'Crem Caramel'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    cremCaramel = [x[0] for x in myresult]
    dishes_count.append(cremCaramel)

    # Get the total counts for Panna Cotta
    sql = "SELECT COUNT(*) FROM Accepted_Orders WHERE Dolce = 'Panna Cotta'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    pannaCotta = [x[0] for x in myresult]
    dishes_count.append(pannaCotta)

    # List containing the values for the dishes
    dishesCount = [x[0] for x in dishes_count]

    # List containing the labels for the dishes
    dishes = ["Pasta Boscaiola", "Risotto allo Zafferano", "Pizza Margherita", "Cotoletta alla milanese", "Tagliata", "Salmone", "Cicoria", "Patatine fritte", "Insalata", "Tiramisù", "Crem Caramel", "Panna Cotta"]

    # Dati da visualizzare
    labels = dishes
    sizes = dishesCount
    colors = ['red', 'blue', 'green', 'orange', 'lightblue', 'purple', 'yellow', 'white', 'black', 'lightgreen', 'brown', 'lightcyan']

    plt.figure(figsize=(12, 10))

    # Creazione del grafico a torta
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

    # Personalizzazione dell'aspetto del grafico
    plt.title("Percentuale vendite", fontsize=14)

    plt.savefig('static/pie_chart.png')

    ###################################

    # Multi-pie chart graph

    # Clear previous figure
    plt.clf()

    # Lists containing the values for the dishes
    dishesCountPrimi = [dishesCount[0], dishesCount[1], dishesCount[2]]
    dishesCountSecondi = [dishesCount[3], dishesCount[4], dishesCount[5]]
    dishesCountContorni = [dishesCount[6], dishesCount[7], dishesCount[8]]
    dishesCountDolci = [dishesCount[9], dishesCount[10], dishesCount[11]]

    # Lists containing the labels for the dishes
    dishesPrimi = ["Pasta Boscaiola", "Risotto allo Zafferano", "Pizza Margherita"]
    dishesSecondi = ["Cotoletta alla milanese", "Tagliata", "Salmone"]
    dishesContorni = ["Cicoria", "Patatine fritte", "Insalata"]
    dishesDolci = ["Tiramisù", "Crem Caramel", "Panna Cotta"]

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # plot pie charts on each subplot using the lists
    axes[0, 0].pie(dishesCountPrimi, labels=dishesPrimi, autopct='%.2f%%', textprops={'fontsize': 8})
    axes[0, 0].set_title("Primi", fontsize=14)
    axes[0, 1].pie(dishesCountSecondi, labels=dishesSecondi, autopct='%.2f%%', textprops={'fontsize': 8})
    axes[0, 1].set_title("Secondi", fontsize=14)
    axes[1, 0].pie(dishesCountContorni, labels=dishesContorni, autopct='%.2f%%', textprops={'fontsize': 8})
    axes[1, 0].set_title("Contorni", fontsize=14)
    axes[1, 1].pie(dishesCountDolci, labels=dishesDolci, autopct='%.2f%%', textprops={'fontsize': 8})
    axes[1, 1].set_title("Dolci", fontsize=14)

    # save the figure
    plt.savefig('static/multi-pie-graph.png')

    return tot


def stats2():
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="restaurant_menu_flask"
    )
    mycursor = mydb.cursor()

    # Define the dishes list
    dishes = ["Pasta Boscaiola", "Risotto allo Zafferano", "Pizza Margherita", "Cotoletta alla milanese", "Tagliata",
              "Salmone", "Cicoria", "Patatine fritte", "Insalata", "Tiramisù", "Crem Caramel", "Panna Cotta"]

    primi = ["Pasta Boscaiola", "Risotto allo Zafferano", "Pizza Margherita"]
    secondi = ["Cotoletta alla milanese", "Tagliata", "Salmone"]
    contorni =["Cicoria", "Patatine fritte", "Insalata"]
    dolci = ["Tiramisù", "Crem Caramel", "Panna Cotta"]

    # Define an empty list to store the values
    values_h = []

    # Loop over the primi list
    for dish in primi:
        # Define the parameterized query
        sql = "SELECT * FROM accepted_orders WHERE Primo = %s"
        # Execute the query with the dish as a parameter
        mycursor.execute(sql, (dish,))
        # Fetch the results
        myresult = mycursor.fetchall()
        # Initialize a sum variable
        sum = 0
        # Loop over the results and add the quantity to the sum
        for x in myresult:
            sum += int(x[6])
        # Append the sum to the values list
        values_h.append(sum)

    # Loop over the secondi list
    for dish in secondi:
        # Define the parameterized query
        sql = "SELECT * FROM accepted_orders WHERE Secondo = %s"
        # Execute the query with the dish as a parameter
        mycursor.execute(sql, (dish,))
        # Fetch the results
        myresult = mycursor.fetchall()
        # Initialize a sum variable
        sum = 0
        # Loop over the results and add the quantity to the sum
        for x in myresult:
            sum += int(x[6])
        # Append the sum to the values list
        values_h.append(sum)

    # Loop over the contorni list
    for dish in contorni:
        # Define the parameterized query
        sql = "SELECT * FROM accepted_orders WHERE Contorno = %s"
        # Execute the query with the dish as a parameter
        mycursor.execute(sql, (dish,))
        # Fetch the results
        myresult = mycursor.fetchall()
        # Initialize a sum variable
        sum = 0
        # Loop over the results and add the quantity to the sum
        for x in myresult:
            sum += int(x[6])
        # Append the sum to the values list
        values_h.append(sum)

    # Loop over the dolci list
    for dish in dolci:
        # Define the parameterized query
        sql = "SELECT * FROM accepted_orders WHERE Dolce = %s"
        # Execute the query with the dish as a parameter
        mycursor.execute(sql, (dish,))
        # Fetch the results
        myresult = mycursor.fetchall()
        # Initialize a sum variable
        sum = 0
        # Loop over the results and add the quantity to the sum
        for x in myresult:
            sum += int(x[6])
        # Append the sum to the values list
        values_h.append(sum)


    # Dati da visualizzare
    categories = dishes
    values = values_h

    # Clear previous figure
    plt.clf()

    plt.figure(figsize=(12, 10))
    # Creazione dell'istogramma
    plt.bar(categories, values)

    # Personalizzazione dell'aspetto del grafico
    plt.title("Vendite per Piatto")
    plt.xlabel("Piatti", fontsize=14)
    plt.ylabel("€", fontsize=14)
    # Set the xtick labels and font size
    plt.xticks(categories, fontsize=8)
    # Rotate the xtick labels by 20 degrees
    plt.tick_params(axis='x', which='major', rotation=20)


    plt.savefig('static/histogram.png')



def stats3():
    global dishesCount
    global dishes




@app.route('/stats', methods=['post'])
def showStats():
    tot = stats1()
    # Clear the current figure
    plt.clf()
    stats2()
    return render_template('stats.html', tot=tot)


@app.route('/admin_login.html')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_area')
def admin_area():
    return render_template('admin_area.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="restaurant_menu_flask"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM restaurant_menu_flask.Manager;")
    myresult = mycursor.fetchall()
    conta = []
    for x in myresult:
        if username not in x and password not in x:
            conta.append("0")
        elif username in x and password in x:
            conta.append("1")
            if conta.count("1") == 1:
                print("Bentornato!")
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=pwd,
                    database="restaurant_menu_flask"
                )
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM Customers")
                myresult = mycursor.fetchall()
                admin_area()
                return render_template('admin_area.html', myresult=myresult)

@app.route('/accettaRifiuta_ordine', methods=['POST'])
def accettaRifiuta_ordine():
    # Get the values of the input fields
    id = request.form.get('id')
    email = request.form.get('email')
    primo = request.form.get('primo')
    secondo = request.form.get('secondo')
    contorno = request.form.get('contorno')
    dolce = request.form.get('dolce')
    price = request.form.get('price')
    accetta = request.form.get('accetta')
    rifiuta = request.form.get('rifiuta')
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="restaurant_menu_flask"
    )
    mycursor = mydb.cursor()
    # Check which button was clicked
    if accetta:
        # Add the id to the database
        sql = "INSERT INTO Accepted_Orders (id, email, primo, secondo, contorno, dolce, price) VALUES (%(id)s, %(email)s, %(primo)s, %(secondo)s, %(contorno)s, %(dolce)s, %(prezzo)s)"
        data = {
            "id": id,
            "email": email,
            "primo": primo,
            "secondo": secondo,
            "contorno": contorno,
            "dolce": dolce,
            "prezzo": price
        }
        mycursor.execute(sql, data)
        mydb.commit()
        # Remove the record with the id from the database
        sql = "DELETE FROM Customers WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        # Send email to customer to confirm order
        subj = "Il suo ordine presso Ristorante Trattoria La Bella Roma"
        body = f"""<p>Gentile Cliente,</p>
        <p>Grazie per il suo ordine!</p>
        <p>Di seguito trova i dettagli di ciò che ha ordinato:</p>
        <ul>
        <li>{primo}</li>
        <li>{secondo}</li>
        <li>{contorno}</li>
        <li>{dolce}</li>
        </ul>
        <p>Il totale è: {price}€</p>
        <p>Il Team di La Bella Roma</p>
        <img class="email-logo" src="cid:email-logo" />
        <p>Questo messaggio e gli eventuali allegati sono destinati esclusivamente al destinatario indicato e possono contenere informazioni confidenziali o riservate. Se avete ricevuto questa mail per errore, vi preghiamo di cancellarla immediatamente e di informare il mittente al seguente indirizzo: trattoria@labellaroma.com. Qualsiasi uso non autorizzato del contenuto di questa mail è vietato e può costituire una violazione della legge.</p>"""
        invia_email(email, subj, body)
    elif rifiuta:
        # Remove the record with the id from the database
        sql = "DELETE FROM Customers WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        # Send email to customer to confirm order
        subj = "Ordine presso Ristorante Trattoria La Bella Roma cancellato"
        body = f"""<p>Gentile Cliente,</p>
        <p>Questa email è per informarla che al momento, data la grande richiesta, <b>non siamo in grado di gestire il suo ordine</b>. Ci scusiamo per il disagio e le auguriamo un buon proseguimento.</p>
        <p>Il Team di La Bella Roma</p>
        <img class="email-logo" src="cid:email-logo" />
        <p>Questo messaggio e gli eventuali allegati sono destinati esclusivamente al destinatario indicato e possono contenere informazioni confidenziali o riservate. Se avete ricevuto questa mail per errore, vi preghiamo di cancellarla immediatamente e di informare il mittente al seguente indirizzo: trattoria@labellaroma.com. Qualsiasi uso non autorizzato del contenuto di questa mail è vietato e può costituire una violazione della legge.</p>"""
        invia_email(email, subj, body)
    # Return a response or redirect
    # Query the database for the updated data
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Customers")
    myresult = mycursor.fetchall()
    admin_area()
    # Render the same template with the updated data
    return render_template('admin_area.html', myresult=myresult)




if __name__ == '__main__':
    app.run()




