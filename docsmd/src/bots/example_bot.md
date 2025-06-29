# ExampleBot

[wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Bots](./index.md#bots) / ExampleBot

> Auto-generated documentation for [src.bots.example_bot](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/example_bot.py) module.

## ExampleBot

[Show source in example_bot.py:15](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/example_bot.py#L15)

A class representing a simple Wordle bot that generates guesses based on a predefined list of unique words.

It inherits from BotBehaviors and implements methods to generate the first guess and subsequent guesses
based on the index of previous guesses.

Attributes
----------
filter : BotBehaviors
    An instance of BotBehaviors that provides methods for filtering and generating guesses.

#### Signature

```python
class ExampleBot(BotBehaviors):
    def __init__(self): ...
```

### ExampleBot().generate_first_guess

[Show source in example_bot.py:33](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/example_bot.py#L33)

Generate the first guess for the Wordle game.

Returns
-------
str
    The first guess word for the bot, which is the first unique word in the list.

#### Signature

```python
def generate_first_guess(self) -> str: ...
```

### ExampleBot().generate_next_guess

[Show source in example_bot.py:44](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/example_bot.py#L44)

Generate the next guess for the Wordle game based on the number of previous guesses.

This method selects the next guess from the list of unique words based on the index of previous guesses.

Returns
-------
str
    The next guess word for the bot, selected from the list of unique words.

#### Signature

```python
def generate_next_guess(self) -> str: ...
```
