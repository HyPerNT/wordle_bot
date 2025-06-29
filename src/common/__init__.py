"""
Module for Common Utilities.

This module provides various utility functions and constants used throughout the Wordle bot application.

It includes functions for handling word lists, formatting guesses, and defining constants related to game results.
"""

from .util import (
    RESULT,
    MSG,
    INCORRECT_LETTER,
    MISPLACED_LETTER,
    CORRECT_LETTER,
    LOG_FILE,
    ALL_CORRECT,
    boolean_comprehension,
    get_word_list,
    prettify_guess,
    prettify_guess_no_color,
)
