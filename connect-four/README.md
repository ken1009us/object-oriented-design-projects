# Connect Four Game

This is a simple implementation of the Connect Four game in Python. The game allows two players to take turns placing their pieces on a grid and aims to connect four of their pieces either horizontally, vertically, or diagonally.

```bash
Board:

0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 Y 0 0 0 0 0
0 Y R Y 0 0 0
0 Y R R R 0 0

Player 1's turn...
Enter column between 1 and 7 to add piece:
```

## Features

- Command-line interface for playing the game
- Customizable grid size and number of pieces to connect for a win
- Tracks and displays the scores of the players
- Prompts for user input validation and error handling

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/connect-four.git
``

2. Change into the project directory:

```bash
cd connect-four
```

3. Run the game:

```bash
python game.py
```

## How to Play

1. The game starts by displaying an empty grid.

2. Players take turns entering the column number to place their piece.

3. The game checks for a win condition after each move.

4. The game ends when one player reaches the target score.

## Configuration

You can customize the game settings by modifying the following parameters in the main.py file:

- rows: The number of rows in the grid.
- columns: The number of columns in the grid.
- connectN: The number of pieces to connect for a win.
- targetScore: The score required to win the game.

## Acknowledgments

This project is based on the Connect Four game, originally created by Howard Wexler and Ned Strongin.