class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.questionIndex = 0

    def isEmpty(self):
        return self.questionIndex == len(self.questions)

    def nextQuestion(self):
        input(f"Q.{self.questionIndex}: {self.questions[self.questionIndex].question} (True/False)")
        self.questionIndex += 1
