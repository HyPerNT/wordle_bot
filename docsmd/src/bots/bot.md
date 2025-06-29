# Bot

[wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Bots](./index.md#bots) / Bot

> Auto-generated documentation for [src.bots.bot](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot.py) module.

## WordleBot

[Show source in bot.py:15](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot.py#L15)

A class representing a Wordle bot that generates guesses based on letter frequency and previous results.

It inherits from BotBehaviors and implements methods to generate the first guess and subsequent guesses
based on the frequency of letters and the results of previous guesses.

Attributes
----------
frequency_list : str
    A string representing the frequency of letters in the English language, ordered from most to least frequent.
MAX_LETTERS : int
    The maximum number of unique letters to try for in guessing.

#### Signature

```python
class WordleBot(BotBehaviors):
    def __init__(self): ...
```

### WordleBot().generate_first_guess

[Show source in bot.py:37](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot.py#L37)

Generate the first guess for the Wordle game.

Parameters
----------
None

Returns
-------
str
    The first guess word for the bot, which is hardcoded to "GHOST".

#### Signature

```python
def generate_first_guess(self) -> str: ...
```

### WordleBot().generate_next_guess

[Show source in bot.py:52](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot.py#L52)

Generate the next guess for the Wordle game based on previous guesses and results.

This method filters the list of possible words based on the last guess and its result,
and then selects the next guess based on letter frequency and uniqueness.
Uniqueness is prioritized to avoid repeated letters in the guess.

Parameters
----------
None

Returns
-------
str
    The next guess word for the bot, selected from the filtered list of possible words.

#### Signature

```python
def generate_next_guess(self) -> str: ...
```
