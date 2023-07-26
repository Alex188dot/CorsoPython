from flask import Flask, render_template, request, redirect, make_response
import mysql.connector
import datetime
from datetime import datetime
from datetime import date
import collections
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

pwd = 'your-db-pwd'





"""

Esercizio supermarket

Creare un programma supermarketFlask che rappresenta la gestione di un supermercato online. Inizialmente creare l’interfaccia per l’utente: l’utente può scegliere tra 4 select prodotti da banco, prodotti freschi, prodotti da frigo, inoltre nell’ultima select  possiamo scegliere tra vari elettrodomestici. In questo programma l’utente può anche scegliere di non selezionare alcuni prodotti (stringa vuota o null). Inoltre una volta effettuato l’ordine il programma va a scrivere su una tabella mysql i dati. ATTENZIONE: tra i dati sono presenti la mail e la password dell’utente, e quindi i relativi cookie dei dati di sessione.


"""






class Prodotto:
    def __init__(self, id, prezzo):
        self.id = id
        self.prezzo = prezzo


    def __str__(self):
        return f"{self.prezzo}"

# Prodotti confezionati
pasta = Prodotto(1, 1)
riso = Prodotto(2, 1.5)
paneInCassetta = Prodotto(3, 1.2)

# Prodotti freschi
lattuga = Prodotto(4, 1.2)
cetrioli = Prodotto(5, 1.3)
carne = Prodotto(6, 8)

# Prodotti da frigo
ricotta = Prodotto(7, 4)
provola = Prodotto(8, 3.5)
latte = Prodotto(9, 1.5)

# Elettrodomestici
ferroDaStiro = Prodotto(10, 35)
lavatrice = Prodotto(11, 350)
asciugaCapelli = Prodotto(12, 49)

sceltaNulla = Prodotto(0, 0)

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('flask_supermarket_login.html')

@app.route('/register')
def register_page():
    return render_template('flask_supermarket_register.html')
@app.route('/admin_login')
def admin_login():
    return render_template('flask_supermarket_admin_login.html')

@app.route('/admin_area', methods=['POST'])
def admin_area():
    username = request.form['username']
    password = request.form['password']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="Talentform"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Talentform.admin;")
    myresult = mycursor.fetchall()
    conta = []
    for x in myresult:
        if username not in x and password not in x:
            conta.append("0")
        elif username in x and password in x:
            conta.append("1")
            if conta.count("1") == 1:

                # Calculate today's revenue

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=pwd,
                    database="Talentform"
                )
                mycursor = mydb.cursor()

                # Get the current date as a string in the format YYYY-MM-DD
                today = datetime.today().strftime("%Y-%m-%d")

                # Execute the SQL query with the WHERE clause
                mycursor.execute(f"SELECT totale FROM prodotti_scelti WHERE last_access LIKE '{today}%';")
                myresult = mycursor.fetchall()
                totale = []
                for x in myresult:
                    totale.append(x[0])
                incassi = sum(totale)


                # Format today's date to include in the HTML
                today_formatted = datetime.today().strftime("%d-%m-%Y")

                # First graph - Calculate when there are most accesses to the website

                mycursor = mydb.cursor()
                mycursor.execute("SELECT last_access FROM prodotti_scelti;")
                myresult = mycursor.fetchall()
                new_result = []
                for row in myresult:
                    dt_tuple = row
                    dt_obj = dt_tuple[0]
                    # Format it into a string with the desired components separated by commas
                    dt_str = dt_obj.strftime("%Y,%m,%d,%H,%M,%S")
                    # Split the string into a list of its components
                    dt_list = dt_str.split(",")
                    # Convert each element of the list into an integer
                    dt_int = map(int, dt_list)
                    # Convert the list into a tuple
                    final_tuple = tuple(dt_int)
                    new_result.append(final_tuple)

                # Create an empty list to store the hours
                hours = []

                # Loop through each row in myresult
                for row in new_result:
                    # Create a datetime object from the tuple elements
                    last_access = datetime(row[0], row[1], row[2], row[3], row[4], row[5])
                    # Get the hour component and append it to the list
                    if last_access.date() == date.today():
                        # Get the hour component and append it to the list
                        hours.append(last_access.hour)

                # Create a Counter object from the list
                counter = collections.Counter(hours)
                # Get a list of the counts
                counts = list(counter.values())
                # Create a set object from the list
                myset = set(hours)
                # Convert the set object to a list
                unique = list(myset)



                # Pie chart graph: purchases per hour in percentages

                # Clear previous figure
                plt.clf()

                # Create new figure
                plt.figure(figsize=(12, 10))

                # Personalizzazione dell'aspetto del grafico
                plt.title("Acquisti per ora della giornata in percentuale")

                # Dati da visualizzare
                labels = unique
                sizes = counts
                colors = ['red', 'blue', 'green', 'orange', 'lightblue', 'purple', 'yellow', 'white', 'black', 'lightgreen', 'brown', 'lightcyan']

                # Creazione del grafico a torta
                plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

                plt.savefig('static/purchases_per_hour_piechart.png')


                # Second graph: linegraph

                # Clear previous figure
                plt.clf()

                # Dati da visualizzare
                x = unique
                y = counts

                # Creazione del grafico a linee
                plt.plot(x, y)

                # Personalizzazione dell'aspetto del grafico
                plt.title("Acquisti per ora della giornata")
                plt.xlabel("Orario (24h)", fontsize=14)
                plt.ylabel("N. Acquisti", fontsize=14)
                # Set the tick locations and labels on the x-axis (9-22)
                plt.xticks(range(9, 23))

                # Mostra il grafico
                plt.savefig('static/purchases_per_hour_linegraph.png')



                return render_template('flask_supermarket_admin_area.html', today_formatted=today_formatted, incassi=incassi)





@app.route('/registrate', methods=['POST'])
def registration():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=pwd,
            database='Talentform'
        )
        cursor = connection.cursor()
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        last_access = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO users3 (email, username, password, last_access) VALUES (%(email)s, %(username)s, %(password)s, %(last_access)s)"
        values = {
            "email": email,
            "username": username,
            "password": password,
            "last_access": last_access
        }
        cursor.execute(query, values)
        connection.commit()
        print("Dati salvati correttamente nel database.")
        msg = "Registrazione effettuata con successo"
        response = make_response(redirect('/', code=302))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        response.set_cookie('last_access_time', datetime.now().isoformat())
        return response
    except mysql.connector.Error as error:
        print("Errore durante il salvataggio dei dati:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return render_template('flask_supermarket_login.html', msg=msg)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="Talentform"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Talentform.users3;")
    myresult = mycursor.fetchall()
    conta = []
    for x in myresult:
        if username not in x and password not in x:
            conta.append("0")
        elif username in x and password in x:
            conta.append("1")
            if conta.count("1") == 1:
                # Read the existing cookie, if present
                last_access_time = request.cookies.get('last_access_time')
                msg = f"Bentornato {username}! Scegli tra i prodotti disponibili per la tua spesa a domicilio: "
                return render_template('flask_supermarket_choose_product.html', msg=msg, last_access_time=last_access_time)
            #elif conta.count("1") == 0:
                #msg = "Username or password not valid"
                #return render_template('flask_supermarket_login.html', msg=msg)

@app.route('/order', methods=['POST'])
def order():
    cart = []
    confezionati = request.form['confezionati']
    freschi = request.form['freschi']
    frigo = request.form['frigo']
    elettrodomestici = request.form['elettrodomestici']
    if confezionati == "0":
        confezionati = ""
        cart.append(int(sceltaNulla.prezzo))
    elif confezionati == "1":
        confezionati = "Pasta"
        cart.append(int(pasta.prezzo))
    elif confezionati == "2":
        confezionati = "Riso"
        cart.append(int(riso.prezzo))
    elif confezionati == "3":
        confezionati = "Pane in cassetta"
        cart.append(int(paneInCassetta.prezzo))
    if freschi == "4":
        freschi = "Lattuga"
        cart.append(int(lattuga.prezzo))
    elif freschi == "5":
        freschi = "Cetrioli"
        cart.append(int(cetrioli.prezzo))
    elif freschi == "6":
        freschi = "Carne"
        cart.append(int(carne.prezzo))
    elif freschi == "0":
        freschi = ""
        cart.append(int(sceltaNulla.prezzo))
    if frigo == "7":
        frigo = "Ricotta"
        cart.append(int(ricotta.prezzo))
    elif frigo == "8":
        frigo = "Provola"
        cart.append(int(provola.prezzo))
    elif frigo == "9":
        frigo = "Latte"
        cart.append(int(latte.prezzo))
    elif frigo == "0":
        frigo = ""
        cart.append(int(sceltaNulla.prezzo))
    if elettrodomestici == "10":
        elettrodomestici = "Ferro da Stiro"
        cart.append(int(ferroDaStiro.prezzo))
    elif elettrodomestici == "11":
        elettrodomestici = "Lavatrice"
        cart.append(int(lavatrice.prezzo))
    elif elettrodomestici == "12":
        elettrodomestici = "Asciuga Capelli"
        cart.append(int(asciugaCapelli.prezzo))
    elif elettrodomestici == "0":
        elettrodomestici = ""
        cart.append(int(sceltaNulla.prezzo))
    prezzo = sum(cart)
    ordine = f"La sua spesa: {confezionati}, {freschi}, {frigo}, {elettrodomestici}. Il totale è: {prezzo}€"
    # This code will add the order to the DB
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="Talentform"
    )
    mycursor = mydb.cursor()
    username = request.cookies.get('username')
    email = request.cookies.get('email')
    last_access = datetime.now().isoformat()
    sql = "INSERT INTO prodotti_scelti (confezionati, freschi, frigo, elettrodomestici, username, email, totale, last_access) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (confezionati, freschi, frigo, elettrodomestici, username, email, prezzo, last_access)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Scelta registrata")
    return render_template('flask_supermarket_order.html', ordine=ordine)








if __name__ == "__main__":
    app.run(debug=True)
