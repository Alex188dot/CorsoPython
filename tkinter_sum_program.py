"""
Scrivere una interfaccia grafica che ha due entry, un bottone e una etichetta. Il programma chiede di inserire due numeri e modifica il testo dell'etichetta con la somma dei due numeri. Attenzione: il metodo get() delle entry ritorna una stringa quindi è necessario fare il cast
La somma viene restituita alla pressione del pulsante
"""

from tkinter import *

master = Tk()

# root window title and dimension
master.title("Sum Calculator")
# Set geometry(widthxheight)

width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))


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


# function to display user text when
# button is clicked
def clicked():
    res = f"Total: {int(txt1.get()) + int(txt2.get())}"
    lbl3.configure(text=res)


# button widget with red color text inside
btn = Button(master, text="Sum",
             fg="blue", command=clicked)
# Set Button Grid
btn.grid(column=3, row=4)

# Execute Tkinter
master.mainloop()