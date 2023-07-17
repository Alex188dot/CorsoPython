from tkinter import *
from tkinter import messagebox
import tkinter as tk


class Conto:
    def __init__(self, id, saldo):
        self.saldo = saldo
        self.id = id


class Mach:
    def __init__(self, conti):
        self.conti = conti

    def erogaCa(self, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo >= 2:
                    i.saldo -= 2
                    stringa = "Erogazione in corso"
                else:
                    stringa = "Credito insufficiente"
                return [stringa, i.saldo]

    def erogaThe(self, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo >= 3:
                    i.saldo -= 3
                    stringa = "Erogazione in corso"
                else:
                    stringa = "Credito insufficiente"
                return [stringa, i.saldo]

    def erogaCiok(self, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo >= 3.50:
                    i.saldo -= 3.50
                    stringa = "Erogazione in corso"
                else:
                    stringa = "Credito insufficiente"
                return [stringa, i.saldo]

    def erogaW(self, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo >= 1.50:
                    i.saldo -= 1.50
                    stringa = "Erogazione in corso"
                else:
                    stringa = "Credito insufficiente"
                return [stringa, i.saldo]

    def addMoney(self, id, importo):
        for i in self.conti:
            if i.id == id:
                    i.saldo += importo
                    stringa = "Ricarica effettuata con successo!"
                    return [stringa, i.saldo]

c1 = Conto("01", 20)
c2 = Conto("02", 10)
c3 = Conto("03", 10)
lista = []
lista.append(c1)
lista.append(c2)
lista.append(c3)
m1 = Mach(lista)






# GUI code starts here


master = Tk()

# root window title and dimension
master.title("Login")


# Start code to center the window

def centerWindow(window):
    width = 600  # Width
    height = 300  # Height

    screen_width = window.winfo_screenwidth()  # Width of the screen
    screen_height = window.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


# End code to center the window

centerWindow(master)

# adding a label to the root window
lbl1 = Label(master, text="Inserire ID chiavetta: ")
lbl3 = Label(master)

lbl1.grid()
lbl3.grid()

# adding Entry Field
txt1 = Entry(master, show="*", width=10)
txt1.grid(column=1, row=0)
lbl3.grid(column=1, row=2)


# function to display Login successful when
# button is clicked

def show_login(x):
    messagebox.showinfo("Login", x)

def show_alert(x):
    messagebox.showinfo("Result", x)

def clicked():
    id1 = txt1.get()
    for el in m1.conti:
        if id1 == el.id:
            res = "Login effettuato con successo"
            lbl3.configure(text=res)
            show_login(res)
            # open a new window
            new_window = tk.Toplevel(master)
            new_window.title("Nuova Finestra")
            centerWindow(new_window)

            def coffee():
                c = m1.erogaCa(id1)
                stringa = c[0]
                saldo = f"Saldo rimanente: {c[1]}€"
                show_alert(stringa)
                show_alert(saldo)

            def tea():
                t = m1.erogaThe(id1)
                stringa = t[0]
                saldo = f"Saldo rimanente: {t[1]}€"
                show_alert(stringa)
                show_alert(saldo)

            def chocolate():
                ch = m1.erogaCiok(id1)
                stringa = ch[0]
                saldo = f"Saldo rimanente: {ch[1]}€"
                show_alert(stringa)
                show_alert(saldo)

            def water():
                w = m1.erogaW(id1)
                stringa = w[0]
                saldo = f"Saldo rimanente: {w[1]}€"
                show_alert(stringa)
                show_alert(saldo)


            def topUp():
                new_window2 = tk.Toplevel(master)
                new_window2.title("Nuova Finestra importo")
                centerWindow(new_window2)

                # adding a label to the root window
                lblImporto = Label(new_window2, text="Inserire l'importo da ricaricare: ")
                lbl3Ricevuta = Label(new_window2)

                lblImporto.grid()
                lbl3Ricevuta.grid()

                # adding Entry Field
                txtM = Entry(new_window2, width=10)
                txtM.grid(column=1, row=0)
                lbl3.grid(column=1, row=2)

                def money():
                    topUp1 = m1.addMoney(id1, int(txtM.get()))
                    stringa = f"{topUp1[0]}"
                    saldo = f"Saldo rimanente: {topUp1[1]}€"
                    show_alert(stringa)
                    show_alert(saldo)

                btn6 = Button(new_window2, text="Done",
                          fg="blue", command=money)
                btn6.place(relx=0.5, rely=0.5, anchor=CENTER)

                centerWindow(new_window2)

            btn1 = Button(new_window, text="Coffee ☕️",
                          fg="blue", command=coffee)
            btn2 = Button(new_window, text="Tea 🫖",
                          fg="blue", command=tea)
            btn3 = Button(new_window, text="Chocolate 🍫",
                          fg="blue", command=chocolate)
            btn4 = Button(new_window, text="Water 🚰",
                          fg="blue", command=water)
            btn5 = Button(new_window, text="Top up 💰",
                          fg="blue", command=topUp)
            btn1.place(relx=0.5, rely=0.15, anchor=CENTER)
            btn2.place(relx=0.5, rely=0.30, anchor=CENTER)
            btn3.place(relx=0.5, rely=0.45, anchor=CENTER)
            btn4.place(relx=0.5, rely=0.6, anchor=CENTER)
            btn5.place(relx=0.5, rely=0.75, anchor=CENTER)

            new_window.mainloop()


button = tk.Button(master, command=show_alert)

# button widget with red color text inside
btn = Button(master, text="Login",
             fg="blue", command=clicked)
# Set Button Grid
btn.grid(column=3, row=4)

# Execute Tkinter
master.mainloop()
