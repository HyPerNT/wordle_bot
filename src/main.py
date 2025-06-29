"""
Main script to run the Wordle bot tests.

This script initializes the Wordle bot and runs the tests defined in the Tester class.
It also ensures that the log file is removed before starting the tests to avoid appending to an
existing log file.
"""

from tester import WordleTester
from bots import WordleBot
from common.util import LOG_FILE
import os

# file: src/main.py


def main():
    """Main function to run the Wordle bot tests."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    WordleTester().test(WordleBot())


if __name__ == "__main__":
    """Entry point for the script."""
    main()
