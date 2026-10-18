import random

RULES = 'What is the result of the expression?'


def calculate(a, b, op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b


def get_question_and_answer():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-', '*'])

    question = f'{a} {op} {b}'
    correct = str(calculate(a, b, op))
    return question, correct