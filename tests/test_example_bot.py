"""
Test suite for the ExampleBot class in the bots package.

This module contains tests for the ExampleBot class, which is a simple Wordle bot that generates guesses
based on a predefined list of unique words. The tests cover the generation of the first guess and subsequent guesses.
"""

from bots.example_bot import ExampleBot  # type: ignore
from bots.util import GUESSES  # type: ignore

# file: tests/test_example_bot.py


class TestExampleBot:
    def test_generate_first_guess(self):
        """Test the first guess generation."""
        bot = ExampleBot()
        first_guess = bot.generate_first_guess()
        assert first_guess == "ABENG", f"Expected 'ABENG', got '{first_guess}'"

    def test_generate_next_guess(self):
        """Test the next guess generation."""
        bot = ExampleBot()
        bot.guesses = {GUESSES: ["ABENG"]}
        next_guess = bot.generate_next_guess()
        assert next_guess == "ABERS", f"Expected 'ABERS', got '{next_guess}'"

    def test_generate_guess(self):
        """Test the overall guess generation."""
        bot = ExampleBot()
        first_guess = bot.generate_guess()
        assert first_guess == "ABENG", f"Expected 'ABENG', got '{first_guess}'"

        bot.guesses = {GUESSES: ["ABENG"]}
        next_guess = bot.generate_guess()
        assert next_guess == "ABERS", f"Expected 'ABERS', got '{next_guess}'"
