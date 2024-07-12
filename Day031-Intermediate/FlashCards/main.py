from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Methods

# Load data
data = pd.read_csv("data/words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=cardFrontImg)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=cardBackImg)


def is_known():
    to_learn.remove(current_card)
    next_card()


# Main

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# flip card
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
cardFrontImg = PhotoImage(file="images/card_front.png")
cardBackImg = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=cardFrontImg)
card_background = canvas.create_image(400, 263, image=cardFrontImg)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic", "underline"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

wrongImg = PhotoImage(file="images/wrong.png")
unknownButton = Button(image=wrongImg, highlightthickness=0)
unknownButton.grid(row=1, column=0)

checkImg = PhotoImage(file="images/right.png")
checkButton = Button(image=checkImg, highlightthickness=0)
checkButton.grid(row=1, column=1)


next_card()

window.mainloop()
