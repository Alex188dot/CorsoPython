from flask import Flask, render_template, request

"""
Inizializza una lista di user arbitrari ("Rossi" "Bianchi" etc...). Dopo aver reso il login va a leggere lo user inserito e se non lo trova nella lista lo aggiunge, altrimenti la lista rimane invariata. Infine passiamo la lista e la stampiamo per bene all'interno della pagina html

"""

app = Flask(__name__)

utenti = []
utenti.append("Rossi")
utenti.append("Bianchi")
print(utenti)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    for user in utenti:
        if username == user:
            return render_template('profile3.html', utenti=utenti)
        else:
            utenti.append(username)
            return render_template('profile3.html', utenti=utenti)

if __name__ == '__main__':
    app.run(debug=True)