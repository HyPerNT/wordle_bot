# Util

[Wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Bots](./index.md#bots) / Util

> Auto-generated documentation for [src.bots.util](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py) module.

- [Util](#util)
  - [Filter](#filter)
    - [Filter().filter_compatible_with_guess](#filter()filter_compatible_with_guess)
    - [Filter().filter_compatible_with_past_guesses](#filter()filter_compatible_with_past_guesses)
    - [Filter().filter_containing_letter](#filter()filter_containing_letter)
    - [Filter().filter_containing_letter_at](#filter()filter_containing_letter_at)
    - [Filter().filter_not_containing_letter](#filter()filter_not_containing_letter)
    - [Filter().filter_not_containing_letter_at](#filter()filter_not_containing_letter_at)
    - [Filter().filter_unique_letters](#filter()filter_unique_letters)
    - [Filter().has_all_unique_letters](#filter()has_all_unique_letters)
    - [Filter().is_letter_possible](#filter()is_letter_possible)
    - [Filter().is_valid_word](#filter()is_valid_word)

## Filter

[Show source in util.py:25](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L25)

A class that provides various filtering methods for word lists used in Wordle games.

It includes methods to check for unique letters, filter words based on letter presence,
and filter words based on previous guesses and results.

Attributes
----------
logger : logging.Logger
    A logger instance for logging filtering events and errors.
word_list : list[str]
    A list of valid words that can be used in the game.
all_unique_words : list[str]
    A list of words that contain all unique letters, derived from the word list.

#### Signature

```python
class Filter:
    def __init__(self) -> None: ...
```

### Filter().filter_compatible_with_guess

[Show source in util.py:189](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L189)

Filter a list of words based on a guess and the result of that guess.

The result is expected to be a dictionary with a key 'result' that contains a list of responses
corresponding to each letter in the guess. The responses can be:
- CORRECT_LETTER: The letter is in the correct position.
- MISPLACED_LETTER: The letter is in the word but in the wrong position.
- INCORRECT_LETTER: The letter is not in the word at all

Parameters
----------
words : list[str]
    A list of words to filter based on the guess and result.
guess : str
    The guessed word to compare against the words in the list.
result : dict
    A dictionary containing the result of the guess, with a key 'result' that holds a
    list of responses for each letter in the guess.

Returns
-------
list[str]
    A list of words that are compatible with the guess and result.

#### Signature

```python
def filter_compatible_with_guess(
    self, words: list[str], guess: str, result: dict
) -> list[str]: ...
```

### Filter().filter_compatible_with_past_guesses

[Show source in util.py:236](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L236)

Filter a list of words based on multiple past guesses and their results.

This method iterates through all past guesses and their corresponding results,
filtering the list of words to retain only those that are compatible with all guesses.

Parameters
----------
words : list[str]
    A list of words to filter based on the past guesses and results.
guesses : dict
    A dictionary containing past guesses and their results, with keys 'words' and 'results'.
    'words' is a list of guessed words, and 'results' is a list of dictionaries containing
    the result for each guess.

Returns
-------
list[str]
    A list of words that are compatible with all past guesses and results.

#### Signature

```python
def filter_compatible_with_past_guesses(
    self, words: list[str], guesses: dict
) -> list[str]: ...
```

### Filter().filter_containing_letter

[Show source in util.py:109](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L109)

Filter a list of words to include only those that contain a specific letter.

Parameters
----------
words : list[str]
    A list of words to filter.
letter : str
    The letter to check for in the words.

Returns
-------
list[str]
    A list of words that contain the specified letter.

#### Signature

```python
def filter_containing_letter(self, words: list[str], letter: str) -> list[str]: ...
```

### Filter().filter_containing_letter_at

[Show source in util.py:145](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L145)

Filter a list of words to include only those that contain a specific letter at a specific index.

Parameters
----------
words : list[str]
    A list of words to filter.
letter : str
    The letter to check for in the words.
index : int
    The index at which the letter should be present in the words.

Returns
-------
list[str]
    A list of words that contain the specified letter at the specified index.

#### Signature

```python
def filter_containing_letter_at(
    self, words: list[str], letter: str, index: int
) -> list[str]: ...
```

### Filter().filter_not_containing_letter

[Show source in util.py:127](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L127)

Filter a list of words to exclude those that contain a specific letter.

Parameters
----------
words : list[str]
    A list of words to filter.
letter : str
    The letter to check for in the words.

Returns
-------
list[str]
    A list of words that do not contain the specified letter.

#### Signature

```python
def filter_not_containing_letter(self, words: list[str], letter: str) -> list[str]: ...
```

### Filter().filter_not_containing_letter_at

[Show source in util.py:167](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L167)

Filter a list of words to exclude those that contain a specific letter at a specific index.

Parameters
----------
words : list[str]
    A list of words to filter.
letter : str
    The letter to check for in the words.
index : int
    The index at which the letter should not be present in the words.

Returns
-------
list[str]
    A list of words that do not contain the specified letter at the specified index.

#### Signature

```python
def filter_not_containing_letter_at(
    self, words: list[str], letter: str, index: int
) -> list[str]: ...
```

### Filter().filter_unique_letters

[Show source in util.py:263](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L263)

Filter a list of words to include only those that have all unique letters.

Parameters
----------
words : list[str]
    A list of words to filter.

Returns
-------
list[str]
    A list of words that contain all unique letters.

#### Signature

```python
def filter_unique_letters(self, words: list[str]) -> list[str]: ...
```

### Filter().has_all_unique_letters

[Show source in util.py:54](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L54)

Check if a word contains all unique letters.

A word is considered to have all unique letters if no letter appears more than once.

Parameters
----------
word : str
    The word to check for unique letters.

Returns
-------
bool
    True if the word has all unique letters, False otherwise.

#### Signature

```python
def has_all_unique_letters(self, word: str) -> bool: ...
```

### Filter().is_letter_possible

[Show source in util.py:75](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L75)

Check if a letter is present in any of the words in the list.

Parameters
----------
words : list[str]
    A list of words to check.
letter : str
    The letter to check for presence in the words.

Returns
-------
bool
    True if the letter is present in any of the words, False otherwise.

#### Signature

```python
def is_letter_possible(self, words: list[str], letter: str) -> bool: ...
```

### Filter().is_valid_word

[Show source in util.py:93](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/util.py#L93)

Check if a word is valid by verifying its presence in the word list.

Parameters
----------
word : str
    The word to check for validity.

Returns
-------
bool
    True if the word is in the word list, False otherwise.

#### Signature

```python
def is_valid_word(self, word: str) -> bool: ...
```