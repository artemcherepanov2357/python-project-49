import random

RULE = "Find the greatest common divisor of given numbers."


def get_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return str(num1)


def generate_round():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"{num1} {num2}"
    correct_answer = get_gcd(num1, num2)

    return question, correct_answer
