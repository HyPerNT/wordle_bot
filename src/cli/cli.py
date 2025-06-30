"""
CLI for Wordle Bot.

This module provides a command-line interface for interacting with Wordle bots.
It allows users to select a bot, play games, and input guesses and results interactively.
"""

from bots import BotBehaviors
from common import prettify_guess
from wordle import Wordle
from bots.util import GUESSES, RESULTS
from common.util import (
    ALL_CORRECT,
    CORRECT_LETTER,
    INCORRECT_LETTER,
    MISPLACED_LETTER,
    MSG,
    RESULT,
    get_all_subclasses,
)
from .util import get_bot_selection, get_choice_from_prompt


class Cli:
    """
    Command-line interface for Wordle bots.

    This class manages user interaction for playing Wordle with different bot behaviors.
    It handles bot selection, game flow, user guesses, and result input.
    """

    def __init__(self):
        """Initialize the CLI."""
        self.bots = get_all_subclasses(BotBehaviors)
        self.wordle = Wordle()
        self.quit = False

    def game_in_progress(self) -> bool:
        """
        Determine whether a game is in progress.

        Returns
        -------
        bool
            False if the game is over, True otherwise
        """
        if len(self.bot.guesses[GUESSES]) == 0:
            return True
        return (len(self.bot.guesses[GUESSES]) < 6) and (
            self.bot.guesses[RESULTS][-1][RESULT] != ALL_CORRECT
        )

    def init_bot(self) -> None:
        """Prompt user for bot to use and set class instance to that selection."""
        selection: int = get_bot_selection(self.bots)
        self.bot: BotBehaviors = self.bots[selection]()
        self.bot.reset()

    def play_interactively(self) -> None:
        """Play a game interactively with the user, prompting for guesses and results."""
        # Play a single game
        while self.game_in_progress():
            self.provide_guess()
            self.accept_guess()
            self.accept_result()
        print("Game over!")

    def play_automatically(self) -> None:
        """Play a game a automatically with the user, prompting for a secret word and running the game."""
        self.wordle.start_game()
        guess: str = self.get_valid_word()
        self.wordle.secret_word = guess
        self.bot.reset()
        while self.wordle.game_in_progress:
            self.bot.accept_result(self.wordle.guess(self.bot.generate_guess()))
        for word, result in zip(self.wordle.guesses, self.wordle.results):
            print(f"\t{prettify_guess(word, result)}")

    def play(self) -> None:
        """Play a game with the user, repeatedly prompting for new games or new bots."""
        while True:
            choice: int = get_choice_from_prompt(
                "Play interactively, or set a secret word and watch the bot play?",
                ["Play interactively", "Play automatically"],
            )
            if choice == 0:
                self.play_interactively()
            elif choice == 1:
                self.play_automatically()

            # Post-game options
            while True:
                choice = get_choice_from_prompt(
                    "\nWhat would you like to do next?",
                    [
                        "New game with the same bot",
                        "New game with a new bot",
                        "Go back",
                        "Quit",
                    ],
                )
                if choice == 0:
                    self.bot.reset()
                    break  # Start new game with same bot
                elif choice == 1:
                    self.init_bot()
                    break  # Start new game with new bot
                elif choice == 2:
                    self.quit = False
                    return  # Exit the play loop, go back
                elif choice == 3:
                    self.quit = True
                    return  # Exit the play loop and quit

    def init_session(self) -> None:
        """Initialize a new game session."""
        self.init_bot()
        self.play()

    def provide_guess(self):
        """Provide the bot's next guess to the user."""
        old_list: list[str] = self.bot.possible_words
        print(
            f"Suggested next word: {self.bot.generate_guess()} (of {len(self.bot.possible_words)} words)"
        )
        # Reset bot's internal state
        self.bot.guesses[GUESSES].pop()
        self.bot.possible_words = old_list

    def accept_guess(self):
        """Accept a guess from the user, validate, and update bot state."""
        guess = self.get_valid_word()
        self.bot.guesses[GUESSES].append(guess)

    def get_valid_word(self) -> str:
        """Accept a word from the user, testing if it is valid before returning."""
        print("Enter your word")
        while True:
            word = input("> ").strip().upper()
            if word in self.wordle.word_list:
                return word
            else:
                print(
                    f"'{word}' is not a valid word. Please enter a valid word from the possible words list."
                )

    def accept_result(self):
        """Prompt user for result of guess and update bot state."""
        VALID_DIGITS = {INCORRECT_LETTER, MISPLACED_LETTER, CORRECT_LETTER}
        while True:
            print("Enter result for the guess")
            print(
                f"(5 digits, {INCORRECT_LETTER}=incorrect, {MISPLACED_LETTER}=misplaced, {CORRECT_LETTER}=correct)"
            )
            result_str = input("> ").strip()
            # Remove commas and spaces
            cleaned = result_str.replace(",", "").replace(" ", "")
            if len(cleaned) == 5 and all(int(c) in VALID_DIGITS for c in cleaned):
                # Convert to list of ints
                result_list = [int(c) for c in cleaned]
                self.bot.accept_result({RESULT: result_list, MSG: None})
                break
            else:
                print(
                    "Invalid input. Please enter exactly 5 digits (0, 1, or 2), e.g. 01220 or 0 1 2 2 0 or 0,1,2,2,0."
                )
