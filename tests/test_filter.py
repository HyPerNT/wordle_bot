"""
Test suite for the Filter class in the bots module.

This module contains unit tests for the Filter class, ensuring that the filtering methods work as expected.
"""

from common.util import RESULT  # type: ignore
from bots import Filter  # type: ignore
from bots.util import GUESSES, RESULTS  # type: ignore

# file: tests/test_filter.py


class TestFilter:
    """
    Unit tests for the Filter class.

    This class tests the core functionality of the Filter class,
    ensuring that all provided methods behave as expected.
    """

    def test_filter(self):
        """Test the Filter class."""
        filter_instance = Filter()
        assert filter_instance is not None
        assert hasattr(filter_instance, "word_list")
        assert isinstance(filter_instance.word_list, list)
        assert len(filter_instance.word_list) > 0  # Assuming the word list is not empty
        assert hasattr(filter_instance, "all_unique_words")
        assert isinstance(filter_instance.all_unique_words, list)
        assert (
            len(filter_instance.all_unique_words) > 0
        )  # Assuming there are unique words
        assert hasattr(filter_instance, "has_all_unique_letters")
        assert callable(
            filter_instance.has_all_unique_letters
        )  # Check if the method exists
        assert hasattr(filter_instance, "is_letter_possible")
        assert callable(
            filter_instance.is_letter_possible
        )  # Check if the method exists
        assert hasattr(filter_instance, "is_valid_word")
        assert callable(filter_instance.is_valid_word)  # Check if the method exists
        assert hasattr(filter_instance, "filter_containing_letter")
        assert callable(
            filter_instance.filter_containing_letter
        )  # Check if the method exists
        assert hasattr(filter_instance, "filter_not_containing_letter")
        assert callable(
            filter_instance.filter_not_containing_letter
        )  # Check if the method exists
        assert hasattr(filter_instance, "filter_containing_letter_at")
        assert callable(
            filter_instance.filter_containing_letter_at
        )  # Check if the method exists
        assert hasattr(filter_instance, "filter_not_containing_letter_at")
        assert callable(
            filter_instance.filter_not_containing_letter_at
        )  # Check if the method exists
        assert hasattr(filter_instance, "filter_compatible_with_guess")
        assert callable(
            filter_instance.filter_compatible_with_guess
        )  # Check if the method exists
        assert hasattr(filter_instance, "filter_compatible_with_past_guesses")
        assert callable(
            filter_instance.filter_compatible_with_past_guesses
        )  # Check if the method exists
        assert hasattr(filter_instance, "filter_unique_letters")
        assert callable(
            filter_instance.filter_unique_letters
        )  # Check if the method exists

    def test_has_all_unique_letters(self):
        """Test the has_all_unique_letters method."""
        filter_instance = Filter()
        assert filter_instance.has_all_unique_letters("APPLE") is False
        assert filter_instance.has_all_unique_letters("WORLD") is True
        assert filter_instance.has_all_unique_letters("THERE") is False

    def test_is_letter_possible(self):
        """Test the is_letter_possible method."""
        filter_instance = Filter()
        words = ["APPLE", "WORLD", "THERE"]
        assert filter_instance.is_letter_possible(words, "A") is True
        assert filter_instance.is_letter_possible(words, "Z") is False

    def test_is_valid_word(self):
        """Test the is_valid_word method."""
        filter_instance = Filter()
        assert filter_instance.is_valid_word("APPLE") is True
        assert filter_instance.is_valid_word("WORLD") is True
        assert filter_instance.is_valid_word("THERE") is True
        assert filter_instance.is_valid_word("INVALID") is False

    def test_filter_containing_letter(self):
        """Test the filter_containing_letter method."""
        filter_instance = Filter()
        words = ["APPLE", "WORLD", "THERE"]
        filtered_words = filter_instance.filter_containing_letter(words, "A")
        assert filtered_words == ["APPLE"]
        filtered_words = filter_instance.filter_containing_letter(words, "Z")
        assert filtered_words == []
        filtered_words = filter_instance.filter_containing_letter(words, "E")
        assert filtered_words == ["APPLE", "THERE"]

    def test_filter_not_containing_letter(self):
        """Test the filter_not_containing_letter method."""
        filter_instance = Filter()
        words = ["APPLE", "WORLD", "THERE"]
        filtered_words = filter_instance.filter_not_containing_letter(words, "A")
        assert filtered_words == ["WORLD", "THERE"]
        filtered_words = filter_instance.filter_not_containing_letter(words, "Z")
        assert filtered_words == ["APPLE", "WORLD", "THERE"]
        filtered_words = filter_instance.filter_not_containing_letter(words, "E")
        assert filtered_words == ["WORLD"]

    def test_filter_containing_letter_at(self):
        """Test the filter_containing_letter_at method."""
        filter_instance = Filter()
        words = ["APPLE", "WORLD", "THERE"]
        filtered_words = filter_instance.filter_containing_letter_at(words, "A", 0)
        assert filtered_words == ["APPLE"]
        filtered_words = filter_instance.filter_containing_letter_at(words, "O", 1)
        assert filtered_words == ["WORLD"]
        filtered_words = filter_instance.filter_containing_letter_at(words, "E", 4)
        assert filtered_words == ["APPLE", "THERE"]
        filtered_words = filter_instance.filter_containing_letter_at(words, "Z", 0)
        assert filtered_words == []

    def test_filter_not_containing_letter_at(self):
        """Test the filter_not_containing_letter_at method."""
        filter_instance = Filter()
        words = ["APPLE", "WORLD", "THERE"]
        filtered_words = filter_instance.filter_not_containing_letter_at(words, "A", 0)
        assert filtered_words == ["WORLD", "THERE"]
        filtered_words = filter_instance.filter_not_containing_letter_at(words, "O", 1)
        assert filtered_words == ["APPLE", "THERE"]
        filtered_words = filter_instance.filter_not_containing_letter_at(words, "E", 4)
        assert filtered_words == ["WORLD"]
        filtered_words = filter_instance.filter_not_containing_letter_at(words, "Z", 0)
        assert filtered_words == ["APPLE", "WORLD", "THERE"]

    def test_filter_compatible_with_guess(self):
        """Test the filter_compatible_with_guess method."""
        filter_instance = Filter()
        words = ["APPLE", "WORLD", "THERE"]
        guess = "APPLE"
        result = {RESULT: [2, 2, 2, 2, 2]}
        filtered_words = filter_instance.filter_compatible_with_guess(
            words, guess, result
        )
        assert filtered_words == ["APPLE"]
        guess = "WORLD"
        result = {RESULT: [0, 0, 0, 0, 0]}
        filtered_words = filter_instance.filter_compatible_with_guess(
            words, guess, result
        )
        assert filtered_words == []  # Assuming all letters are incorrect
        guess = "THERE"
        result = {RESULT: [0, 0, 0, 1, 0]}
        filtered_words = filter_instance.filter_compatible_with_guess(
            words, guess, result
        )
        assert filtered_words == ["WORLD"]  # Assuming 'R' is misplaced
        guess = "APPLE"
        result = {RESULT: [0, 0, 0, 0, 2]}
        filtered_words = filter_instance.filter_compatible_with_guess(
            words, guess, result
        )
        assert filtered_words == ["THERE"]  # Assuming 'E' is correect

    def test_filter_compatible_with_past_guesses(self):
        """Test the filter_compatible_with_past_guesses method."""
        filter_instance = Filter()
        # Assuming the first guess filters to 'APPLE' and the second guess filters out all words
        words = ["APPLE", "WORLD", "THERE"]
        guesses = {
            GUESSES: ["APPLE", "WORLD"],
            RESULTS: [{RESULT: [2, 0, 0, 1, 1]}, {RESULT: [0, 0, 0, 0, 0]}],
        }
        filtered_words = filter_instance.filter_compatible_with_past_guesses(
            words, guesses
        )
        assert filtered_words == []

    def test_filter_unique_letters(self):
        """Test the filter_unique_letters method."""
        filter_instance = Filter()
        words = ["APPLE", "WORLD", "THERE", "HELLO"]
        filtered_words = filter_instance.filter_unique_letters(words)
        assert filtered_words == ["WORLD"]
