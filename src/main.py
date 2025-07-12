"""
Main Script.

This script provides some interaction via the command-line to either run tests against a bot of choice, or
to play a wordle game with a bot of choice.
"""

from tester import WordleTester
from bots import BotBehaviors
from common.util import LOG_FILE, get_all_subclasses
from cli import Cli
from cli.util import get_bot_selection, get_choice_from_prompt
import os

# file: src/main.py


def play_game() -> bool:
    """
    Play a game over the CLI.

    Parameters
    ----------
        None

    Returns
    -------
        True if the user intends to quit, false otherwise
    """
    cli = Cli()
    cli.init_session()
    return cli.quit


def run_tests() -> None:
    """
    Run tests using WordleTester() on a bot of choice.

    Parameters
    ----------
        None

    Returns
    -------
        None
    """
    while True:
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
        bots = get_all_subclasses(BotBehaviors)
        selection: int = get_bot_selection(bots)
        choice: int = get_choice_from_prompt("Print failures?", ["No", "Yes"])
        print_failures: bool = choice == 1
        WordleTester().test(bots[selection](), print_failures=print_failures)
        print("Run another test? (y/N)")
        again = input("> ").strip().lower()
        if again != "y":
            break


def main():
    """Main function to run the Wordle bot or tests."""
    while True:
        choice: int = get_choice_from_prompt(
            "What would you like to do?",
            ["Play a game", "Run tests", "Quit"],
            has_default=False,
        )
        if choice == 0:
            if play_game():
                break
        elif choice == 1:
            run_tests()
        elif choice == 2:
            break


if __name__ == "__main__":
    """Entry point for the script."""
    main()
