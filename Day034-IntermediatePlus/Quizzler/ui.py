from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreLabel = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scoreLabel.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.questionText = self.canvas.create_text(150, 125, text="Some quest text", fill=THEME_COLOR, font="Arial 20 italic")
        self.canvas.grid(row=1, column=0,columnspan=2, pady=50)
        trueImg = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImg, highlightthickness=0)
        self.trueButton.grid(row=2, column=0)

        falseImg = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImg, highlightthickness=0)
        self.falseButton.grid(row=2, column=1)




        self.window.mainloop()

