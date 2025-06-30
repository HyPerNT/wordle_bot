<a id="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Last Commit][last-commit-shield]][last-commit-url]
[![Coverage][coverage-badge]][coverage-url]
![Interrogate][interrogate-shield]
[![Contributors][contributors-shield]][contributors-url]
[![Unlicense License][license-shield]][license-url]
![Size][repo-size-shield]

<br />
<div align="center">
  <a href="https://github.com/HyPerNT/wordle_bot">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c5/Wordle_Logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Wordle Bot</h3>

  <p align="center">
    A library designed for building and testing strategies for the game Wordle.
    <br />
    <a href="https://hypernt.github.io/wordle_bot/"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-tests">Running Tests</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is a Python library aimed at providing developers with adequate tooling to develop and test an algorithmic strategy for the game Wordle.

There are three main modules included and intended for use.
1. `wordle` - The Wordle game itself. This needn't be extended, but should be imported if a user wanted to augment the testing procedure.
2. `bots` - The primary module for building bots to play the game, namely by extending the `BotBehaviors` class provided.
3. `tester` - The primary module used for testing Wordle bots. This is used to run a bot against the full Wordle word list and provide summary results to the command-line.

The modules provided are intended to be as slim as possible so that providing additional logic or alternative strategies is as easy as possible.
Check out the [Example Bot](https://github.com/HyPerNT/wordle_bot/blob/main/src/bots/example_bot.py) to see how simple they can really be!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Black](black-url)
* [Coverage](coverage-url)
* [Coverage-badge](coverage-badge-url)
* [Flake8](flake8-url)
* [Handsdown](hd-url)
* [Interrogate](int-url)
* [MkDocs](mkdocs-url)
* [MyPy](mypy-url)
* [Pre-commit-hooks](pch-url)
* [Pydocstyle](pds-url)
* [Pyroma](pyroma-url)
* [PyTest](pytest-url)
* [Xenon](xenon-url)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started, simply clone the repo:
```sh
git clone git@github.com:HyPerNT/wordle_bot.git
```

You can run the tester against the example bot by simply running the `main.py` file:
```sh
python3 src/main.py
```

### Prerequisites

It's recommended that you run this repo in a python virtual environment, such as `pyenv`:
```sh
curl -fsSL https://pyenv.run | bash\n
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/HyPerNT/wordle_bot.git
   ```
2. Create a new pyenv environment
   ```sh
   pyenv install 3.11.7
   pyenv shell 3.11.7
   pyenv local 3.11.7
   ```
3. Install required python modules with pip
   ```sh
   pip3 install tqdm
   ```
4. (Optional) Install additional python modules to support use of pre-commit hooks, tests, and coverage reports
   ```sh
   pip3 install poetry mypy flake8 black pyroma xenon interrogate handsdown mkdocs pytest coverage coverage-badge
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin <github_username>/<repo_name>
   git remote -v # confirm the changes
   ```

### Running Tests

In order to run tests, it is necessary to install the package in editable mode:
```sh
  pip3 install -e .
```

Then, tests should be executable readily by PyTest:
```sh
  pytest
```

For code coverage:
```sh
  coverage run -m pytest
  coverage report # For a short report in the command-line
  coverage html -d cov # For HTML coverage reports
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can access the features of the interactive CLI by running `python3 src/main.py`.
From that script, you can choose to run the automated tester on a bot of your choice:
![Demo of tests run on the ExampleBot](images/tester_demo.gif)

Or play a game using a bot of your choice, setting a secret word for it to guess.
![Demo of ExampleBot trying to guess "MUSIC"](images/word_guess_demo.gif)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add README
- [x] Add v0.1.0 source code and example project
- [x] Add documentation
- [x] Add tests and coverage reports
- [ ] Add support for testing a bot against today's word

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Brenton Candelaria - [@HyPerNT](https://discord.com/users/198554971954872320) - brentoncandelaria@example.com

Project Link: [https://github.com/HyPerNT/wordle_bot](https://github.com/HyPerNt/wordle_bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[last-commit-shield]: https://img.shields.io/github/last-commit/HyPerNT/wordle_bot
[last-commit-url]: https://github.com/HyPerNT/wordle_bot/commits/main/
[contributors-shield]: https://img.shields.io/github/contributors/HyPerNT/wordle_bot
[contributors-url]: https://github.com/HyPerNT/wordle_bot/graphs/contributors
[license-shield]: https://img.shields.io/github/license/HyPerNT/wordle_bot
[license-url]: https://github.com/HyPerNT/wordle_bot/blob/main/LICENSE
[interrogate-shield]: ./badges/interrogate.svg
[repo-size-shield]: https://img.shields.io/github/languages/code-size/HyPerNT/wordle_bot
[pytest-url]: https://docs.pytest.org/en/stable/
[black-url]: https://github.com/psf/black
[pch-url]: https://github.com/pre-commit/pre-commit-hooks
[flake8-url]: https://flake8.pycqa.org/en/latest/
[mypy-url]: https://mypy-lang.org
[xenon-url]: https://pypi.org/project/xenon/
[pyroma-url]: https://pypi.org/project/pyroma/
[int-url]: https://interrogate.readthedocs.io/en/latest/
[pds-url]: https://www.pydocstyle.org/en/stable/
[hd-url]: https://github.com/vemel/handsdown
[coverage-url]: https://coverage.readthedocs.io/en/7.9.1/
[coverage-badge-url]: https://pypi.org/project/coverage-badge/
[coverage-badge]: badges/coverage.svg
[mkdocs-url]: https://www.mkdocs.org
