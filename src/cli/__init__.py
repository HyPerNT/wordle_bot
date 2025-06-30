"""
Module for CLI functionality.

This module adds some CLI support.

It imports the Cli class, which is used for playing with a bot via the command-line.
It also provides a utility to dynamically select a bot from all potential implementations
"""

from .cli import Cli
from .util import get_bot_selection
