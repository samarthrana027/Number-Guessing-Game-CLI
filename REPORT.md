# Project Report: Number Guessing Game (CLI)

Repository: https://github.com/samarthrana027/Number-Guessing-Game-CLI
Author: samarthrana027
Date: 2026-07-05

## 1. Project Overview

This repository contains a simple command-line Number Guessing Game implemented in Python. The player attempts to guess a secret integer between 1 and 100. The game provides hints (too high / too low), tracks previous guesses, displays a visual range bar, and records basic session statistics (wins, games played, best score) during a single run.

## 2. Key Features

- Random secret number between 1 and 100.
- Interactive CLI with input validation and graceful handling of EOF/interrupts.
- Visual range bar showing the current feasible range.
- Previous guesses history with simple symbols:
  - ↑ indicates previous guess was too low
  - ↓ indicates previous guess was too high
  - ✓ indicates correct guess
- Session statistics shown between rounds (wins, total games, best score).

## 3. Files of Interest

- `Number_Guessing_Game.py` — Main game implementation. This file contains display logic, game loop, input handling, range visualization, and session statistics.

## 4. Implementation Details

- Language: Python 3
- Randomness: Uses Python's `random.randint(1, 100)` to generate the secret number.
- Input handling: Accepts numeric guesses or the keyword `quit`. Non-numeric inputs are rejected with a friendly message.
- Range tracking: `low` and `high` variables are updated on incorrect guesses to narrow the feasible range, and a bar of width 30 displays the current range relative to 1–100.
- Attempts counting: Each valid numeric guess increments the attempt counter.
- End conditions: The round ends when the player guesses correctly or types `quit`. The program also handles Ctrl+C / EOF gracefully.

## 5. How to Run

1. Ensure you have Python 3 installed (3.7+ recommended).
2. Clone the repository:

   git clone https://github.com/samarthrana027/Number-Guessing-Game-CLI.git
3. Run the game:

   python Number_Guessing_Game.py

Follow the on-screen prompts to play.

## 6. Example Session

- Program prompts: "Guess a number between 1 and 100." 
- You input guesses like `50`, `75`, `63`.
- The game responds with "Too low!" or "Too high!" and updates the range bar.
- When you guess correctly, the game prints a summary and updates session stats.

## 7. Testing and Validation

- Manual testing: Play several rounds to ensure hints, range updates, history display, and session stats behave correctly.
- Edge cases tested in code:
  - Non-digit input handling
  - Out-of-range numbers (less than 1 or greater than 100)
  - Keyboard interrupt and EOF handling

## 8. Known Issues / Limitations

- No persistent storage: session statistics (wins, best score) are kept only in memory for the current program run and reset when the process exits.
- No unit tests included.
- The range bar assumes a total range of 1–100. If the game range were to change, the visualization would need updating.

## 9. Suggestions & Future Improvements

- Persist statistics to a local file (JSON or simple text) to track best scores across runs.
- Add unit tests for input parsing, range updates, and attempt counting.
- Add a command-line flag to set the upper and lower bounds rather than hard-coding 1–100.
- Add difficulty levels (e.g., smaller ranges, fewer attempts) or a scoring system.
- Improve accessibility (clearer symbols or optional color support using a library like `colorama`).

## 10. Contribution Guidelines

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Create a new branch for your change.
3. Make changes, include tests where appropriate.
4. Open a pull request describing the change.

## 11. License

Include a license file if you want to make this project open-source (e.g., MIT, Apache-2.0). Currently, no license file is present in the repository — add `LICENSE` to make project terms explicit.

---

If you'd like, I can:
- Add this `REPORT.md` file to the repository now (I will commit it to the default branch),
- Or create a new branch and open a pull request instead.

Which would you prefer?