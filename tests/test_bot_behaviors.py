"""
Test suite for the BotBehaviors class in the bots module.

This module contains unit tests for the BotBehaviors class, ensuring that the bot's behaviors and methods work as expected.
"""

from common.util import MSG, RESULT  # type: ignore
from bots import BotBehaviors  # type: ignore
from bots.util import GUESSES, RESULTS  # type: ignore


class TestBotBehaviors:
    def test_bot_behaviors(self):
        """Test the BotBehaviors class."""
        bot_behaviors = BotBehaviors()
        assert bot_behaviors is not None
        assert hasattr(bot_behaviors, "logger")
        assert hasattr(bot_behaviors, "filter")
        assert hasattr(bot_behaviors, "guesses")
        assert isinstance(bot_behaviors.guesses, dict)
        assert hasattr(bot_behaviors, "reset")
        assert callable(bot_behaviors.reset)  # Check if the reset method exists
        assert hasattr(bot_behaviors, "generate_first_guess")
        assert callable(
            bot_behaviors.generate_first_guess
        )  # Check if the method exists
        assert hasattr(bot_behaviors, "generate_next_guess")
        assert callable(bot_behaviors.generate_next_guess)  # Check if the method exists
        assert hasattr(bot_behaviors, "generate_guess")
        assert callable(
            bot_behaviors.generate_guess
        )  # Check if the generate_guess method exists
        assert hasattr(bot_behaviors, "accept_result")
        assert callable(
            bot_behaviors.accept_result
        )  # Check if the accept_result method exists

    def test_reset(self):
        """Test the reset method."""
        bot_behaviors = BotBehaviors()
        bot_behaviors.reset()
        assert bot_behaviors.guesses[GUESSES] == []
        assert bot_behaviors.guesses[RESULTS] == []
        assert bot_behaviors.possible_words == bot_behaviors.filter.word_list

    def test_accept_result(self):
        """Test the accept_result method."""
        bot_behaviors = BotBehaviors()
        bot_behaviors.reset()
        assert bot_behaviors.guesses[GUESSES] == []
        assert bot_behaviors.guesses[RESULTS] == []
        assert bot_behaviors.possible_words == bot_behaviors.filter.word_list
        # Test with a typical result
        result = {RESULT: [2, 0, 0, 1, 1], MSG: None}
        bot_behaviors.accept_result(result)
        assert bot_behaviors.guesses[GUESSES] == []
        assert bot_behaviors.guesses[RESULTS] == [result]
        # Test with an empty result
        empty_result = {RESULT: None, MSG: None}
        bot_behaviors.accept_result(empty_result)
        assert bot_behaviors.guesses[GUESSES] == []
        assert bot_behaviors.guesses[RESULTS] == [result]
        # Test with a result that has a message
        result = {RESULT: [0 for _ in range(5)], MSG: "The message doesn't matter"}
        bot_behaviors.accept_result(result)
        assert bot_behaviors.guesses[GUESSES] == []
        assert bot_behaviors.guesses[RESULTS] == []  # Assuming the bot resets
        assert bot_behaviors.possible_words == bot_behaviors.filter.word_list
