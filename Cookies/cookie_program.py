from flask import Flask, request, render_template, make_response
import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt




pwd = "yoour-db-pwd"

"""
Creare una applicazione flask che utilizza i cookie di sessione. In particolare vogliamo registrare di un utente 
lo username e l’ultimo accesso.
Questi dati vengono registrati in un database. Creare delle statistiche sui dati di accesso dell’utente.

Create a flask application that uses session cookies. Specifically we want to register a user's
username and last access.
This data is recorded in a database. Create statistics on user access data.

"""




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register')
def register_page():
    return render_template('registration.html')


def save_data_to_database(username, password, last_access):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=pwd,
            database='Talentform'
        )

        cursor = connection.cursor()
        query = "INSERT INTO users4 (username, password, last_access) VALUES (%s, %s, %s)"
        values = (username, password, last_access)
        cursor.execute(query, values)
        connection.commit()
        print("User succesfully registered.")
    except mysql.connector.Error as error:
        print("Error while saving data:", error)

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
    mycursor.execute("SELECT * FROM Talentform.users4;")
    myresult = mycursor.fetchall()
    conta = []
    for x in myresult:
        if username not in x and password not in x:
            conta.append("0")
        elif username in x and password in x:
            conta.append("1")
            if conta.count("1") == 1:
                # get the cookie value for the username
                cookie_username = request.cookies.get('username')
                # compare it with the form input
                if cookie_username == username:
                    # print a welcome message
                    msg = f"Welcome back {cookie_username}!"
                else:
                    msg = f"Welcome back {username}!"
                # Save access data to the database
                last_access = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                try:
                    connection = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password=pwd,
                        database='Talentform'
                    )
                    cursor = connection.cursor()
                    query = "INSERT INTO users2 (username, last_access) VALUES (%s, %s)"
                    values = (username, last_access)
                    cursor.execute(query, values)
                    connection.commit()
                    print("User access succesfully registered.")
                except mysql.connector.Error as error:
                    print("Error while saving data:", error)
                return render_template('successful_login.html', msg=msg)



@app.route('/registration', methods=['POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        last_access = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=pwd,
            database="Talentform"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT username FROM Talentform.users4;")
        myresult = mycursor.fetchall()
        conta = []
        for x in myresult:
            if username not in x:
                conta.append("0")
            elif username in x:
                conta.append("1")
                if conta.count("1") == 1:
                    msg = f"User {username} already registered!"
                    return render_template('registration.html', msg=msg)
        else:
            # save the data to the database
            save_data_to_database(username, password, last_access)
            # create a response object
            response = make_response(f'{username} succesfully registered!')
            msg = f'{username} succesfully registered!'
            # set a new cookie with the username
            response.set_cookie('username', username)
            # set a new cookie with last_access
            response.set_cookie('last_access', last_access)
            # return the response
            return render_template('successful_registration.html', response=response, msg=msg)
    else:
        return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pwd,
    database="Talentform"
)

# Seleziono tutti gli usernames

mycursor = mydb.cursor()
mycursor.execute("SELECT username FROM users2")
myresult = mycursor.fetchall()

username_list = []
for x in myresult:
    username_list.append(x)

new_username_list = [t[0] for t in username_list]

unique_names = []
for name in new_username_list:
    if name not in unique_names:
        unique_names.append(name)

# Tolgo le parentesi quadre alla lista unique names per inseriral nella query

new_unique_names = str(unique_names).replace('[', '').replace(']', '')

# Seleziono tutte le volte che hanno fatto accesso

mycursor = mydb.cursor()
mycursor.execute(f"""
SELECT username, COUNT(*) AS count FROM users2 WHERE username IN ({new_unique_names}) GROUP BY username ORDER BY count DESC
""")
myresult = mycursor.fetchall()

names = []
count = []

for x in myresult:
    count.append(x[1])

for x in myresult:
    names.append(x[0])

# Dati da visualizzare
categories = names
values = count

# Creazione dell'istogramma
plt.bar(categories, values)

# Personalizzazione dell'aspetto del grafico
plt.title("Accessi per Utente")
plt.xlabel("Utenti")
plt.xticks(rotation=20)
plt.ylabel("Accessi")

# Show graph
plt.show()

# PIE CHART

# Dati da visualizzare
labels = names
sizes = count
colors = ['red', 'blue', 'green', 'orange', 'lightblue', 'purple', 'yellow', 'white', 'black', 'lightgreen', 'brown', 'lightcyan']

# Creazione del grafico a torta
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Personalizzazione dell'aspetto del grafico
plt.title("Accessi per utente in percentuale")

# Show graph
plt.show()




# Terzo grafico

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users2")
myresult = mycursor.fetchall()

time = []
access = []

# Loop through the data and extract the hour and minute from the datetime object
for record in myresult:
    hour = record[2].hour
    minute = record[2].minute
    # Format the time as HH:MM
    time_str = f"{hour:02d}:{minute:02d}"
    # Append the time to the time list
    time.append(time_str)

# Use a dictionary to count the number of occurrences of each time
count = {}
for t in time:
    if t in count.keys():
        count[t] += 1
    else:
        count[t] = 1

for key, value in count.items():
    access.append(value)

# Convert the list to a set to have unique elements
time_set = set(time)
# Convert the set back to a list
time_unique = list(time_set)
# Sort the list using the sorted() function
time_sorted = sorted(time_unique)


# Print the results
#print("Time:", time_sorted)
#print("Access:", access)


# Dati da visualizzare
x = time_sorted
y = access

# Creazione del grafico a linee
plt.plot(x, y)

# Personalizzazione dell'aspetto del grafico
plt.title("Accessi totali al sito per orario")
plt.xlabel("Orario")
plt.ylabel("Accessi")

# Show graph
plt.show()