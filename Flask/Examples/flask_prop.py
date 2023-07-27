from flask import Flask


class oggetto:
   x = 5

   def __str__(self):
    return f"Oggetto semplice con valore: {self.x} "
app = Flask(__name__)

# prop = oggetto.x
# print(prop)
# prop2 = 6

prop3 = int(input("Inserisci un numero: "))
prop4 = int(input("Inserisci un altro numero: "))

@app.route("/")
def home():
   return f"Il valore della somma è: {prop3 + prop4}"

if __name__ == "__main__":
    app.run()