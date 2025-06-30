# Cli

[Wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Cli](./index.md#cli) / Cli

> Auto-generated documentation for [src.cli.cli](../../../src/cli/cli.py) module.

- [Cli](#cli)
  - [Cli](#cli-1)
    - [Cli().accept_guess](#cli()accept_guess)
    - [Cli().accept_result](#cli()accept_result)
    - [Cli().game_in_progress](#cli()game_in_progress)
    - [Cli().get_valid_word](#cli()get_valid_word)
    - [Cli().init_bot](#cli()init_bot)
    - [Cli().init_session](#cli()init_session)
    - [Cli().play](#cli()play)
    - [Cli().play_automatically](#cli()play_automatically)
    - [Cli().play_interactively](#cli()play_interactively)
    - [Cli().provide_guess](#cli()provide_guess)

## Cli

[Show source in cli.py:24](../../../src/cli/cli.py#L24)

Command-line interface for Wordle bots.

This class manages user interaction for playing Wordle with different bot behaviors.
It handles bot selection, game flow, user guesses, and result input.

#### Signature

```python
class Cli:
    def __init__(self): ...
```

### Cli().accept_guess

[Show source in cli.py:130](../../../src/cli/cli.py#L130)

Accept a guess from the user, validate, and update bot state.

#### Signature

```python
def accept_guess(self): ...
```

### Cli().accept_result

[Show source in cli.py:147](../../../src/cli/cli.py#L147)

Prompt user for result of guess and update bot state.

#### Signature

```python
def accept_result(self): ...
```

### Cli().game_in_progress

[Show source in cli.py:38](../../../src/cli/cli.py#L38)

Determine whether a game is in progress.

Returns
-------
bool
    False if the game is over, True otherwise

#### Signature

```python
def game_in_progress(self) -> bool: ...
```

### Cli().get_valid_word

[Show source in cli.py:135](../../../src/cli/cli.py#L135)

Accept a word from the user, testing if it is valid before returning.

#### Signature

```python
def get_valid_word(self) -> str: ...
```

### Cli().init_bot

[Show source in cli.py:53](../../../src/cli/cli.py#L53)

Prompt user for bot to use and set class instance to that selection.

#### Signature

```python
def init_bot(self) -> None: ...
```

### Cli().init_session

[Show source in cli.py:115](../../../src/cli/cli.py#L115)

Initialize a new game session.

#### Signature

```python
def init_session(self) -> None: ...
```

### Cli().play

[Show source in cli.py:79](../../../src/cli/cli.py#L79)

Play a game with the user, repeatedly prompting for new games or new bots.

#### Signature

```python
def play(self) -> None: ...
```

### Cli().play_automatically

[Show source in cli.py:68](../../../src/cli/cli.py#L68)

Play a game a automatically with the user, prompting for a secret word and running the game.

#### Signature

```python
def play_automatically(self) -> None: ...
```

### Cli().play_interactively

[Show source in cli.py:59](../../../src/cli/cli.py#L59)

Play a game interactively with the user, prompting for guesses and results.

#### Signature

```python
def play_interactively(self) -> None: ...
```

### Cli().provide_guess

[Show source in cli.py:120](../../../src/cli/cli.py#L120)

Provide the bot's next guess to the user.

#### Signature

```python
def provide_guess(self): ...
```