from tkinter import messagebox
import tkinter as tk

def show_alert():
    messagebox.showinfo("Alert", "Questo è un messaggio di alert!")

# Creazione della finestra principale
window = tk.Tk()
window.title("Alert example")
window.geometry('300x150')

# Creazione di un pulsante per mostrare l'alert
button = tk.Button(window, text="Mostra Alert", command=show_alert)
button.pack()

# Esecuzione del main loop della finestra
window.mainloop()