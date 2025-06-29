"""
Wordle Bot that generates guesses based on letter frequency and previous results.

This module defines the WordleBot class, which implements the behavior of a Wordle bot.

It inherits from BotBehaviors and provides methods to generate guesses based on letter frequency and previous results.
"""

from .util import GUESSES, RESULTS
from .bot_behaviors import BotBehaviors

# file: bots/bot.py


class WordleBot(BotBehaviors):
    """
    A class representing a Wordle bot that generates guesses based on letter frequency and previous results.

    It inherits from BotBehaviors and implements methods to generate the first guess and subsequent guesses
    based on the frequency of letters and the results of previous guesses.

    Attributes
    ----------
    frequency_list : str
        A string representing the frequency of letters in the English language, ordered from most to least frequent.
    MAX_LETTERS : int
        The maximum number of unique letters to try for in guessing.
    """

    def __init__(self):
        """Initialize the WordleBot instance with a predefined frequency list of letters."""
        # Initialize the parent class
        super().__init__()
        self.frequency_list: str = "EARIOTNSLCUDPMHGBFYWKVXZJQ"
        self.MAX_LETTERS: int = 26

    def generate_first_guess(self) -> str:
        """
        Generate the first guess for the Wordle game.

        Parameters
        ----------
        None

        Returns
        -------
        str
            The first guess word for the bot, which is hardcoded to "GHOST".
        """
        return "GHOST"

    def generate_next_guess(self) -> str:
        """
        Generate the next guess for the Wordle game based on previous guesses and results.

        This method filters the list of possible words based on the last guess and its result,
        and then selects the next guess based on letter frequency and uniqueness.
        Uniqueness is prioritized to avoid repeated letters in the guess.

        Parameters
        ----------
        None

        Returns
        -------
        str
            The next guess word for the bot, selected from the filtered list of possible words.
        """
        self.possible_words = self.filter.filter_compatible_with_guess(
            self.possible_words, self.guesses[GUESSES][-1], self.guesses[RESULTS][-1]
        )
        num_possible = len(self.possible_words)
        if num_possible == 1:
            return self.possible_words[0]
        # TODO Make it less susceptible to repeated letters
        unique_candidates = self.filter.filter_unique_letters(self.possible_words)
        letter_count = 0
        if len(unique_candidates) > 0:
            for letter in self.frequency_list:
                if letter_count >= self.MAX_LETTERS:
                    break
                if self.filter.is_letter_possible(self.possible_words, letter):
                    filtered = self.filter.filter_containing_letter(
                        unique_candidates, letter
                    )
                    if len(filtered) == 0:
                        return unique_candidates[0]
                    unique_candidates = self.filter.filter_containing_letter(
                        unique_candidates, letter
                    )
                    letter_count += 1
            return self.filter.filter_unique_letters(self.possible_words)[0]
        # TODO make it more clever
        return self.possible_words[0]
