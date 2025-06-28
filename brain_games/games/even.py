import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    """
    Generates a round of the 'Even or Not' game.

    Returns:
        tuple: A tuple containing:
            - str: A randomly generated number (as a string).
            - str: The correct answer ("yes" if the number is even, "no" otherwise).
    """
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer
