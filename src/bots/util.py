"""
Common Utilities for Wordle Bot.

This module provides various utility functions and constants used throughout the Wordle bot application.

It includes functions for reading a word list, formatting guesses with ANSI color coding,
and generating boolean comprehensions for lists.
"""

from common import (
    get_word_list,
    RESULT,
    INCORRECT_LETTER,
    MISPLACED_LETTER,
    CORRECT_LETTER,
)
import logging

# file: bots/util.py

GUESSES = "words"
RESULTS = "results"


class Filter:
    """
    A class that provides various filtering methods for word lists used in Wordle games.

    It includes methods to check for unique letters, filter words based on letter presence,
    and filter words based on previous guesses and results.

    Attributes
    ----------
    logger : logging.Logger
        A logger instance for logging filtering events and errors.
    word_list : list[str]
        A list of valid words that can be used in the game.
    all_unique_words : list[str]
        A list of words that contain all unique letters, derived from the word list.
    """

    def __init__(self) -> None:
        """
        Initialize the Filter instance with a word list and sets up logging.

        Loads the word list from a file and filters it to find words with all unique letters.
        """
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.word_list = get_word_list()
        self.all_unique_words = [
            word for word in self.word_list if self.has_all_unique_letters(word)
        ]

    def has_all_unique_letters(self, word: str) -> bool:
        """
        Check if a word contains all unique letters.

        A word is considered to have all unique letters if no letter appears more than once.

        Parameters
        ----------
        word : str
            The word to check for unique letters.

        Returns
        -------
        bool
            True if the word has all unique letters, False otherwise.
        """
        for c in word:
            if word.count(c) > 1:
                return False
        return True

    def is_letter_possible(self, words: list[str], letter: str) -> bool:
        """
        Check if a letter is present in any of the words in the list.

        Parameters
        ----------
        words : list[str]
            A list of words to check.
        letter : str
            The letter to check for presence in the words.

        Returns
        -------
        bool
            True if the letter is present in any of the words, False otherwise.
        """
        return any(letter in word for word in words)

    def is_valid_word(self, word: str) -> bool:
        """
        Check if a word is valid by verifying its presence in the word list.

        Parameters
        ----------
        word : str
            The word to check for validity.

        Returns
        -------
        bool
            True if the word is in the word list, False otherwise.
        """
        return word in self.word_list

    def filter_containing_letter(self, words: list[str], letter: str) -> list[str]:
        """
        Filter a list of words to include only those that contain a specific letter.

        Parameters
        ----------
        words : list[str]
            A list of words to filter.
        letter : str
            The letter to check for in the words.

        Returns
        -------
        list[str]
            A list of words that contain the specified letter.
        """
        return [word for word in words if letter in word]

    def filter_not_containing_letter(self, words: list[str], letter: str) -> list[str]:
        """
        Filter a list of words to exclude those that contain a specific letter.

        Parameters
        ----------
        words : list[str]
            A list of words to filter.
        letter : str
            The letter to check for in the words.

        Returns
        -------
        list[str]
            A list of words that do not contain the specified letter.
        """
        return [word for word in words if letter not in word]

    def filter_containing_letter_at(
        self, words: list[str], letter: str, index: int
    ) -> list[str]:
        """
        Filter a list of words to include only those that contain a specific letter at a specific index.

        Parameters
        ----------
        words : list[str]
            A list of words to filter.
        letter : str
            The letter to check for in the words.
        index : int
            The index at which the letter should be present in the words.

        Returns
        -------
        list[str]
            A list of words that contain the specified letter at the specified index.
        """
        return [word for word in words if word[index] == letter]

    def filter_not_containing_letter_at(
        self, words: list[str], letter: str, index: int
    ) -> list[str]:
        """
        Filter a list of words to exclude those that contain a specific letter at a specific index.

        Parameters
        ----------
        words : list[str]
            A list of words to filter.
        letter : str
            The letter to check for in the words.
        index : int
            The index at which the letter should not be present in the words.

        Returns
        -------
        list[str]
            A list of words that do not contain the specified letter at the specified index.
        """
        return [word for word in words if word[index] is not letter]

    def filter_compatible_with_guess(
        self, words: list[str], guess: str, result: dict
    ) -> list[str]:
        """
        Filter a list of words based on a guess and the result of that guess.

        The result is expected to be a dictionary with a key 'result' that contains a list of responses
        corresponding to each letter in the guess. The responses can be:
        - CORRECT_LETTER: The letter is in the correct position.
        - MISPLACED_LETTER: The letter is in the word but in the wrong position.
        - INCORRECT_LETTER: The letter is not in the word at all

        Parameters
        ----------
        words : list[str]
            A list of words to filter based on the guess and result.
        guess : str
            The guessed word to compare against the words in the list.
        result : dict
            A dictionary containing the result of the guess, with a key 'result' that holds a
            list of responses for each letter in the guess.

        Returns
        -------
        list[str]
            A list of words that are compatible with the guess and result.
        """
        index = 0
        self.logger.debug(f"Currently {len(words)} words")
        self.logger.debug(f"Filtering {guess} / {result[RESULT]}")
        for letter, response in zip(guess, result[RESULT]):
            if response is CORRECT_LETTER:
                words = self.filter_containing_letter_at(words, letter, index)
            elif response is INCORRECT_LETTER:
                if guess.count(letter) > 1:
                    words = self.filter_not_containing_letter_at(words, letter, index)
                else:
                    words = self.filter_not_containing_letter(words, letter)
            elif response is MISPLACED_LETTER:
                filtered_words = self.filter_not_containing_letter_at(
                    words, letter, index
                )
                words = self.filter_containing_letter(filtered_words, letter)
            index += 1
        self.logger.debug(f"Filtered to {len(words)} words")
        return words

    def filter_compatible_with_past_guesses(
        self, words: list[str], guesses: dict
    ) -> list[str]:
        """
        Filter a list of words based on multiple past guesses and their results.

        This method iterates through all past guesses and their corresponding results,
        filtering the list of words to retain only those that are compatible with all guesses.

        Parameters
        ----------
        words : list[str]
            A list of words to filter based on the past guesses and results.
        guesses : dict
            A dictionary containing past guesses and their results, with keys 'words' and 'results'.
            'words' is a list of guessed words, and 'results' is a list of dictionaries containing
            the result for each guess.

        Returns
        -------
        list[str]
            A list of words that are compatible with all past guesses and results.
        """
        for guess, result in zip(guesses[GUESSES], guesses[RESULTS]):
            words = self.filter_compatible_with_guess(words, guess, result)
        return words

    def filter_unique_letters(self, words: list[str]) -> list[str]:
        """
        Filter a list of words to include only those that have all unique letters.

        Parameters
        ----------
        words : list[str]
            A list of words to filter.

        Returns
        -------
        list[str]
            A list of words that contain all unique letters.
        """
        return [word for word in words if self.has_all_unique_letters(word)]
