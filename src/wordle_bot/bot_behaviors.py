"""
Class for Wordle Bot Behaviors.

This module defines the BotBehaviors class, which encapsulates the behaviors of a Wordle bot.

It includes methods for generating guesses, accepting results, and managing the bot's state.
"""

from .util import Filter, GUESSES, RESULTS
from common import RESULT, MSG
import logging

# file: wordle_bot/bot_behaviors.py


class BotBehaviors:
    """
    A class representing the behaviors of a Wordle bot.

    It manages the bot's guesses and results, and provides methods to generate guesses
    and accept results from the game.

    Attributes
    ----------
    logger : logging.Logger
        A logger instance for logging bot events and errors.
    filter : Filter
        An instance of Filter to manage the word list and filtering.
    guesses : dict
        A dictionary to store the bot's guesses and results.
    possible_words : list[str]
        A list of possible words that the bot can guess from.
    """

    def __init__(self) -> None:
        """
        Initialize the BotBehaviors instance with default values.

        Sets up the logger, initializes the filter, and resets the guesses.
        """
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.filter = Filter()
        self.guesses: dict = {}
        self.reset()

    def reset(self) -> None:
        """
        Reset the bot's guesses and results.

        Initialize the guesses dictionary and sets the possible words
        to the complete word list.
        """
        self.guesses = {GUESSES: [], RESULTS: []}
        self.possible_words = self.filter.word_list

    def generate_first_guess(self) -> str:  # type: ignore[empty-body]
        """
        Code to generate the first guess.

        This method should be overridden by subclasses to provide specific first guess logic.

        Returns
        -------
        str
            The first guess word for the bot.
        """
        pass

    def generate_next_guess(self) -> str:  # type: ignore[empty-body]
        """
        Code to generate the next guess.

        This method should be overridden by subclasses to provide specific next guess logic.
        This should take into account the previous guesses and results
        Returns
        -------
        str
            The next guess word for the bot.
        """
        pass

    def generate_guess(self) -> str:
        """
        Generate a guess for the bot based on the current state of guesses.

        If there are no previous guesses, it generates the first guess.
        Otherwise, it generates the next guess based on the previous guesses and results.

        Returns
        -------
        str
            The generated guess word for the bot.
        """
        guess = ""
        if len(self.guesses[GUESSES]) == 0:
            guess = self.generate_first_guess()
        else:
            guess = self.generate_next_guess()
        self.guesses[GUESSES].append(guess)
        return guess

    def accept_result(self, result: dict):
        """
        Accept the result of a guess and updates the bot's state accordingly.

        This method processes the result of a guess, updates the guesses and results,
        and logs the received result. If the result indicates a win or loss, it resets the bot's state.

        Parameters
        ----------
        result : dict
            A dictionary containing the result of the guess, with keys RESULT and MSG.
            RESULT is expected to be None if the game is still ongoing, or a win/loss indication.
            MSG can contain additional messages or information about the result.

        Returns
        -------
        None
        """
        if result[RESULT] is None:
            return
        elif result[MSG] is not None:
            self.reset()
        self.guesses[RESULTS].append(result)
        self.logger.info(f"Received: {result}")
