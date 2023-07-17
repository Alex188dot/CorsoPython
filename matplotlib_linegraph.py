import matplotlib.pyplot as plt

# Dati da visualizzare
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Creazione del grafico a linee
plt.plot(x, y)

# Personalizzazione dell'aspetto del grafico
plt.title("Grafico a linee")
plt.xlabel("X")
plt.ylabel("Y")

# Mostra il grafico
plt.show()