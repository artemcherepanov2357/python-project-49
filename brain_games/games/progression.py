import random

RULE = "What number is missing in the progression?"


def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def generate_round():
    start = random.randint(1, 20)  # NOSONAR
    step = random.randint(1, 5)  # NOSONAR
    length = random.randint(5, 10)  # NOSONAR
    hidden_index = random.randint(0, length - 1)  # NOSONAR

    progression = generate_progression(start, step, length)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, correct_answer
