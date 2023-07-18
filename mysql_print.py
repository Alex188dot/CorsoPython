import mysql.connector
pwd = "your-password"

# Per stampare tutti gli elementi di customers

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="Talentform"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#################################################

# Per stampare tutti i campi della colonna name

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#################################################


# Per stampare nome specifico, tutti i record

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE name ='Luigi'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#################################################