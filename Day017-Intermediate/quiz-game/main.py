from data import question_data
from question_model import Question

for question in question_data:
    print(f"question['text']: {question['text']} question['answer']: {question['answer']}")
    print(f"{Question(question['text'], question['answer'])}")
