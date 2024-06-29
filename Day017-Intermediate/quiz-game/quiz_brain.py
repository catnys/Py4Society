class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.questionIndex = 0
        self.score = 0

    def isEmpty(self):
        return self.questionIndex == len(self.questions)

    def nextQuestion(self):
        input(f"Q.{self.questionIndex}: {self.questions[self.questionIndex].question} (True/False)")
        self.questionIndex += 1


    def checkAnswer(self, answer,userAnswer):
        if answer.lower() == userAnswer.lower():
            print(f"Correct! {answer}")
            self.score += 1
        else:
            print(f"Incorrect! you have replied {userAnswer}, however the answer was {answer}")
        print(f"Your score is {self.score}/{self.questionIndex}")


