import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(game):
    name = welcome_user()
    print(game.RULES)

    for _ in range(ROUNDS_COUNT):
        question, correct = game.get_question_and_answer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')