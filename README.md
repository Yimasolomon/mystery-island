# Mystery Island

Mystery Island is a command-line adventure game built with Python.

You play as an explorer stranded on a mysterious island. Explore different
locations, collect items, solve a puzzle, manage your energy, and find your
way to the Lighthouse to win.

## Features

- Player creation with a custom name.
- Energy management and recovery through resting.
- Exploration of four locations: Beach, Jungle, Cave, and Lighthouse.
- Item collection and inventory management.
- A cave riddle that must be solved to obtain the treasure.
- Location access restrictions.
- Win and quit conditions.
- Automated unit tests.

## Requirements

- Python 3.8 or later.
- No external packages are required.

## How to Run

From the project directory, run:

    python3 game.py

## How to Run Tests

Run the automated tests with:

    python3 -m unittest discover -s tests -v

## Game Instructions

1. Explore the Beach to collect the compass.
2. Explore the Jungle to collect the key.
3. Enter the Cave using the key.
4. Solve the cave riddle. The answer is `echo`.
5. Collect the treasure.
6. Reach the Lighthouse with the compass and treasure to win.

You can also rest to recover energy or quit the game at any time.

## Project Structure

    mystery-island/
    ├── README.md
    ├── player.py
    ├── game.py
    └── tests/
        ├── test_player.py
        └── test_game.py
