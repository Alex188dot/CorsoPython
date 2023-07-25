from flask import Flask, request, render_template, make_response
import mysql.connector
from datetime import datetime

pwd = 'your-db-pwd'



"""

Esercizio supermarket

Creare un programma supermarketFlask che rappresenta la gestione di un supermercato online. Inizialmente creare l’interfaccia per l’utente: l’utente può scegliere tra 4 select prodotti da banco, prodotti freschi, prodotti da frigo, inoltre nell’ultima select  possiamo scegliere tra vari elettrodomestici. In questo programma l’utente può anche scegliere di non selezionare alcuni prodotti (stringa vuota o null). Inoltre una volta effettuato l’ordine il programma va a scrivere su una tabella mysql i dati. ATTENZIONE: tra i dati sono presenti la mail e la password dell’utente, e quindi i relativi cookie dei dati di sessione.


"""






app = Flask(__name__)




@app.route('/')
def index():
    return render_template('flask_supermarket_login.html')

@app.route('/register')
def register_page():
    return render_template('flask_supermarket_register.html')


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
        query = "INSERT INTO users3 (email, username, password, last_access) VALUES (%s, %s, %s, %s)"
        values = (email, username, password, last_access)
        cursor.execute(query, values)
        connection.commit()
        print("Dati salvati correttamente nel database.")
        msg = "Registrazione effettuata con successo"
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
                print("Bentornato!")
                return render_template('flask_supermarket_choose_product.html')
            #elif conta.count("1") == 0:
                #msg = "Username or password not valid"
                #return render_template('flask_supermarket_login.html', msg=msg)




if __name__ == "__main__":
    app.run(debug=True)
