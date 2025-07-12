"""
Module for Wordle Bot Functionality.

This module initializes the Wordle bot functionality.

It imports the BotBehaviors class, which provides methods for generating guesses,
and the BayesianBot class, which implements the bot's behavior in the game.
It also includes the ExampleBot class for demonstration purposes.
"""

from .bayesian_bot import BayesianBot
from .bot_behaviors import BotBehaviors
from .example_bot import ExampleBot
from .util import Filter
