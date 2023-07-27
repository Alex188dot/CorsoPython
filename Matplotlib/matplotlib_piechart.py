import matplotlib.pyplot as plt

# Dati da visualizzare
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 15, 30]
colors = ['red', 'blue', 'green', 'orange']

# Creazione del grafico a torta
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Personalizzazione dell'aspetto del grafico
plt.title("Grafico a torta")

# Mostra il grafico
plt.show()