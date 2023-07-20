"""
Creiamo una applicazione che chiede all'utente nome e passowrd (tramite un form html) Impostare user e password già all'inizio. Successivamente il programma se queste variabili vengono riconosciute stampa benvenuto e il nome dell'user altrimenti stampa utente non ricnosciuto

"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login1.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return render_template('profile2.html', username=username, password=password)

if __name__ == '__main__':
    app.run(debug=True)