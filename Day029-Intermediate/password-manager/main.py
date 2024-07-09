from tkinter import *

from bokeh.models import canvas

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.geometry('500x500')
window.config(padx=10, pady=10)

canvas = Canvas(width=500, height=500)
logo = PhotoImage(file='logo.png')
canvas.create_image(250, 250, image=logo)
canvas.pack()




window.mainloop()



