﻿# Snakes and Ladders

A Python implementation of the classic Snakes and Ladders board game for 2-4 players.

## Features
- Supports 2-4 players with custom names
- Standard 10x10 board (positions 1-100)
- Predefined snakes and ladders
- Turn-based gameplay with dice rolling (1-6)
- Clear game status and winner announcement
- Robust input validation and user-friendly messages

## Game Rules
- All players start at position 0
- Roll the dice to move forward (1-6)
- Land on a ladder to climb up, or a snake to slide down
- You must roll the exact number to reach position 100 (bounce back if exceeded)
- First player to reach 100 wins

## Board Configuration
- **Ladders (bottom → top):** 4→14, 9→31, 20→38, 28→84, 40→59, 51→67, 63→81, 71→91
- **Snakes (head → tail):** 17→7, 54→34, 62→19, 64→60, 87→24, 93→73, 95→75, 99→78

## How to Run
1. Make sure you have Python 3 installed.
2. Open a terminal in the project directory.
3. Run the game:
   ```sh
   python "snakes and ladders.py"
   ```

## Example Session
```
========================================
  Welcome to Snakes and Ladders!
========================================
Game Rules:
- 2 to 4 players, each with a custom name
- First to reach exactly 100 wins
- Ladders help you climb up, snakes bring you down
- Roll the dice (1-6) each turn
- Bounce back if you overshoot 100
- Enjoy the game!
========================================
Enter number of players (2-4): 2
Enter name for Player 1: Alice
Enter name for Player 2: Rodney

Players:
- Alice
- Rodney

Alice's turn. Press Enter to roll the dice...
You rolled a 4.
Alice is at position 0.
Ladder! Climb up from 4 to 14.
Alice moved to position 14.

Current Board Status:
  Alice: 14
  Rodney: 0
...
🎉 Congratulations, Alice wins the game! 🎉
Final Positions:
  Alice: 100
  Rodney: 87
```
