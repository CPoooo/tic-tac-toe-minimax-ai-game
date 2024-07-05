# Tic-Tac-Toe AI with Minimax Algorithm

Welcome to my Tic-Tac-Toe AI project! This project allows you to play against an AI that uses the Minimax algorithm, a classic approach in game theory for decision-making.

## Getting Started

To play the game:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CPoooo/tic-tac-toe-minimax-ai-game
   cd tic-tac-toe-ai
   ```

2. **Install dependencies:**
   Ensure you have Python and Pygame installed. If not, install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   Execute the `main.py` file to start playing against the AI:
   ```bash
   python main.py
   ```

4. **Gameplay Instructions:**
   - The game starts with you (Player X) making the first move.
   - Click on an empty cell to place your mark (X).
   - The AI (Player O) uses the Minimax algorithm to determine its moves.
   - The game ends when a player wins, or all cells are filled (draw).
   - Press `r` to reset the game after it ends.

## How the AI Works

The AI uses the Minimax algorithm to determine the best move in a given game state:
- **Minimax Algorithm:** This is a decision rule used in decision theory and game theory for minimizing the possible loss for a worst-case scenario.

## Features

- **Game State Management:** Tracks game states, checks for wins, draws, and manages player turns.
- **Reset Functionality:** Allows resetting the game to play again.
