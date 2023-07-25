from flask import Flask, request, render_template
import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt




pwd = "your-db-pwd"

"""
Creare una applicazione flask che utilizza i cookie di sessione. In particolare vogliamo registrare di un utente lo username e l’ultimo accesso.
Questi dati vengono registrati in un database. Creare delle statistiche sui dati di accesso dell’utente.
"""




app = Flask(__name__)


def save_data_to_database(username, last_access):
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
        print("Dati salvati correttamente nel database.")
    except mysql.connector.Error as error:
        print("Errore durante il salvataggio dei dati:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        last_access = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_data_to_database(username, last_access)
        return f'Dati salvati con successo per lo username: {username}'
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
plt.ylabel("Accessi")

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

# Mostra il grafico
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

# Mostra il grafico
plt.show()
