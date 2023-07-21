import mysql.connector
from flask import Flask, render_template, request

pwd = "your-db-password"

"""
Creare un file html con 4 select che rappresentano le scelte degli utenti per un ristorante.
Le select rappresentano il primo, il secondo, il contorno e il dolce.
Ogni select avrà valori diversi per il primo es. “lasagna”, “risotto” etc
per il secondo “cotoletta”, “spigola” etc.
"""


class Piatto:
    def __init__(self,id, prezzo):
        self.prezzo = prezzo
        self.id = id

    def __str__(self):
        return f"{self.prezzo}"

# Primi
pastaBoscaiola = Piatto(1, 12)
risotto = Piatto(2, 10)
pizzaMargherita = Piatto(3, 8)

# Secondi
cotoletta = Piatto(1, 11)
tagliata = Piatto(2, 15)
salmone = Piatto(3, 14)

# Contorni
cicoria = Piatto(1, 6)
patatine = Piatto(2, 5)
insalata = Piatto(3, 7)

# Dolci
tiramisu = Piatto(1, 6)
cremcaramel = Piatto(2, 6)
pannacotta = Piatto(3, 6)

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

# Created Customers Table and added Email, Choice and Price columns
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


# Codice per ottenere le opzioni dall'HTML
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('select.html')

@app.route('/stamp', methods=['POST'])
def stamp():
    opzione1_selezionata = request.form['opzione1']
    opzione2_selezionata = request.form['opzione2']
    return f"Hai selezionato le opzioni: {opzione1_selezionata}, {opzione2_selezionata}"

if __name__ == '__main__':
    app.run()
"""
# Codice HTML
"""
<!DOCTYPE html>
<html>
<head>
    <title>Selezione Opzioni</title>
</head>
<body>
    <h2>Seleziona due opzioni:</h2>
    <form action="/stamp" method="post">
        <label for="opzione1">Opzione 1:</label>
        <select name="opzione1" id="opzione1">
            <option value="opzione1">Opzione 1</option>
            <option value="opzione2">Opzione 2</option>
            <option value="opzione3">Opzione 3</option>
        </select>
        <br>
        <label for="opzione2">Opzione 2:</label>
        <select name="opzione2" id="opzione2">
            <option value="opzioneA">Opzione A</option>
            <option value="opzioneB">Opzione B</option>
            <option value="opzioneC">Opzione C</option>
        </select>
        <br>
        <input type="submit" value="Invia">
    </form>
</body>
</html>
"""


