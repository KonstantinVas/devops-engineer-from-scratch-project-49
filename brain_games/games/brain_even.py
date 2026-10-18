import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def get_question_and_answer():
    number = random.randint(0, 100)
    correct = 'yes' if is_even(number) else 'no'
    return number, correct