# WordleTester

[wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Tester](./index.md#tester) / WordleTester

> Auto-generated documentation for [src.tester.wordle_tester](https://github.com/HyPerNT/wordle_bot/blob/main/src/tester/wordle_tester.py) module.

## WordleTester

[Show source in wordle_tester.py:30](https://github.com/HyPerNT/wordle_bot/blob/main/src/tester/wordle_tester.py#L30)

A class to test a Wordle bot against a list of words.

It inherits from the Wordle class and provides methods to run tests,
collect results, and analyze the performance of the bot.

Attributes
----------
test_results : list[dict]
    A list to store the results of each test, including the word, result, and guesses.
successes : list[str]
    A list to store the words that were guessed correctly by the bot.
failures : list[str]
    A list to store the words that were not guessed correctly by the bot.
logger : logging.Logger
    A logger instance for logging test events and errors.

#### Signature

```python
class WordleTester(Wordle):
    def __init__(self) -> None: ...
```

### WordleTester().get_failure_str

[Show source in wordle_tester.py:175](https://github.com/HyPerNT/wordle_bot/blob/main/src/tester/wordle_tester.py#L175)

Generate a formatted string for a single failure, including the word, the guesses made, and the results of those guesses.

Parameters
----------
r : dict
    A dictionary containing the word, guesses, and results for a single test.
color : bool, optional
    If True, the output will be formatted with colors for better readability.
    Defaults to True.

Returns
-------
str
    A formatted string containing the details of the failure, including the word,
    guesses, and results.

#### Signature

```python
def get_failure_str(self, r: dict, color: bool = True) -> str: ...
```

### WordleTester().get_failures_str

[Show source in wordle_tester.py:149](https://github.com/HyPerNT/wordle_bot/blob/main/src/tester/wordle_tester.py#L149)

Generate a detailed string of the failures encountered during the tests.

This includes the words that were not guessed correctly, the guesses made,
and the results of those guesses.

Parameters
----------
color : bool, optional
    If True, the output will be formatted with colors for better readability.
    Defaults to True.

Returns
-------
str
    A formatted string containing details of the failures, including the words,
    guesses, and results.

#### Signature

```python
def get_failures_str(self, color: bool = True) -> str: ...
```

### WordleTester().get_results_str

[Show source in wordle_tester.py:110](https://github.com/HyPerNT/wordle_bot/blob/main/src/tester/wordle_tester.py#L110)

Generate a summary string of the test results, including the number of correct and incorrect guesses, success rates, and failure details.

Returns
-------
str
    A formatted string summarizing the test results, including success and failure rates,
    average guesses per success, and details of incorrect guesses.

#### Signature

```python
def get_results_str(self) -> str: ...
```

### WordleTester().get_wacky_failures_string

[Show source in wordle_tester.py:199](https://github.com/HyPerNT/wordle_bot/blob/main/src/tester/wordle_tester.py#L199)

Generate a string containing details of failures that include misplaced letters.

This method filters the test results to include only those where the last result
contains misplaced letters, and formats the output accordingly.

Parameters
----------
color : bool, optional
    If True, the output will be formatted with colors for better readability.
    Defaults to True.

Returns
-------
str
    A formatted string containing details of failures with misplaced letters,
    including the words, guesses, and results.

#### Signature

```python
def get_wacky_failures_string(self, color: bool = True) -> str: ...
```

### WordleTester().test

[Show source in wordle_tester.py:61](https://github.com/HyPerNT/wordle_bot/blob/main/src/tester/wordle_tester.py#L61)

Runs tests on the bot using a predefined list of words.

It iterates through each word in the word list, starts a new game,
sets the secret word, and allows the bot to make guesses until the game is over.
The results of each test are collected and stored in the test_results list.

Parameters
----------
bot : BotBehaviors
    An instance of a bot that inherits from BotBehaviors.
    This bot will generate guesses and accept results based on the game's feedback.
print_results : bool, optional
    If True, the results of the tests will be printed to the console.
    Defaults to True.
print_failures : bool, optional
    If True, additionally prints out failed words in the style of Wordle.
    Defaults to False.

#### Signature

```python
def test(
    self, bot: BotBehaviors, print_results: bool = True, print_failures=False
) -> None: ...
```
