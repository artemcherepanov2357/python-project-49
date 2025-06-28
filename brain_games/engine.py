"""Common engine"""

import prompt


ROUNDS_COUNT = 3


def run_game(game_module, name):
    print(game_module.RULE)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")
