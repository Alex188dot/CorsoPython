import matplotlib.pyplot as plt

# Dati da visualizzare
categories = ['A', 'B', 'C', 'D', 'E']
values = [15, 25, 30, 10, 20]

# Creazione dell'istogramma
plt.bar(categories, values)

# Personalizzazione dell'aspetto del grafico
plt.title("Istogramma")
plt.xlabel("Categorie")
plt.ylabel("Valori")

# Mostra il grafico
plt.show()