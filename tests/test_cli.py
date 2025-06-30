"""
Test suite for the Cli class in the cli package.

This module contains unit tests for the Cli class, which provides the command-line interface
for interacting with Wordle bots. The tests cover bot selection, guess handling, and result input.
"""

import io
from contextlib import redirect_stdout
import pytest
from bots.bot_behaviors import BotBehaviors  # type: ignore
from bots.example_bot import ExampleBot  # type: ignore
from bots.util import GUESSES, RESULTS  # type: ignore
from common.util import RESULT, get_all_subclasses  # type: ignore
from cli.cli import Cli  # type: ignore
from .cli_test_utils import string_sequence_generator  # type: ignore

# file: tests/test_cli.py


class TestCli:
    """
    Unit tests for the Cli class.

    This class tests the core functionality of the Cli interface, including bot selection,
    guess validation, result input handling, and error conditions.
    """

    game_inputs = ["GHOST", "00000"] * 6

    def test_init_bot(self, monkeypatch):
        """Test that the Cli can correctly list and select available bots."""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Find our desired option
        bots = get_all_subclasses(BotBehaviors)
        ex_bot_idx = next(
            i for i, bot in enumerate(bots) if bot.__name__ == ExampleBot.__name__
        )

        # Make generator and mock input()
        gen = string_sequence_generator([str(ex_bot_idx + 1)])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.init_bot()

        # Assertions
        assert cli.bot.__class__ is ExampleBot

    def test_init_bot_errors(self, monkeypatch):
        """Test that the Cli can correctly list and select available bots."""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Make generator and mock input()
        gen = string_sequence_generator(["-1", "banana", "1"])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.init_bot()

        # Check that the expected messages look like they're in the output
        did_error_on_bad_int = False
        did_error_on_bad_string = False
        for line in f.getvalue().splitlines():
            if "between" in line:
                did_error_on_bad_int = True
            if "Invalid" in line:
                did_error_on_bad_string = True

        assert did_error_on_bad_int
        assert did_error_on_bad_string

    def test_provide_guess(self):
        """Test that the Cli can correctly provide guesses"""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Set Cli to use ExampleBot
        cli.bot = ExampleBot()

        # Run CLI method
        with redirect_stdout(f):
            cli.provide_guess()

        # Assertions
        assert "ABENG" in f.getvalue().splitlines()[0]  # Should be first word
        assert len(cli.bot.guesses[GUESSES]) == 0  # Should have no guesses

    def test_accept_guess(self, monkeypatch):
        """Test that the Cli can corectly accept guesses"""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Set Cli to use ExampleBot
        cli.bot = ExampleBot()

        # Make generator and mock input()
        gen = string_sequence_generator(["GHOST"])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.accept_guess()

        # Assertions
        assert "GHOST" in cli.bot.guesses[GUESSES]  # Should be in bot's memory
        assert len(cli.bot.guesses[GUESSES]) == 1  # Should have one guess

    def test_accept_guess_errors(self, monkeypatch):
        """Test that the Cli can corectly handle errors when accepting guesses"""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Set Cli to use ExampleBot
        cli.bot = ExampleBot()

        # Make generator and mock input()
        gen = string_sequence_generator(["AAAAA", "GHOST"])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.accept_guess()

        did_error = False
        for line in f.getvalue().splitlines():
            if "valid" in line:
                did_error = True

        # Assertions
        assert did_error

    def test_accept_result(self, monkeypatch):
        """Test that the Cli can correctly accept results"""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Set Cli to use ExampleBot
        cli.bot = ExampleBot()

        # Make generator and mock input()
        gen = string_sequence_generator(["00000"])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.accept_result()

        # Assertions
        assert cli.bot.guesses[RESULTS][0][RESULT] == [
            0 for _ in range(5)
        ]  # Should be in bot's memory
        assert len(cli.bot.guesses[RESULTS]) == 1  # Should have one guess

    def test_accept_result_errors(self, monkeypatch):
        """Test that the Cli can correctly handle errors when accepting results"""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Set Cli to use ExampleBot
        cli.bot = ExampleBot()

        # Make generator and mock input()
        gen = string_sequence_generator(["55555", "00000"])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.accept_result()

        did_error = False
        for line in f.getvalue().splitlines():
            if "Invalid" in line:
                did_error = True

        # Assertions
        assert did_error

    def test_play_automatically(self, monkeypatch):
        """Test that the Cli can correctly play the game automatically"""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Set Cli to use ExampleBot
        cli.bot = ExampleBot()

        # Make generator and mock input()
        gen = string_sequence_generator(["ABIDE"])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.play_automatically()

        # Assertions
        assert "ABENG" in cli.wordle.guesses
        assert "ABIDE" in cli.wordle.guesses

    def test_init_session(self, monkeypatch):
        """Test that the Cli can correctly list and select available bots."""
        # Setup output mocking and new Cli instance
        f = io.StringIO()
        cli = Cli()

        # Find our desired option
        bots = get_all_subclasses(BotBehaviors)
        ex_bot_idx = next(
            i for i, bot in enumerate(bots) if bot.__name__ == ExampleBot.__name__
        )
        bot = str(ex_bot_idx + 1)

        # Make generator and mock input()
        gen = string_sequence_generator([bot, "", *self.game_inputs, "4"])
        monkeypatch.setattr("builtins.input", lambda _: next(gen))

        # Run CLI method
        with redirect_stdout(f):
            cli.init_session()

        # Assertions
        assert cli.bot.__class__ is ExampleBot
        assert cli.game_in_progress() is False
        assert cli.quit is True

        # Test if the player wants to play again with the same bot
        gen = string_sequence_generator(
            [bot, "", *self.game_inputs, "", "", *self.game_inputs, "4"]
        )
        with redirect_stdout(f):
            cli.init_session()

        assert cli.bot.__class__ is ExampleBot
        assert cli.game_in_progress() is False
        assert cli.quit is True

        # Test if the player wants to shoose a different bot and play again
        gen = string_sequence_generator(
            [bot, "", *self.game_inputs, "2", bot, "", *self.game_inputs, "4"]
        )
        with redirect_stdout(f):
            cli.init_session()

        assert cli.bot.__class__ is ExampleBot
        assert cli.game_in_progress() is False
        assert cli.quit is True

        # Test alternate exit condition
        gen = string_sequence_generator([bot, "", *self.game_inputs, "3"])
        with redirect_stdout(f):
            cli.init_session()

        assert cli.bot.__class__ is ExampleBot
        assert cli.game_in_progress() is False
        assert cli.quit is False

        # Test automatic play
        gen = string_sequence_generator([bot, "2", "MUSIC", "4"])
        with redirect_stdout(f):
            cli.init_session()

        assert cli.bot.__class__ is ExampleBot
        assert cli.wordle.game_in_progress is False
        assert cli.quit is True
