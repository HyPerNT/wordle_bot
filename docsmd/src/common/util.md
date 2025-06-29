# Util

[wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Common](./index.md#common) / Util

> Auto-generated documentation for [src.common.util](https://github.com/HyPerNT/wordle_bot/blob/main/src/common/util.py) module.

## boolean_comprehension

[Show source in util.py:26](https://github.com/HyPerNT/wordle_bot/blob/main/src/common/util.py#L26)

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

#### Signature

```python
def boolean_comprehension(
    list: str | list[str] | list[int], value: str | int
) -> list[int]: ...
```



## get_word_list

[Show source in util.py:47](https://github.com/HyPerNT/wordle_bot/blob/main/src/common/util.py#L47)

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

#### Signature

```python
def get_word_list() -> list[str]: ...
```



## prettify_guess

[Show source in util.py:69](https://github.com/HyPerNT/wordle_bot/blob/main/src/common/util.py#L69)

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

#### Signature

```python
def prettify_guess(guess: str, result: list[int]) -> str: ...
```



## prettify_guess_no_color

[Show source in util.py:103](https://github.com/HyPerNT/wordle_bot/blob/main/src/common/util.py#L103)

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

#### Signature

```python
def prettify_guess_no_color(guess: str, result: list[int]) -> str: ...
```
