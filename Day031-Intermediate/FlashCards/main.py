from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
cardFrontImg = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=cardFrontImg)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic", "underline"), fill="black")
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0)

wrongImg = PhotoImage(file="images/wrong.png")
unknownButton = Button(image=wrongImg, highlightthickness=0)
unknownButton.grid(row=1, column=0)

checkImg = PhotoImage(file="images/right.png")
checkButton = Button(image=checkImg, highlightthickness=0)
checkButton.grid(row=1, column=1)

window.mainloop()
