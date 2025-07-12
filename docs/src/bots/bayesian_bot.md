# BayesianBot

[Wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Bots](./index.md#bots) / BayesianBot

> Auto-generated documentation for [src.bots.bayesian_bot](../../../src/bots/bayesian_bot.py) module.

- [BayesianBot](#bayesianbot)
  - [BayesianBot](#bayesianbot-1)
    - [BayesianBot().generate_first_guess](#bayesianbot()generate_first_guess)
    - [BayesianBot().generate_next_guess](#bayesianbot()generate_next_guess)
    - [BayesianBot().get_number_of_guesses](#bayesianbot()get_number_of_guesses)
    - [BayesianBot().guess_most_probable_from_list](#bayesianbot()guess_most_probable_from_list)
    - [BayesianBot().use_bayesian_strategy](#bayesianbot()use_bayesian_strategy)
    - [BayesianBot().use_greedy_strategy](#bayesianbot()use_greedy_strategy)

## BayesianBot

[Show source in bayesian_bot.py:15](../../../src/bots/bayesian_bot.py#L15)

A class representing a Wordle bot that generates guesses based on letter frequency and previous results.

It inherits from BotBehaviors and implements methods to generate the first guess and subsequent guesses
based on the frequency of letters and the results of previous guesses.

Attributes
----------
frequency_list : str
    A string representing the frequency of letters in the English language, ordered from most to least frequent.
MAX_WORDS : int
    The maximum number of words to allow in the search space before BayesianBot switches away from the greedy strategy.
BAYES_MIN_TURNS : int
    The minimum number of turns before BayesianBot uses the Bayesian strategy.
unique_words_set : list[str]
    The word set of the 20 most common letters in English, as disjoint and legal Wordle words.
GREEDY_MAX_TURNS : int
    The maximum number of turns the Greedy strategy will pbe played for, set to the size of the unique_words_set.

#### Signature

```python
class BayesianBot(BotBehaviors):
    def __init__(self): ...
```

### BayesianBot().generate_first_guess

[Show source in bayesian_bot.py:46](../../../src/bots/bayesian_bot.py#L46)

Generate the first guess for the Wordle game.

Parameters
----------
None

Returns
-------
str
    The first guess word for the bot, which is hardcoded to "CAGEY".

#### Signature

```python
def generate_first_guess(self) -> str: ...
```

### BayesianBot().generate_next_guess

[Show source in bayesian_bot.py:114](../../../src/bots/bayesian_bot.py#L114)

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

### BayesianBot().get_number_of_guesses

[Show source in bayesian_bot.py:91](../../../src/bots/bayesian_bot.py#L91)

Get number of guesses made.

Returns
-------
int
    Number of guesses made in this game.

#### Signature

```python
def get_number_of_guesses(self) -> int: ...
```

### BayesianBot().guess_most_probable_from_list

[Show source in bayesian_bot.py:61](../../../src/bots/bayesian_bot.py#L61)

Filter a given candidate word list based on a letter frequency list and returns first result.

Parameters
----------
candidates : list[str]
    A candidate word list.
frequency_list : str
    A string representing the order of letters to prioritize.

Returns
-------
str
    The first word from the candidate list with optimum frequency.

#### Signature

```python
def guess_most_probable_from_list(
    self, candidates: list[str], frequency_list: str
) -> str: ...
```

### BayesianBot().use_bayesian_strategy

[Show source in bayesian_bot.py:108](../../../src/bots/bayesian_bot.py#L108)

Use the Bayesian strategy.

#### Signature

```python
def use_bayesian_strategy(self) -> bool: ...
```

### BayesianBot().use_greedy_strategy

[Show source in bayesian_bot.py:102](../../../src/bots/bayesian_bot.py#L102)

Use the greedy strategy.

#### Signature

```python
def use_greedy_strategy(self) -> bool: ...
```