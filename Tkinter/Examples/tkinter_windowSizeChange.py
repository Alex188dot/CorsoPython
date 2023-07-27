# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Benvenuti al Corso Python")
# Set geometry (widthxheight)
root.geometry('700x400')

# adding a label to the root window
lbl = Label(root, text="Are you a developer?")
lbl.grid()

# all widgets will be here
# Execute Tkinter
root.mainloop()