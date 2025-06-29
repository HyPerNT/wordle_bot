# Wordle

[wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Wordle](./index.md#wordle) / Wordle

> Auto-generated documentation for [src.wordle.wordle](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py) module.

## Wordle

[Show source in wordle.py:27](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py#L27)

A class representing a Wordle game.

It manages the game state, including the secret word, guesses, and results.
It provides methods to start the game, make guesses, and check for errors.

Attributes
----------
turns_taken : int
    The number of turns taken in the current game.
game_in_progress : bool
    Indicates whether a game is currently in progress.
guesses : list[str]
    A list of words guessed by the player.
results : list[list[int]]
    A list of results corresponding to each guess, where each result is a list of integers
    representing the status of each letter in the guess (correct, misplaced, or incorrect).
word_list : list[str]
    A list of valid words that can be used in the game.
logger : logging.Logger
    A logger instance for logging game events and errors.

Methods
-------
generate_word() -> str
    Generate a random word from the word list to be used as the secret word for the game
get_all_indices(list: list[int]) -> list[int]
    Returns a list of indices where the value is 1 in the given list.
is_misplaced_letter(letter: str, word: str, result: list[int], index: int) -> bool
    Check if a letter in the guessed word is misplaced compared to the secret word.
check_error_conditions(word: str) -> dict
    Check for error conditions before making a guess and returns a dictionary with the result and message.
guess(word: str) -> dict
    Process a guess, updates the game state, and returns the result of the guess.
start_game() -> None
    Initialize a new game by selecting a secret word and resetting the game state.

#### Signature

```python
class Wordle:
    def __init__(self) -> None: ...
```

### Wordle().check_error_conditions

[Show source in wordle.py:167](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py#L167)

Check for error conditions before making a guess.

This method verifies if the game is in progress and if the guessed word is valid.

Parameters
----------
word : str
    The word to be guessed.

Returns
-------
dict
    A dictionary containing the result and a message.
    If there are no errors, the result is None and the message is None.
    If there are errors, the result is None and the message describes the error.

#### Signature

```python
def check_error_conditions(self, word: str) -> dict: ...
```

### Wordle().generate_word

[Show source in wordle.py:87](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py#L87)

Select a random word from the word list to be used as the secret word for the game.

Parameters
----------
None

Returns
-------
str
    A randomly selected word from the word list.

#### Signature

```python
def generate_word(self) -> str: ...
```

### Wordle().get_all_indices

[Show source in wordle.py:102](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py#L102)

Returns a list of indices where the value is 1 in the given list.

This is used to find the positions of correct letters in the result list.

Parameters
----------
list : list[int]
    A list of integers where 1 indicates the presence of a correct letter.

Returns
-------
list[int]
    A list of indices where the value is 1 in the input list.

#### Signature

```python
def get_all_indices(self, list: list[int]) -> list[int]: ...
```

### Wordle().guess

[Show source in wordle.py:193](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py#L193)

Process a guess, updates the game state, and returns the result of the guess.

This method checks for error conditions, compares the guessed word with the secret word,
and updates the results accordingly. It also checks if the player has won or lost the game.

Parameters
----------
word : str
    The word guessed by the player.

Returns
-------
dict
    A dictionary containing the result of the guess and a message.
    If the guess is valid, the result is a list indicating the status of each letter
    (correct, misplaced, or incorrect). If the player wins, the message indicates a win.
    If the player loses, the message indicates a loss.
    If there are errors, the result is None and the message describes the error.

#### Signature

```python
def guess(self, word: str) -> dict: ...
```

### Wordle().is_misplaced_letter

[Show source in wordle.py:120](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py#L120)

Check if a letter in the guessed word is misplaced compared to the secret word.

A letter is considered misplaced if it exists in the secret word but is not in the correct position
and the number of occurrences in the secret word is greater than or equal to the number of
occurrences in the guessed word up to the current index.

Parameters
----------
letter : str
    The letter to check for being misplaced.
word : str
    The guessed word.
result : list[int]
    The result of the previous guesses, where each element indicates the status of each letter
    (correct or incorrect).
index : int
    The current index in the guessed word being checked.

Returns
-------
bool
    True if the letter is misplaced, False otherwise.

#### Signature

```python
def is_misplaced_letter(
    self, letter: str, word: str, result: list[int], index: int
) -> bool: ...
```

### Wordle().start_game

[Show source in wordle.py:249](https://github.com/HyPerNT/wordle_bot/blob/main/src/wordle/wordle.py#L249)

Initialize a new game by selecting a secret word and resetting the game state.

This method sets the secret word to a randomly generated word from the word list,
resets the game in progress flag to True, and clears the guesses and results lists.

Parameters
----------
None

Returns
-------
None

#### Signature

```python
def start_game(self) -> None: ...
```
