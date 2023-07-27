import mysql.connector
pwd = "your-password"




"""

scrivere un programma che chiede all'utente di inserire username e password e li va a registrare in una tabella 
creata ad hoc. Il programma se l'utente è già presente nella tabella stampa bentornato  lo username altrimenti 
stampa registrazione avvenuta con successo. Attenzione: se l'utente è già presente nella tabella non deve essere 
registrato due volte.

"""
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd
)
"""
"""
# Created new database user_access
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE user_access")

print(mydb)
"""

"""
# Created Customers Table and added Username and Pwd columns 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="user_access"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customers (Username VARCHAR(255), Pwd VARCHAR(255))")
"""



inp = input("Benvenuto nel programma di Gestione Database, premere invio per continuare")

while inp != "0":
    inp = input("Inserire Username, oppure 0 per uscire: ")
    inp2 = input("Inserire Password, oppure 0 per uscire: ")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="user_access"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM user_access.Customers;")
    myresult = mycursor.fetchall()
    conta = []
    for x in myresult:
        if inp not in x and inp2 not in x:
            conta.append("0")
        elif inp in x and inp2 in x:
            conta.append("1")
            if conta.count("1") == 1:
                print("Bentornato!")
    if conta.count("1") == 0:
        sql = "INSERT INTO Customers (Username, Pwd) VALUES (%s, %s)"
        val = (inp, inp2)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
