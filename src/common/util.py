"""
Utility Functions and Constants.

This module provides various utility functions and constants used throughout the Wordle bot application.

It includes functions for reading a word list, formatting guesses with ANSI color coding,
and generating boolean comprehensions for lists.
"""

import os

# File: common/util.py

RESULT = "result"
MSG = "msg"

INCORRECT_LETTER = 0
MISPLACED_LETTER = 1
CORRECT_LETTER = 2

LOG_FILE = "wordle.ansi"

ALL_CORRECT = [CORRECT_LETTER for _ in range(5)]


def boolean_comprehension(
    list: str | list[str] | list[int], value: str | int
) -> list[int]:
    """
    Returns a list of 1s and 0s where 1 indicates the value is present in the list.

    Parameters
    ----------
    list : str | list[str] | list[int]
        The list to check.
    value : str | int
        The value to check for in the list.

    Returns
    -------
    list[int]
        A list of 1s and 0s where 1 indicates the value is present.
    """
    return [1 if x == value else 0 for x in list]


def get_word_list() -> list[str]:
    """
    Read a word list from a file and returns it as a list of uppercase words.

    The file is expected to be named "wordle_word_list.txt" and located in the same
    directory as this script.

    Parameters
    ----------
    None

    Returns
    -------
    list[str]
        A list of words in uppercase.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "wordle_word_list.txt")
    with open(file_path) as f:
        return [word.strip().upper() for word in f.readlines()]


def prettify_guess(guess: str, result: list[int]) -> str:
    """
    Format a guess with ANSI color coding based on the result.

    Parameters
    ----------
    guess : str
        The guessed word.
    result : list[int]
        A list of integers representing the result of the guess, where:
        - 0 indicates an incorrect letter,
        - 1 indicates a misplaced letter,
        - 2 indicates a correct letter.

    Returns
    -------
    str
        The formatted guess with color coding.
    """
    start = "\033["
    green = "42m"
    yellow = "43m"
    end = start + "0m"
    s = ""
    for r, c in zip(result, guess):
        if r == INCORRECT_LETTER:
            s += c
        if r == CORRECT_LETTER:
            s += start + green + c + end
        if r == MISPLACED_LETTER:
            s += start + yellow + c + end
    return s + end


def prettify_guess_no_color(guess: str, result: list[int]) -> str:
    """
    Format a guess without ANSI color coding based on the result.

    Parameters
    ----------
    guess : str
        The guessed word.
    result : list[int]
        A list of integers representing the result of the guess, where:
        - 0 indicates an incorrect letter,
        - 1 indicates a misplaced letter,
        - 2 indicates a correct letter.

    Returns
    -------
    str
        The formatted guess without color coding.
    """
    return f"{guess}\t{result}"
