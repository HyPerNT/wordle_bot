"""
Test suite for the BayesianBot class.

This module contains tests for the BayesianBot class, specifically for the methods
generate_first_guess and generate_next_guess.
"""

from common.util import RESULT, MSG  # type: ignore
from bots import BayesianBot  # type: ignore
from bots.util import GUESSES, RESULTS  # type: ignore

# file: tests/test_bayesian_bot.py


class TestBayesianBot:
    """
    Unit tests for the BayesianBot class.

    This class tests the BayesianBot to ensure it functions correctly,
     as well produce the correct sequences of guesses.
    """

    def test_generate_first_guess(self):
        """
        Test the generate_first_guess method of the BayesianBot class.
        """
        bot = BayesianBot()
        first_guess = bot.generate_first_guess()
        assert isinstance(first_guess, str)
        assert len(first_guess) == 5  # Assuming the words are 5 letters long
        assert (
            first_guess in bot.filter.all_unique_words
        ), "First guess should be in the list of unique words"
        assert first_guess == "CAGEY", "Expected first guess to be 'CAGEY'"

    def test_generate_next_guess(self):
        """
        Test the generate_next_guess method of the BayesianBot class.
        """
        bot = BayesianBot()
        bot.guesses[GUESSES].append("CAGEY")  # Simulate a previous guess
        bot.accept_result(
            {RESULT: [0 for _ in range(5)], MSG: None}
        )  # Simulate a result for the guess
        next_guess = bot.generate_next_guess()
        assert isinstance(next_guess, str)
        assert len(next_guess) == 5  # Assuming the words are 5 letters long
        assert (
            next_guess in bot.filter.all_unique_words
        ), "Next guess should be in the list of unique words"
        assert next_guess == "BLIND", "Expected next guess to be 'BLIND'"

    def test_for_music(self):
        """
        Test the bot against "MUSIC" to ensure it returns the expected words.
        """
        bot = BayesianBot()
        guess = bot.generate_guess()
        assert guess == "CAGEY", "Expected first guess to be 'CAGEY'"
        bot.accept_result({RESULT: [1, 0, 0, 0, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "BLIND", "Expected next guess to be 'BLIND'"
        bot.accept_result({RESULT: [0, 0, 1, 0, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "FROWS", "Expected next guess to be 'FROWS'"
        bot.accept_result({RESULT: [0, 0, 0, 0, 1], MSG: None})
        guess = bot.generate_guess()
        assert guess == "THUMP", "Expected next guess to be 'THUMP'"
        bot.accept_result({RESULT: [0, 0, 1, 1, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "MUSIC", "Expected next guess to be 'MUSIC'"

    def test_for_ziram(self):
        """
        Test the bot against "ZIRAM" to ensure it returns the expected words.
        """
        bot = BayesianBot()
        guess = bot.generate_guess()
        assert guess == "CAGEY", "Expected first guess to be 'CAGEY'"
        bot.accept_result({RESULT: [0, 1, 0, 0, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "BLIND", "Expected next guess to be 'BLIND'"
        bot.accept_result({RESULT: [0, 0, 1, 0, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "FROWS", "Expected next guess to be 'FROWS'"
        bot.accept_result({RESULT: [0, 1, 0, 0, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "THUMP", "Expected next guess to be 'THUMP'"
        bot.accept_result({RESULT: [0, 0, 0, 1, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "AMARI", "Expected next guess to be 'AMARI'"
        bot.accept_result({RESULT: [1, 1, 0, 1, 1], MSG: None})
        guess = bot.generate_guess()
        assert guess == "MIRZA", "Expected next guess to be 'MIRZA'"
