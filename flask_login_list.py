from flask import Flask, render_template, request
import mysql.connector

pwd = "your-db-pwd"

"""
1) Inizializza una lista di user arbitrari ("Rossi" "Bianchi" etc...). Dopo aver reso il login va a leggere lo user inserito e se non lo trova nella lista lo aggiunge, altrimenti la lista rimane invariata. Infine passiamo la lista e la stampiamo per bene all'interno della pagina html

2) Fai la stessa cosa ma il controllo questa volta tramite lista proveniente da database

"""
# 1)
"""
app = Flask(__name__)

utenti = []
utenti.append("Rossi")
utenti.append("Bianchi")

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    if username in utenti:
        return render_template('profile3.html', utenti=utenti)
    else:
        utenti.append(username)
        return render_template('profile3.html', utenti=utenti)


if __name__ == '__main__':
    app.run(debug=True)

"""

# 2)

"""
# Created new database flask_login
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE flask_login")

print(mydb)
"""

# Created Users Table and added Username column
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="flask_login"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Users (Id INT AUTO_INCREMENT PRIMARY KEY, Username VARCHAR(255))")
"""
# Manually inserted "Rossi" and "Bianchi" under Users, in Workbench

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="flask_login"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Username FROM flask_login.Users")
    myresult = mycursor.fetchall()
    print(myresult)
    myresult = [x[0].strip("()'") for x in myresult]
    print(myresult)
    if username in myresult:
        return render_template('profile3.html', myresult=myresult)
    else:
        sql = "INSERT INTO Users (Username) VALUES ('{}')".format(username)
        mycursor.execute(sql)
        mydb.commit()
        myresult.append(username)
        print(mycursor.rowcount, "Utente registrato")
        return render_template('profile3.html', myresult=myresult)


if __name__ == '__main__':
    app.run(debug=True)
