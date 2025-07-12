"""
Wordle Bot that generates guesses based on letter frequency and previous results.

This module defines the BayesianBot class, which implements the behavior of a Wordle bot.

It inherits from BotBehaviors and provides methods to generate guesses based on letter frequency and previous results.
"""

from .util import GUESSES, RESULTS
from .bot_behaviors import BotBehaviors

# file: bots/bayesian_bot.py


class BayesianBot(BotBehaviors):
    """
    A class representing a Wordle bot that generates guesses based on letter frequency and previous results.

    It inherits from BotBehaviors and implements methods to generate the first guess and subsequent guesses
    based on the frequency of letters and the results of previous guesses.

    Attributes
    ----------
    frequency_list : str
        A string representing the frequency of letters in the English language, ordered from most to least frequent.
    MAX_WORDS : int
        The maximum number of words to allow in the search space before BayesianBot switches away from the greedy strategy.
    BAYES_MIN_TURNS : int
        The minimum number of turns before BayesianBot uses the Bayesian strategy.
    unique_words_set : list[str]
        The word set of the 20 most common letters in English, as disjoint and legal Wordle words.
    GREEDY_MAX_TURNS : int
        The maximum number of turns the Greedy strategy will pbe played for, set to the size of the unique_words_set.
    """

    def __init__(self):
        """Initialize the BayesianBot instance with a predefined frequency list of letters."""
        # Initialize the parent class
        super().__init__()
        self.frequency_list: str = "EARIOTNSLCUDPMHGBFYWKVXZJQ"
        self.MAX_WORDS: int = 3
        self.BAYES_MIN_TURNS: int = 4
        self.unique_words_set: list[str] = ["BLIND", "FROWS", "THUMP"]
        self.GREEDY_MAX_TURNS: int = len(self.unique_words_set) + 1

    def generate_first_guess(self) -> str:
        """
        Generate the first guess for the Wordle game.

        Parameters
        ----------
        None

        Returns
        -------
        str
            The first guess word for the bot, which is hardcoded to "CAGEY".
        """
        return "CAGEY"

    def guess_most_probable_from_list(
        self, candidates: list[str], frequency_list: str
    ) -> str:
        """
        Filter a given candidate word list based on a letter frequency list and returns first result.

        Parameters
        ----------
        candidates : list[str]
            A candidate word list.
        frequency_list : str
            A string representing the order of letters to prioritize.

        Returns
        -------
        str
            The first word from the candidate list with optimum frequency.
        """
        for letter in frequency_list:
            if self.filter.is_letter_possible(self.possible_words, letter):
                filtered: list[str] = self.filter.filter_containing_letter(
                    candidates, letter
                )
                if len(filtered) == 0:
                    return candidates[0]
                candidates = self.filter.filter_containing_letter(candidates, letter)
        return candidates[
            0
        ]  # MyPy complains if this isn't here, even if it will never be executed

    def get_number_of_guesses(self) -> int:
        """
        Get number of guesses made.

        Returns
        -------
        int
            Number of guesses made in this game.
        """
        return len(self.guesses[GUESSES])

    def use_greedy_strategy(self) -> bool:
        """Use the greedy strategy."""
        if self.get_number_of_guesses() < self.GREEDY_MAX_TURNS:
            return not len(self.possible_words) <= self.MAX_WORDS
        return False

    def use_bayesian_strategy(self) -> bool:
        """Use the Bayesian strategy."""
        if self.get_number_of_guesses() >= self.BAYES_MIN_TURNS:
            return True
        return len(self.possible_words) <= self.MAX_WORDS

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
        self.possible_words = self.filter.filter_compatible_with_past_guesses(
            self.possible_words, self.guesses
        )
        num_possible: int = len(self.possible_words)
        if num_possible == 1:
            return self.possible_words[0]
        if self.use_greedy_strategy() and not self.use_bayesian_strategy():
            return self.unique_words_set[self.get_number_of_guesses() - 1]
        totals_dict: dict[str, int] = self.filter.get_letter_count(self.possible_words)
        sorted_letters: str = self.filter.get_sorted_letters(totals_dict)
        return self.guess_most_probable_from_list(self.possible_words, sorted_letters)
