from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def main():
    questionBank = []
    for question in question_data:
        # print(f"question['text']: {question['text']} question['answer']: {question['answer']}")
        questionBank.append(Question(question['text'], question['answer']))

    quiz = QuizBrain(questionBank)

    while not quiz.isEmpty():
        quiz.nextQuestion()

    print(f"Your final score is {quiz.score()}/{len(quiz.questions)}")

if __name__ == '__main__':
    main()
