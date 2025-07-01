import random

RULE = "What is the result of the expression?"


def generate_round():
    """Generates a simple arithmetic expression and its correct answer.

    Randomly selects two numbers between 1 and 100 and an operator (+, -, *),
    then constructs a math question and computes the correct result.

    Returns:
        tuple: A tuple containing:
            - str: The generated arithmetic expression (e.g., "5 + 3").
            - str: The correct answer as a string (e.g., "8").

    Example:
        >>> generate_round()
        ("42 - 17", "25")
    """
    operators = ["+", "-", "*"]
    num1 = random.randint(1, 100)  # NOSONAR
    num2 = random.randint(1, 100)  # NOSONAR
    op = random.choice(operators)  # NOSONAR

    question = f"{num1} {op} {num2}"
    correct_answer = str(eval(question))

    return question, correct_answer
