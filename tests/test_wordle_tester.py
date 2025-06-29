"""
Test suite for the WordleTester class.

This module contains tests for the WordleTester class, specifically for the methods
producing result strings and for running tests with a Wordle bot.
"""

from tester.wordle_tester import WordleTester  # type: ignore
from bots.example_bot import ExampleBot  # type: ignore

# file: tests/test_wordle_tester.py


class TestWordleTester:
    def test_wordle_tester(self):
        """
        Test the test method of the Tester class.
        This method runs a test with a Wordle bot and checks if the results are as expected.
        """
        tester = WordleTester()
        bot = ExampleBot()
        tester.test(bot, print_results=False)

        # Check if the results contain the expected words
        assert "ABENG" in tester.successes, "Expected 'ABENG' to be in successes"
        assert len(tester.failures) > 14_000, "Expected lots of failures in the test"

        # Check if the results string is formatted correctly
        results_str = tester.get_results_str()
        assert isinstance(results_str, str), "Results should be a string"

        # Check if the failures string is formatted correctly
        failures_str = tester.get_failures_str()
        assert isinstance(failures_str, str), "Failures should be a string"
        assert (
            "\033[0m" in failures_str
        ), "Expected ANSI escape codes in failures string"
        assert "," not in failures_str, "Expected no lists in failures string"

        # Check if the wacky failures string is formatted correctly
        wacky_failures_str = tester.get_wacky_failures_string(color=False)
        assert isinstance(wacky_failures_str, str), "Wacky failures should be a string"
        assert (
            "\033[om" not in wacky_failures_str
        ), "Expected no ANSI escape codes in wacky failures string"
        assert "," in wacky_failures_str, "Expected lists in wacky failures string"
