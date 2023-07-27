import tkinter as tk
from tkinter import ttk
from random import choice
from tkinter import messagebox

root = tk.Tk()
root.title("Slot Machine")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)

simboli = ["7️⃣", "🍷", "🍒", "🍋", "🍊", "🍌"]

font_size = 24 * 4 # Multiply by 4 to make symbols bigger

rullo1_label = ttk.Label(frame, font=("Helvetica", font_size))
rullo1_label.grid(row=0, column=0, padx=5, pady=5)

rullo2_label = ttk.Label(frame, font=("Helvetica", font_size))
rullo2_label.grid(row=0, column=1, padx=5, pady=5)

rullo3_label = ttk.Label(frame, font=("Helvetica", font_size))
rullo3_label.grid(row=0, column=2, padx=5, pady=5)

# Chiamata alla funzione inizializza_rulli dopo aver definito le label

def inizializza_rulli():
    global simboli # Uso della variabile globale simboli
    rullo1 = choice(simboli)
    rullo2 = choice(simboli)
    rullo3 = choice(simboli)

    rullo1_label.config(text=rullo1)
    rullo2_label.config(text=rullo2)
    rullo3_label.config(text=rullo3)

inizializza_rulli() # Chiamata alla funzione prima del loop principale


def spin():
    global credito
    global simboli # Uso della variabile globale simboli

    if credito >= 0.50:
        credito -= 0.50
        rullo1 = choice(simboli)
        rullo2 = choice(simboli)
        rullo3 = choice(simboli)

        rullo1_label.config(text=rullo1)
        rullo2_label.config(text=rullo2)
        rullo3_label.config(text=rullo3)

        if rullo1 == rullo2 == rullo3:
            credito += 10.0
            risultato_label.config(text="Hai vinto! Hai ora {} euro di credito.".format(credito))
            messagebox.showinfo("Result", "Complimenti, hai vinto!")
        else:
            risultato_label.config(text="Riprova! Credito rimanente: {} euro.".format(credito))
    else:
        risultato_label.config(text="Credito insufficiente. Ricarica per continuare a giocare.")



# Start code to center the window

def centerWindow(window):
    width = 380  # Width
    height = 300  # Height

    screen_width = window.winfo_screenwidth()  # Width of the screen
    screen_height = window.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


# End code to center the window

centerWindow(root)
credito = 20.0
costo_partita = 0.50


spin_button = ttk.Button(frame, text="Spin (Costo: {} euro)".format(costo_partita), command=spin)
spin_button.grid(row=1, columnspan=3, padx=5, pady=10, sticky="nsew")  # Aggiunto sticky="nsew"

risultato_label = ttk.Label(frame, text="Credito disponibile: {} euro".format(credito), font=("Helvetica", 16), anchor="center")
risultato_label.grid(row=2, columnspan=3, padx=5, pady=5, sticky="nsew")  # Aggiunto sticky="nsew"



root.mainloop()
