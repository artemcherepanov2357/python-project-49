from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games import progression


def main():
    name = welcome_user()
    run_game(progression, name)


if __name__ == "__main__":
    main()
