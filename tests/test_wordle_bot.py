"""
Test suite for the WordleBot class.

This module contains tests for the WordleBot class, specifically for the methods
generate_first_guess and generate_next_guess.
"""

from common.util import RESULT, MSG  # type: ignore
from bots import WordleBot  # type: ignore
from bots.util import GUESSES, RESULTS  # type: ignore

# file: tests/test_wordle_bot.py


class TestWordleBot:
    def test_generate_first_guess(self):
        """
        Test the generate_first_guess method of the WordleBot class.
        """
        bot = WordleBot()
        first_guess = bot.generate_first_guess()
        assert isinstance(first_guess, str)
        assert len(first_guess) == 5  # Assuming the words are 5 letters long
        assert (
            first_guess in bot.filter.all_unique_words
        ), "First guess should be in the list of unique words"
        assert first_guess == "GHOST", "Expected first guess to be 'GHOST'"

    def test_generate_next_guess(self):
        """
        Test the generate_next_guess method of the WordleBot class.
        """
        bot = WordleBot()
        bot.guesses[GUESSES].append("GHOST")  # Simulate a previous guess
        bot.accept_result(
            {RESULT: [0 for _ in range(5)], MSG: None}
        )  # Simulate a result for the guess
        next_guess = bot.generate_next_guess()
        assert isinstance(next_guess, str)
        assert len(next_guess) == 5  # Assuming the words are 5 letters long
        assert (
            next_guess in bot.filter.all_unique_words
        ), "Next guess should be in the list of unique words"
        assert next_guess == "RAINE", "Expected next guess to be 'RAINE'"

    def test_for_music(self):
        """
        Test the bot against "MUSIC" to ensure it returns the expected words.
        """
        bot = WordleBot()
        guess = bot.generate_guess()
        assert guess == "GHOST", "Expected first guess to be 'GHOST'"
        bot.accept_result({RESULT: [0, 0, 0, 1, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "AESIR", "Expected next guess to be 'AESIR'"
        bot.accept_result({RESULT: [0, 0, 2, 2, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "LYSIN", "Expected next guess to be 'LYSIN'"
        bot.accept_result({RESULT: [0, 0, 2, 2, 0], MSG: None})
        guess = bot.generate_guess()
        assert guess == "MUSIC", "Expected next guess to be 'MUSIC'"
