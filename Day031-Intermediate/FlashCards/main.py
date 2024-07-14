import csv
import os
from tkinter import *
from tkinter import messagebox

backgroundColor = "#B1DDC6"

# Helper Functions
def loadData(filepath):
    try:
        with open(filepath, encoding='utf-8') as file:
            reader = csv.reader(file)
            # Skip header
            next(reader)
            return [{"German": german, "English": english} for german, english in reader]
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return []

def saveUnknownWord(wordPair, filepath):
    with open(filepath, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([wordPair['German'], wordPair['English']])

def showEnglish():
    global currentWord
    if currentWord:
        canvas.itemconfig(cardWord, text=currentWord['English'])

def nextCard():
    global currentWord
    if words:
        currentWord = words.pop()
        canvas.itemconfig(cardTitle, text="German")
        canvas.itemconfig(cardWord, text=currentWord['German'])
        window.after(3000, showEnglish)
    else:
        messagebox.showinfo("End", "No more cards left!")
        window.destroy()

def knownWord():
    nextCard()

def unknownWord():
    if currentWord:
        saveUnknownWord(currentWord, "unknown_words.csv")
    nextCard()

def setupGui():
    global window, canvas, cardTitle, cardWord
    window = Tk()
    window.title("Flash Cards")
    window.config(padx=50, pady=50, bg=backgroundColor)

    canvas = Canvas(width=800, height=526, bg=backgroundColor, highlightthickness=0)
    cardFrontImg = PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=cardFrontImg)
    cardTitle = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic", "underline"), fill="black")
    cardWord = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
    canvas.grid(row=0, column=0, columnspan=2)

    wrongImg = PhotoImage(file="images/wrong.png")
    unknownButton = Button(image=wrongImg, highlightthickness=0, command=unknownWord)
    unknownButton.grid(row=1, column=0)

    checkImg = PhotoImage(file="images/right.png")
    checkButton = Button(image=checkImg, highlightthickness=0, command=knownWord)
    checkButton.grid(row=1, column=1)

    nextCard()  # Load the first card
    window.mainloop()


if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    words = loadData("data/words.csv")  # Adjust the path based on your folder structure
    currentWord = None
    setupGui()
