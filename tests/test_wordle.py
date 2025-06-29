"""
Test suite for the Wordle class in the bots module.

This module contains unit tests for the Wordle class, ensuring that the game logic works as expected.
"""

from common.util import MSG, RESULT  # type: ignore
from wordle import Wordle  # type: ignore

# file: tests/test_wordle.py


class TestWordle:
    def test_wordle_start(self):
        """Test the Wordle class initialization and methods."""
        wordle = Wordle()
        assert wordle is not None
        assert hasattr(wordle, "secret_word")
        assert (
            wordle.secret_word == ""
        )  # Assuming the secret word is set to an empty string initially
        assert hasattr(wordle, "turns_taken")
        assert wordle.turns_taken == 0
        assert hasattr(wordle, "game_in_progress")
        assert not wordle.game_in_progress
        assert hasattr(wordle, "guesses")
        assert wordle.guesses == []
        assert hasattr(wordle, "results")
        assert wordle.results == []
        assert hasattr(wordle, "word_list")
        assert isinstance(wordle.word_list, list)
        assert len(wordle.word_list) == 14855  # Assuming the word list is complete
        assert hasattr(wordle, "logger")
        assert hasattr(wordle, "generate_word")
        assert callable(wordle.generate_word)
        assert hasattr(wordle, "get_all_indices")
        assert callable(wordle.get_all_indices)
        assert hasattr(wordle, "is_misplaced_letter")
        assert callable(wordle.is_misplaced_letter)
        assert hasattr(wordle, "check_error_conditions")
        assert callable(wordle.check_error_conditions)
        assert hasattr(wordle, "guess")
        assert callable(wordle.guess)
        assert hasattr(wordle, "start_game")
        assert callable(wordle.start_game)

    def test_generate_word(self):
        """Test the generate_word method."""
        wordle = Wordle()
        word = wordle.generate_word()
        assert isinstance(word, str)
        assert len(word) == 5
        assert word == word.upper()
        assert word in wordle.word_list

    def test_get_all_indices(self):
        """Test the get_all_indices method."""
        wordle = Wordle()
        indices = wordle.get_all_indices([0, 1, 0, 1, 1])
        assert isinstance(indices, list)
        assert indices == [1, 3, 4]
        indices = wordle.get_all_indices([0, 0, 0, 0, 0])
        assert indices == []

    def test_is_misplaced_letter(self):
        """Test the is_misplaced_letter method."""
        wordle = Wordle()
        wordle.secret_word = "APPLE"
        result = [2, 2, 2, 2, 0]  # Some letters correct
        guess = "APPLY"
        assert wordle.is_misplaced_letter("A", guess, result, 0) is False
        assert wordle.is_misplaced_letter("P", guess, result, 1) is False
        assert wordle.is_misplaced_letter("P", guess, result, 2) is False
        assert wordle.is_misplaced_letter("L", guess, result, 3) is False
        assert wordle.is_misplaced_letter("Y", guess, result, 4) is False
        guess = "TOTAL"
        result = [0, 0, 0, 0, 0]  # All letters incorrect
        assert wordle.is_misplaced_letter("T", guess, result, 0) is False
        assert wordle.is_misplaced_letter("O", guess, result, 1) is False
        assert wordle.is_misplaced_letter("T", guess, result, 2) is False
        assert wordle.is_misplaced_letter("A", guess, result, 3) is True
        assert wordle.is_misplaced_letter("L", guess, result, 4) is True

    def test_check_error_conditions(self):
        """Test the check_error_conditions method."""
        wordle = Wordle()
        wordle.secret_word = "APPLE"
        assert wordle.check_error_conditions("APPLE") == {
            RESULT: None,
            MSG: "Game not started!",
        }
        wordle.game_in_progress = True
        assert wordle.check_error_conditions("BANANA") == {
            RESULT: None,
            MSG: "Not a valid word!",
        }
        assert wordle.check_error_conditions("APPLE") == {RESULT: None, MSG: None}

    def test_guess(self):
        """Test the guess method."""
        wordle = Wordle()
        wordle.secret_word = "APPLE"
        wordle.game_in_progress = True
        assert wordle.guess("APPLE") == {RESULT: [2, 2, 2, 2, 2], MSG: "You win!"}
        assert wordle.turns_taken == 1
        assert wordle.guesses == ["APPLE"]
        assert wordle.results == [[2, 2, 2, 2, 2]]

        # Test an incorrect guess
        wordle.start_game()
        wordle.secret_word = "APPLE"
        result = wordle.guess("TOTAL")
        assert result[RESULT] == [0, 0, 0, 1, 1]  # Assuming 'A' and 'L' are misplaced
        assert result[MSG] is None
        assert wordle.guesses == ["TOTAL"]
        assert wordle.results == [[0, 0, 0, 1, 1]]
        assert wordle.turns_taken == 1

        # Test another incorrect guess
        result = wordle.guess("PLATE")
        assert result[RESULT] == [1, 1, 1, 0, 2]
        assert result[MSG] is None
        assert wordle.guesses == ["TOTAL", "PLATE"]
        assert wordle.results == [[0, 0, 0, 1, 1], [1, 1, 1, 0, 2]]
        assert wordle.turns_taken == 2
        assert wordle.game_in_progress

        # Test a win condition
        result = wordle.guess("APPLE")
        assert result[RESULT] == [2, 2, 2, 2, 2]
        assert result[MSG] == "You win!"
        assert wordle.guesses == ["TOTAL", "PLATE", "APPLE"]
        assert wordle.results == [[0, 0, 0, 1, 1], [1, 1, 1, 0, 2], [2, 2, 2, 2, 2]]
        assert wordle.turns_taken == 3
        assert not wordle.game_in_progress

        # Test a near-loss condition
        wordle.start_game()
        wordle.secret_word = "APPLE"
        for _ in range(5):
            wordle.guess("PLATE")
        result = wordle.guess("APPLE")
        assert result[RESULT] == [2, 2, 2, 2, 2]
        assert result[MSG] == "You win!"
        assert wordle.turns_taken == 6
        assert not wordle.game_in_progress

        # Test a loss condition
        wordle.start_game()
        wordle.secret_word = "APPLE"
        for _ in range(5):
            wordle.guess("PLATE")
        result = wordle.guess("PLATE")
        assert result[RESULT] == [1, 1, 1, 0, 2]
        assert result[MSG] == "You lost!"
        assert wordle.turns_taken == 6
        assert not wordle.game_in_progress

    def test_start_game(self):
        """Test the start_game method."""
        wordle = Wordle()
        wordle.start_game()
        assert wordle.secret_word != ""
        assert wordle.turns_taken == 0
        assert wordle.game_in_progress is True
        assert wordle.guesses == []
        assert wordle.results == []
        assert wordle.secret_word in wordle.word_list
        assert len(wordle.secret_word) == 5
        assert wordle.secret_word.isupper()  # Assuming the secret word is uppercase
