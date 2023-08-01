"""
Scrivere una interfaccia grafica che ha due entry, un bottone e una etichetta. Il programma chiede di inserire due
numeri e modifica il testo dell'etichetta con la somma dei due numeri. Attenzione: il metodo get() delle entry ritorna
una stringa quindi è necessario fare il cast.
La somma viene restituita alla pressione del pulsante.
"""

from tkinter import *
from tkinter import messagebox
import tkinter as tk

master = Tk()

# root window title and dimension
master.title("Calculator")

# Start code to center the window

width = 300  # Width
height = 150  # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))

# End code to center the window


# adding a label to the root window
lbl1 = Label(master, text="First Number: ")
lbl2 = Label(master, text="Second Number: ")
lbl3 = Label(master)

lbl1.grid()
lbl2.grid()
lbl3.grid()

# adding Entry Field
txt1 = Entry(master, width=10)
txt1.grid(column=1, row=0)
txt2 = Entry(master, width=10)
txt2.grid(column=1, row=1)
lbl3.grid(column=1, row=2)


# function to display total when
# button is clicked

def show_alert(x):
    messagebox.showinfo(f"Total:", x)


def sum():
    somma = int(txt1.get()) + int(txt2.get())
    res = f"Total: {somma}"
    lbl3.configure(text=res)
    show_alert(somma)


def divide():
    div = int(txt1.get()) / int(txt2.get())
    res = f"Total: {div}"
    lbl3.configure(text=res)
    show_alert(div)


def multiply():
    mult = int(txt1.get()) * int(txt2.get())
    res = f"Total: {mult}"
    lbl3.configure(text=res)
    show_alert(mult)


def subtract():
    sub = int(txt1.get()) - int(txt2.get())
    res = f"Total: {sub}"
    lbl3.configure(text=res)
    show_alert(sub)


button = tk.Button(master, command=show_alert)

# button widget with red color text inside
btn1 = Button(master, text="+", fg="blue", command=sum)
btn2 = Button(master, text="/", fg="blue", command=divide)
btn3 = Button(master, text="*", fg="blue", command=multiply)
btn4 = Button(master, text="-", fg="blue", command=subtract)

# Configure column 0 and 1 to expand and fill any extra space
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)

# Place the buttons in columns 0 and 1
btn1.grid(column=0, row=4, sticky="nsew")
btn2.grid(column=1, row=4, sticky="nsew")
btn3.grid(column=0, row=6, sticky="nsew")
btn4.grid(column=1, row=6, sticky="nsew")

# Execute Tkinter
master.mainloop()
