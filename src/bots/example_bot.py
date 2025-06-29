"""
Example Bot for Wordle Game.

This module defines the ExampleBot class, which implements a simple Wordle bot that generates guesses
based on a predefined list of unique words. It inherits from BotBehaviors and provides methods to
generate the first guess and subsequent guesses based on the index of previous guesses.
"""

from .util import GUESSES
from .bot_behaviors import BotBehaviors

# file: bots/example_bot.py


class ExampleBot(BotBehaviors):
    """
    A class representing a simple Wordle bot that generates guesses based on a predefined list of unique words.

    It inherits from BotBehaviors and implements methods to generate the first guess and subsequent guesses
    based on the index of previous guesses.

    Attributes
    ----------
    filter : BotBehaviors
        An instance of BotBehaviors that provides methods for filtering and generating guesses.
    """

    def __init__(self):
        """Initialize the ExampleBot instance by calling the parent class constructor."""
        # Initialize the parent class
        super().__init__()

    def generate_first_guess(self) -> str:
        """
        Generate the first guess for the Wordle game.

        Returns
        -------
        str
            The first guess word for the bot, which is the first unique word in the list.
        """
        return self.filter.all_unique_words[0]

    def generate_next_guess(self) -> str:
        """
        Generate the next guess for the Wordle game based on the number of previous guesses.

        This method selects the next guess from the list of unique words based on the index of previous guesses.

        Returns
        -------
        str
            The next guess word for the bot, selected from the list of unique words.
        """
        return self.filter.all_unique_words[len(self.guesses[GUESSES])]
