import random

RULES = 'Find the greatest common divisor of given numbers.'

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    question = f'{a} {b}'
    correct = str(get_gcd(a, b))
    return question, correct