from tkinter import *

# This code will make a line in a window

master = Tk()
w = Canvas(master, width=300, height=300)
w.pack()
canvas_height = 150
canvas_width = 150
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()

