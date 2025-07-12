# Util

[wordle_bot Index](../../README.md#wordle_bot-index) / `src` / [Cli](./index.md#cli) / Util

> Auto-generated documentation for [src.cli.util](https://github.com/HyPerNT/wordle_bot/blob/main/src/cli/util.py) module.

## get_bot_selection

[Show source in util.py:12](https://github.com/HyPerNT/wordle_bot/blob/main/src/cli/util.py#L12)

Get the desired bot of many implementations from the user.

Parameters
----------
bots : list[BotBehaviors]
    A list of bots available

Returns
-------
int
    The index of the bot selected

#### Signature

```python
def get_bot_selection(bots: list[type[BotBehaviors]]) -> int: ...
```



## get_choice_from_prompt

[Show source in util.py:32](https://github.com/HyPerNT/wordle_bot/blob/main/src/cli/util.py#L32)

Prompt the user with a question and a list of options, returning their choice.

Additionally provides some input checking to ensure the selection is valid.

Parameters
----------
prompt : str
    The prompt message, which should be descriptive.
options : list[str]
    A list of strings that correspond with the selections available.
    The first element is always the default, which is accepted if the user
    immediately presses the return key.
has_default : bool, optional
    Whether the first option should be accepted by default, defaults to True

Returns
-------
int
    The choice, 0-indexed

Raises
------
ValueError
    Only when the user provides an illegal option

#### Signature

```python
def get_choice_from_prompt(prompt: str, options: list[str], has_default=True) -> int: ...
```
