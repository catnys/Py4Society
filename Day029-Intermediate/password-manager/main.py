from tkinter import *

window = Tk()
window.title('Password Manager')
window.geometry('700x700')
window.config(padx=10, pady=10)

# Canvas
canvas = Canvas(window, width=500, height=500)
logo = PhotoImage(file='logo.png')
canvas.create_image(250, 250, image=logo)
canvas.grid(row=0, column=0, columnspan=2)  # Using grid instead of pack

# Labels
websiteLabel = Label(window, text='Website')
websiteLabel.config(font=('Calibri', 20))
websiteLabel.grid(row=1, column=0)

emailLabel = Label(window, text='Email')
emailLabel.config(font=('Calibri', 20))
emailLabel.grid(row=2, column=0)

passwordLabel = Label(window, text='Password')
passwordLabel.config(font=('Calibri', 20))
passwordLabel.grid(row=3, column=0)

# Run the Tkinter event loop
window.mainloop()
