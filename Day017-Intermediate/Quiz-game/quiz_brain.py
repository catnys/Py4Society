class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.questionIndex = 0
        self.score = 0

    def isNotEmpty(self):
        return self.questionIndex < len(self.questions)


    def checkAnswer(self, answer,userAnswer):
        if answer.lower() == userAnswer.lower():
            print(f"Correct! {answer}")
            self.score += 1
        else:
            print(f"Incorrect! you have replied {userAnswer}, however the answer was {answer}")
        print(f"Your score is {self.score}/{self.questionIndex}")


    def nextQuestion(self):
        if self.isNotEmpty():
            currentQuestion = self.questions[self.questionIndex]
            userAnswer = input(f"Q.{self.questionIndex}: {currentQuestion.question} (True/False): ")
            self.checkAnswer(currentQuestion.answer, userAnswer)
            self.questionIndex += 1
        else:
            # No more questions to answer
            print("No more questions available.")