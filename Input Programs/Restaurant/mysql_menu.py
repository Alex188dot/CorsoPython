import mysql.connector

pwd = "your-db-pwd"

"""
Creiamo una classe menu che ha un prezzo a seconda che il menu sia di pesce, carne o da bambini. 
Il programma chiede all’utente quale menu desidera ordinare e dopo aver chiesto la mail dell’utente 
va a registrare su una tabella con database dedicato il tipo di menu, la mail del cliente e il prezzo del menu. 
Quando il programma termina, (l’utente preme 0) il programma stampa tutti gli ordini effettuati presenti sulla tabella, 
e il totale dell’incasso (somma dei prezzi presenti nella tabella)

Let's create a menu class that has a price according to whether the meal chosen is fish, meat or children's.
The program asks the user which meal they want to order and after asking for the user's email,
it records the meal type, the customer's email and the price of the meal on a table in a dedicated database.
When the program ends (the user presses 0), it prints to the console all the orders on the db,
and the total revenue (sum of the prices on the table)


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

