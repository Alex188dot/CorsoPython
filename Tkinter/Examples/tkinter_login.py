from tkinter import *
from tkinter import messagebox
import tkinter as tk

master = Tk()

# root window title and dimension
master.title("Login")

# Start code to center the window

width = 600  # Width
height = 300  # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))

# End code to center the window


# adding a label to the root window
lbl1 = Label(master, text="Username: ")
lbl2 = Label(master, text="Password: ")
lbl3 = Label(master)

lbl1.grid()
lbl2.grid()
lbl3.grid()

# adding Entry Field
txt1 = Entry(master, width=10)
txt1.grid(column=1, row=0)
txt2 = Entry(master, show="*", width=10)
txt2.grid(column=1, row=1)
lbl3.grid(column=1, row=2)


# function to display Login successful when
# button is clicked

def show_alert(x):
    messagebox.showinfo("Login", x)


username = "Mario"
password = "Ciao1"


def clicked():
    user1 = txt1.get()
    pwd1 = txt2.get()
    if user1 == username and pwd1 == password:
        res = "Login effettuato con successo"
        lbl3.configure(text=res)
        show_alert(res)
    else:
        res = "Username o password non corretti"
        lbl3.configure(text=res)
        show_alert(res)


button = tk.Button(master, command=show_alert)

# button widget with red color text inside
btn = Button(master, text="Login",
             fg="blue", command=clicked)
# Set Button Grid
btn.grid(column=3, row=4)

# Execute Tkinter
master.mainloop()
