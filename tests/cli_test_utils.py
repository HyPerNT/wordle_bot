"""
Test Utilities for the CLI.

A set of test utilities useful for mocking CLI interactions.
"""

from typing import Generator

# file: tests/cli_test_utils.py


def string_sequence_generator(inputs: list[str]) -> Generator:
    """Yield each input string to mock input()."""
    for value in inputs:
        yield value
