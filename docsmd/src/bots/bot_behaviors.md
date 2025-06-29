# BotBehaviors

[wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Bots](./index.md#bots) / BotBehaviors

> Auto-generated documentation for [src.bots.bot_behaviors](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot_behaviors.py) module.

## BotBehaviors

[Show source in bot_behaviors.py:16](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot_behaviors.py#L16)

A class representing the behaviors of a Wordle bot.

It manages the bot's guesses and results, and provides methods to generate guesses
and accept results from the game.

Attributes
----------
logger : logging.Logger
    A logger instance for logging bot events and errors.
filter : Filter
    An instance of Filter to manage the word list and filtering.
guesses : dict
    A dictionary to store the bot's guesses and results.
possible_words : list[str]
    A list of possible words that the bot can guess from.

#### Signature

```python
class BotBehaviors:
    def __init__(self) -> None: ...
```

### BotBehaviors().accept_result

[Show source in bot_behaviors.py:102](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot_behaviors.py#L102)

Accept the result of a guess and updates the bot's state accordingly.

This method processes the result of a guess, updates the guesses and results,
and logs the received result. If the result indicates a win or loss, it resets the bot's state.

Parameters
----------
result : dict
    A dictionary containing the result of the guess, with keys RESULT and MSG.
    RESULT is expected to be a list of numbers if the game is still ongoing, or None in a win/loss indication.
    MSG can contain additional messages or information about the result.

Returns
-------
None

#### Signature

```python
def accept_result(self, result: dict): ...
```

### BotBehaviors().generate_first_guess

[Show source in bot_behaviors.py:56](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot_behaviors.py#L56)

Code to generate the first guess.

This method should be overridden by subclasses to provide specific first guess logic.

Returns
-------
str
    The first guess word for the bot.

#### Signature

```python
def generate_first_guess(self: ignore[empty - body]) -> str: ...
```

### BotBehaviors().generate_guess

[Show source in bot_behaviors.py:82](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot_behaviors.py#L82)

Generate a guess for the bot based on the current state of guesses.

If there are no previous guesses, it generates the first guess.
Otherwise, it generates the next guess based on the previous guesses and results.

Returns
-------
str
    The generated guess word for the bot.

#### Signature

```python
def generate_guess(self) -> str: ...
```

### BotBehaviors().generate_next_guess

[Show source in bot_behaviors.py:69](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot_behaviors.py#L69)

Code to generate the next guess.

This method should be overridden by subclasses to provide specific next guess logic.
This should take into account the previous guesses and results
Returns
-------
str
    The next guess word for the bot.

#### Signature

```python
def generate_next_guess(self: ignore[empty - body]) -> str: ...
```

### BotBehaviors().reset

[Show source in bot_behaviors.py:46](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/bot_behaviors.py#L46)

Reset the bot's guesses and results.

Initialize the guesses dictionary and sets the possible words
to the complete word list.

#### Signature

```python
def reset(self) -> None: ...
```
