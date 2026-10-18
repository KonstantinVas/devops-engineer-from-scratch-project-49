import random

RULES = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = []

    for index in range(PROGRESSION_LENGTH):
        number = start + index * step
        progression.append(str(number))

    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(progression)

    return question, correct_answer