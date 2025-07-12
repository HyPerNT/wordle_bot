"""
Tester for Wordle Bot Functionality.

This module defines the WordleTester class, which is used to test a Wordle bot against a list of words.

It inherits from the Wordle class and provides methods to run tests, collect results, and analyze
the performance of the bot.
"""

from common.util import RESULT
from wordle import Wordle
from common import (
    ALL_CORRECT,
    CORRECT_LETTER,
    INCORRECT_LETTER,
    MISPLACED_LETTER,
    boolean_comprehension,
    prettify_guess,
    prettify_guess_no_color,
)
from bots import BotBehaviors
from tqdm import tqdm  # type: ignore

# I've no idea why MyPy is complaining about tqdm, it works fine.
import logging

# file: tester/wordle_tester.py


class WordleTester(Wordle):
    """
    A class to test a Wordle bot against a list of words.

    It inherits from the Wordle class and provides methods to run tests,
    collect results, and analyze the performance of the bot.

    Attributes
    ----------
    test_results : list[dict]
        A list to store the results of each test, including the word, result, and guesses.
    successes : list[str]
        A list to store the words that were guessed correctly by the bot.
    failures : list[str]
        A list to store the words that were not guessed correctly by the bot.
    logger : logging.Logger
        A logger instance for logging test events and errors.
    """

    def __init__(self) -> None:
        """
        Initialize the WordleTester instance by calling the parent class constructor and setting up the initial state for testing.

        Sets up the test results, successes, failures, and logger.
        """
        super().__init__()
        self.test_results: list[dict] = []
        self.successes: list[str] = []
        self.failures: list[str] = []
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def test(
        self, bot: BotBehaviors, print_results: bool = True, print_failures=False
    ) -> None:
        """
        Runs tests on the bot using a predefined list of words.

        It iterates through each word in the word list, starts a new game,
        sets the secret word, and allows the bot to make guesses until the game is over.
        The results of each test are collected and stored in the test_results list.

        Parameters
        ----------
        bot : BotBehaviors
            An instance of a bot that inherits from BotBehaviors.
            This bot will generate guesses and accept results based on the game's feedback.
        print_results : bool, optional
            If True, the results of the tests will be printed to the console.
            Defaults to True.
        print_failures : bool, optional
            If True, additionally prints out failed words in the style of Wordle.
            Defaults to False.
        """
        if print_results:
            print("Running tests")
        for word in tqdm(self.word_list):
            self.logger.debug(f"Testing {word}")
            self.start_game()
            self.secret_word = word
            while self.game_in_progress:
                result = self.guess(bot.generate_guess())
                bot.accept_result(result)
                if self.secret_word not in bot.possible_words:
                    print(
                        f"Bot erroneously eliminated {self.secret_word} from possible word list"
                    )
            self.test_results.append(
                {
                    "word": self.secret_word,
                    RESULT: self.results,
                    "guesses": self.guesses,
                }
            )
            self.logger.debug(f"Result: {self.test_results[-1]}")
            if self.results[-1] == ALL_CORRECT:
                self.successes.append(self.secret_word)
            else:
                self.failures.append(self.secret_word)
        if print_results:
            print(self.get_results_str())
            if print_failures:
                print(self.get_failures_str())
                print(self.get_wacky_failures_string())

    def get_results_str(self) -> str:
        """
        Generate a summary string of the test results, including the number of correct and incorrect guesses, success rates, and failure details.

        Returns
        -------
        str
            A formatted string summarizing the test results, including success and failure rates,
            average guesses per success, and details of incorrect guesses.
        """
        string = f"Correct guesses: {len(self.successes)}/{len(self.word_list)} ({100 * len(self.successes)/len(self.word_list):.2f}%)\n"
        string += f"Incorrect guesses: {len(self.failures)}/{len(self.word_list)} ({100 * len(self.failures)/len(self.word_list):.2f}%)\n"
        guess_counts = [0 for _ in range(6)]
        size = 0
        for r in self.test_results:
            if r[RESULT][-1] != ALL_CORRECT:
                continue
            count = len(r[RESULT])
            size += count
            guess_counts[count - 1] += 1
        string += "Success rate:\n"
        for i in range(6):
            string += f"\t{i+1} guesses: {guess_counts[i]} ({100 * guess_counts[i]/len(self.successes):.2f}%)\n"
        string += f"\tAvg: {size / len(self.successes):.3f}\n"
        string += "Failure details:\n"
        correct_letters = 0
        incorrect_letters = 0
        for r in self.test_results:
            if r[RESULT][-1] == ALL_CORRECT:
                continue
            correct_letters += sum(boolean_comprehension(r[RESULT][-1], CORRECT_LETTER))
            incorrect_letters += sum(
                boolean_comprehension(r[RESULT][-1], INCORRECT_LETTER)
            )
        string += f"\tAverage correct letters on loss: {correct_letters / len(self.failures):.3f}\n"
        string += f"\tAverage incorrect letters on loss: {incorrect_letters / len(self.failures):.3f}\n"
        string += f"\tAverage misplaced letters on loss: {(5 * len(self.failures) - correct_letters - incorrect_letters) / len(self.failures):.3f}\n"
        return string

    def get_failures_str(self, color: bool = True) -> str:
        """
        Generate a detailed string of the failures encountered during the tests.

        This includes the words that were not guessed correctly, the guesses made,
        and the results of those guesses.

        Parameters
        ----------
        color : bool, optional
            If True, the output will be formatted with colors for better readability.
            Defaults to True.

        Returns
        -------
        str
            A formatted string containing details of the failures, including the words,
            guesses, and results.
        """
        string = "Additional failure details:\n"
        for r in self.test_results:
            if r[RESULT][-1] == ALL_CORRECT:
                continue
            string += self.get_failure_str(r, color)
        return string

    def get_failure_str(self, r: dict, color: bool = True) -> str:
        """
        Generate a formatted string for a single failure, including the word, the guesses made, and the results of those guesses.

        Parameters
        ----------
        r : dict
            A dictionary containing the word, guesses, and results for a single test.
        color : bool, optional
            If True, the output will be formatted with colors for better readability.
            Defaults to True.

        Returns
        -------
        str
            A formatted string containing the details of the failure, including the word,
            guesses, and results.
        """
        string = f"\t{r['word']}\n"
        prettify_guess_fn = prettify_guess_no_color if not color else prettify_guess
        for word, result in zip(r["guesses"], r[RESULT]):
            string += f"\t\t{prettify_guess_fn(word, result)}\n"
        return string

    def get_wacky_failures_string(self, color: bool = True) -> str:
        """
        Generate a string containing details of failures that include misplaced letters.

        This method filters the test results to include only those where the last result
        contains misplaced letters, and formats the output accordingly.

        Parameters
        ----------
        color : bool, optional
            If True, the output will be formatted with colors for better readability.
            Defaults to True.

        Returns
        -------
        str
            A formatted string containing details of failures with misplaced letters,
            including the words, guesses, and results.
        """
        string = "Failure details:\n"
        prettify_guess_fn = prettify_guess_no_color if not color else prettify_guess
        for r in self.test_results:
            if r[RESULT][-1] == ALL_CORRECT:
                continue
            if MISPLACED_LETTER in r[RESULT][-1]:
                string += f"\t{r['word']}\n"
                for word, result in zip(r["guesses"], r[RESULT]):
                    string += f"\t\t{prettify_guess_fn(word, result)}\n"
        return string
