import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    question = random.randint(2, 100)  # NOSONAR
    correct_answer = "yes" if is_prime(question) else "no"
    return str(question), correct_answer
