import tkinter as tk
from tkinter import ttk

def mostra_selezione():
    valore_selezionato = combobox.get()
    print("Valore selezionato:", valore_selezionato)

root = tk.Tk()

# Esempio di creazione di una ttk.Combobox
valori = ["Opzione 1", "Opzione 2", "Opzione 3"]
combobox = ttk.Combobox(root, values=valori)
combobox.pack()

# Pulsante per mostrare il valore selezionato
mostra_pulsante = ttk.Button(root, text="Mostra Selezione", command=mostra_selezione)
mostra_pulsante.pack()

root.mainloop()