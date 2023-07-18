import mysql.connector
pwd = "your-password"

"""
# Connessione generica a MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pwd"
)

print(mydb)
"""


"""
## Per creare Database tramite Python
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Talentform")
######
"""


"""
## Per stampare tutti i Database che abbiamo in memoria
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
######
"""
"""
# Per connettersi ad un database specifico e inserire tabella con colonne
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pwd",
  database="Talentform"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customers (Name VARCHAR(255), Address VARCHAR(255))")
"""



"""
# Qui mischiamo codice Python con codice SQL. %s si chiama s-string

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pwd",
  database="Talentform"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Customers (Name, Address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
"""

"""
Scriviamo un programma che in maniera iterativa se l'utente preme 1 chiede all'utente di inserire nome e indirizzo. Il programma prevede che il nome e l'ndirizzo vengano scritti all'interno della tabella customers. quando l'utente preme 0 il programma termina
"""


inp = input("Benvenuto nel programma di Gestione Database, premere invio per continuare")

while inp != "0":
    inp = input("Inserire Nome e Cognome da inserire nel Database, oppure 0 per uscire: ")
    if inp == "0":
        break
    inp2 = input("Inserire Indirizzo da inserire nel Database, oppure 0 per uscire: ")
    if inp2 == "0":
        break

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="Talentform"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO Customers (Name, Address) VALUES (%s, %s)"
    val = (inp, inp2)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
