# roulette_project

A simple **terminal-based Roulette game** implemented in Python. This project simulates a classic casino roulette experience where players can place bets and spin the wheel.

## Features
- **Single-player mode** with virtual currency.
- Multiple bet types:
  - Straight (numbers)
  - Red/Black
  - Even/Odd
  - High/Low
  - Column number
  - Dozen
- Randomized wheel spins using Python's `random` module.
- Runs entirely in the terminal.

## Rules
**Starting Conditions**

- You begin with 100 units of money.
- The game consists of 5 rounds (or fewer if you run out of money).

1. Place Your Bet

- You are be prompted to enter a bet amount.
- If you lost the previous round, the bet for the next round will be doubled (Martingale strategy).

**Choose Bet Type**

You can bet on INSIDE (specific numbers) or OUTSIDE (categories: color, odd/even, which dozen and which column).
Inside bets require you to pick one or more numbers.
Outside bets allow you to choose options like Red/Black, Odd/Even, or High/Low, column number and dozen number.

**Spin the Wheel**

The game randomly generates a number (0–36) and its color (Red/Black/Green).

**Check Results**

If your bet matches the outcome, you win according to roulette payout rules:

- Inside bets pay higher (e.g., straight-up number pays 35:1 or lower, depends on how much numbers you enetered).
- Outside bets pay lower (1:1 if you guessed any category).

Your winnings are added to your balance.

**Continue or End**

If you lose, your next bet doubles.
If your balance reaches 0, the game ends immediately.
After 5 rounds, the game ends.

## Future Improvements

Fix project structure and refactor code according to the best practices.
Clean the code
Add GUI using tkinter or PyQt.
Implement multiplayer mode.
Track game statistics and betting history.
