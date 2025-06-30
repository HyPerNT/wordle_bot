"""
Class for Wordle Game Functionality.

This module provides the Wordle game functionality.

It defines the Wordle class, which contains methods for starting a game,
making guesses, and checking results.
"""

from random import randint
from common import (
    boolean_comprehension,
    get_word_list,
    LOG_FILE,
    RESULT,
    MSG,
    CORRECT_LETTER,
    INCORRECT_LETTER,
    MISPLACED_LETTER,
    ALL_CORRECT,
)
import logging

# File: wordle/wordle.py


class Wordle:
    """
    A class representing a Wordle game.

    It manages the game state, including the secret word, guesses, and results.
    It provides methods to start the game, make guesses, and check for errors.

    Attributes
    ----------
    turns_taken : int
        The number of turns taken in the current game.
    game_in_progress : bool
        Indicates whether a game is currently in progress.
    guesses : list[str]
        A list of words guessed by the player.
    results : list[list[int]]
        A list of results corresponding to each guess, where each result is a list of integers
        representing the status of each letter in the guess (correct, misplaced, or incorrect).
    word_list : list[str]
        A list of valid words that can be used in the game.
    logger : logging.Logger
        A logger instance for logging game events and errors.

    Methods
    -------
    generate_word() -> str
        Generate a random word from the word list to be used as the secret word for the game
    get_all_indices(list: list[int]) -> list[int]
        Returns a list of indices where the value is 1 in the given list.
    is_misplaced_letter(letter: str, word: str, result: list[int], index: int) -> bool
        Check if a letter in the guessed word is misplaced compared to the secret word.
    check_error_conditions(word: str) -> dict
        Check for error conditions before making a guess and returns a dictionary with the result and message.
    guess(word: str) -> dict
        Process a guess, updates the game state, and returns the result of the guess.
    start_game() -> None
        Initialize a new game by selecting a secret word and resetting the game state.
    """

    def __init__(self) -> None:
        """
        Initialize the Wordle game instance with default values.

        Sets the secret word to an empty string, initializes the number of turns taken to 0,
        and sets the game in progress flag to False. Initialize lists for guesses and results.
        Loads the word list from a file and sets up logging.
        """
        self.secret_word: str = ""
        self.turns_taken: int = 0
        self.game_in_progress: bool = False
        self.guesses: list[str] = []
        self.results: list[list[int]] = []
        self.word_list: list[str] = get_word_list()
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.CRITICAL,
            format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
        )

    def generate_word(self) -> str:
        """
        Select a random word from the word list to be used as the secret word for the game.

        Parameters
        ----------
        None

        Returns
        -------
        str
            A randomly selected word from the word list.
        """
        return self.word_list[randint(0, len(self.word_list) - 1)]

    def get_all_indices(self, list: list[int]) -> list[int]:
        """
        Returns a list of indices where the value is 1 in the given list.

        This is used to find the positions of correct letters in the result list.

        Parameters
        ----------
        list : list[int]
            A list of integers where 1 indicates the presence of a correct letter.

        Returns
        -------
        list[int]
            A list of indices where the value is 1 in the input list.
        """
        return [i for i, x in enumerate(list) if x == 1]

    def is_misplaced_letter(
        self, letter: str, word: str, result: list[int], index: int
    ) -> bool:
        """
        Check if a letter in the guessed word is misplaced compared to the secret word.

        A letter is considered misplaced if it exists in the secret word but is not in the correct position
        and the number of occurrences in the secret word is greater than or equal to the number of
        occurrences in the guessed word up to the current index.

        Parameters
        ----------
        letter : str
            The letter to check for being misplaced.
        word : str
            The guessed word.
        result : list[int]
            The result of the previous guesses, where each element indicates the status of each letter
            (correct or incorrect).
        index : int
            The current index in the guessed word being checked.

        Returns
        -------
        bool
            True if the letter is misplaced, False otherwise.
        """
        occurances_in_secret_word = boolean_comprehension(self.secret_word, letter)
        occurances_in_guess = boolean_comprehension(word, letter)
        self.logger.info(f"Checking {word} for {letter}")
        self.logger.info(f"{self.secret_word}: {occurances_in_secret_word}")
        self.logger.info(f"{word}: {occurances_in_guess}")
        correct_indices = self.get_all_indices(
            boolean_comprehension(result, CORRECT_LETTER)
        )
        letter_indices = self.get_all_indices(boolean_comprehension(word, letter))
        secret_count = sum(occurances_in_secret_word) - sum(
            idx in correct_indices for idx in letter_indices
        )
        guess_count = sum(occurances_in_guess[: index + 1])
        self.logger.info(f"S: {secret_count}\tG: {guess_count}")
        if secret_count == 0 or secret_count < guess_count:
            return False
        return True

    def check_error_conditions(self, word: str) -> dict:
        """
        Check for error conditions before making a guess.

        This method verifies if the game is in progress and if the guessed word is valid.

        Parameters
        ----------
        word : str
            The word to be guessed.

        Returns
        -------
        dict
            A dictionary containing the result and a message.
            If there are no errors, the result is None and the message is None.
            If there are errors, the result is None and the message describes the error.
        """
        if not self.game_in_progress:
            self.logger.warning("Game not started!")
            return {RESULT: None, MSG: "Game not started!"}
        if word not in self.word_list:
            self.logger.warning("Not a valid word!")
            return {RESULT: None, MSG: "Not a valid word!"}
        return {RESULT: None, MSG: None}

    def guess(self, word: str) -> dict:
        """
        Process a guess, updates the game state, and returns the result of the guess.

        This method checks for error conditions, compares the guessed word with the secret word,
        and updates the results accordingly. It also checks if the player has won or lost the game.

        Parameters
        ----------
        word : str
            The word guessed by the player.

        Returns
        -------
        dict
            A dictionary containing the result of the guess and a message.
            If the guess is valid, the result is a list indicating the status of each letter
            (correct, misplaced, or incorrect). If the player wins, the message indicates a win.
            If the player loses, the message indicates a loss.
            If there are errors, the result is None and the message describes the error.
        """
        self.logger.debug(f"Word guessed: {word}")
        errors = self.check_error_conditions(word)
        if errors[RESULT] is not None:
            return errors
        result = []
        index = 0

        for correct_letter, guessed_letter in zip(self.secret_word, word):
            if guessed_letter == correct_letter:
                result.append(CORRECT_LETTER)
            else:
                result.append(INCORRECT_LETTER)
        index = 0
        for correct_letter, guessed_letter, r in zip(self.secret_word, word, result):
            if r is CORRECT_LETTER:
                index += 1
                continue
            elif self.is_misplaced_letter(guessed_letter, word, result, index):
                result[index] = MISPLACED_LETTER
            index += 1
        self.turns_taken += 1
        if self.turns_taken == 6:
            self.game_in_progress = False
        self.guesses.append(word)
        self.results.append(result)
        if result == ALL_CORRECT:
            self.logger.debug("Player won!")
            self.game_in_progress = False
            return {RESULT: result, MSG: "You win!"}
        if not self.game_in_progress:
            self.logger.debug("Player lost!")
            return {RESULT: result, MSG: "You lost!"}
        self.logger.debug(f"Returnsing: {result}")
        return {RESULT: result, MSG: None}

    def start_game(self) -> None:
        """
        Initialize a new game by selecting a secret word and resetting the game state.

        This method sets the secret word to a randomly generated word from the word list,
        resets the game in progress flag to True, and clears the guesses and results lists.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.secret_word = self.generate_word()
        self.game_in_progress = True
        self.turns_taken = 0
        self.guesses = []
        self.results = []
