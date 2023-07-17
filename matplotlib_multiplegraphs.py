import matplotlib.pyplot as plt

# Dati per i grafici
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 8, 27, 64]
y3 = [1, 2, 3, 4]
y4 = [4, 3, 2, 1]

# Crea la figura e la griglia di subplot
fig, axes = plt.subplots(2, 2)

# Traccia il primo grafico nel subplot (0, 0)
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Grafico 1")

# Traccia il secondo grafico nel subplot (0, 1)
axes[0, 1].plot(x, y2)
axes[0, 1].set_title("Grafico 2")

# Traccia il terzo grafico nel subplot (1, 0)
axes[1, 0].plot(x, y3)
axes[1, 0].set_title("Grafico 3")

# Traccia il quarto grafico nel subplot (1, 1)
axes[1, 1].plot(x, y4)
axes[1, 1].set_title("Grafico 4")

# Regola la disposizione dei subplot
plt.tight_layout()

# Mostra l'immagine con i subplot
plt.show()