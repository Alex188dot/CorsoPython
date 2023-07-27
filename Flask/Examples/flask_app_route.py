from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/hello")
def pag():
    return 'pagina due'

if __name__ == "__main__":
    app.run()