"""
Utilities for CLI interactions.

A set of common utilities used while interacting with the package via the CLI.
"""

from bots import BotBehaviors

# file: cli/util.py


def get_bot_selection(bots: list[type[BotBehaviors]]) -> int:
    """
    Get the desired bot of many implementations from the user.

    Parameters
    ----------
    bots : list[BotBehaviors]
        A list of bots available

    Returns
    -------
    int
        The index of the bot selected
    """
    bot_list = [bot.__name__ for bot in bots]
    return get_choice_from_prompt(
        "Select a bot from the following list", bot_list, has_default=False
    )


def get_choice_from_prompt(prompt: str, options: list[str], has_default=True) -> int:
    """
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
    """
    print(prompt)
    for i, opt in enumerate(options):
        print(f"  {i + 1}. {opt} {'(default)' if has_default and i == 0 else ''}")
    while True:
        choice: str = input("> ").strip()
        if has_default and choice == "":
            return 0
        try:
            selection: int = int(choice) - 1
            if not 0 <= selection < len(options):
                raise ValueError
            return selection
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {len(options)}")
