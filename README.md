# Number Guessing Game CLI

An interactive command-line number guessing game built with Python. Try to guess the secret number between 1 and 100 with helpful hints, visual range indicators, and score tracking. Can you beat your personal best?

## Features

🎮 **Core Features:**
- 🎯 **Guess a Secret Number** - The computer randomly picks a number between 1-100
- 💡 **Smart Hints** - Get feedback on whether your guess is too high or too low
- 📊 **Visual Range Bar** - See the dynamic range narrowing as you make guesses
- 📝 **Guess History** - Track all your previous guesses with visual indicators
- 🏆 **Score Tracking** - Keep track of your best score across multiple games
- 📈 **Game Statistics** - View wins, total games played, and personal best
- ⌨️ **Input Validation** - Robust error handling for invalid inputs
- 🚪 **Exit Option** - Type 'quit' to exit at any time

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/samarthrana027/synent-task2-Number-Guessing-Game-CLI--Samarth.git
cd synent-task2-Number-Guessing-Game-CLI--Samarth
```

2. Ensure Python is installed on your system:
```bash
python --version
```

## Usage

Run the game:
```bash
python Number_Guessing_Game.py
```

### How to Play

1. The game starts with a secret number between 1-100
2. Make your guess when prompted
3. You'll receive feedback:
   - **"Too high!"** - Your guess is higher than the secret number (↑)
   - **"Too low!"** - Your guess is lower than the secret number (↓)
   - **"Correct!"** - You found the number! (✓)
4. Watch the range bar shrink as you narrow down the possibilities
5. Try to find the number in as few attempts as possible
6. After each game, view your statistics and choose to play again
7. Type **'quit'** at any time to exit the game

### Example Gameplay Session

```
=============================================
       NUMBER GUESSING GAME
=============================================

  Welcome! Try to guess the secret number.

  Guess a number between 1 and 100.
  Type 'quit' to exit.

  Range: [1 — 100]
  1 ███████████████────────────── 100

  Attempt #1 — Your guess: 50

  Too low! Try something higher than 50.

  Range: [51 — 100]
  1 ─────────────███████████──── 100
  Previous guesses: 50(↓)

  Attempt #2 — Your guess: 75

  Too high! Try something lower than 75.

  Range: [51 — 74]
  1 ─────────────██████────────── 100
  Previous guesses: 50(↓), 75(↑)

  Attempt #3 — Your guess: 62

  Too low! Try something higher than 62.

  Range: [63 — 74]
  1 ─────────────███████────────── 100
  Previous guesses: 50(↓), 75(↑), 62(↓)

  Attempt #4 — Your guess: 68

  =============================================
  EXCELLENT! You got it in 4 attempts!
  =============================================

  Stats — Wins: 1/1 | Best: 4 attempts

  Play again? (yes/no): no

  Thanks for playing!
  Games played : 1
  Games won    : 1
  Best score   : 4 attempts
```

## Features Explained

### 🎯 Smart Range Indicator
The visual range bar dynamically updates as you make guesses, showing you the narrowed search space. The bar fills with █ symbols representing the current valid range.

### 📝 Guess History
Each previous guess is displayed with a hint indicator:
- **↑** - Too high
- **↓** - Too low
- **✓** - Correct

### 🏆 Score Tracking
The game tracks:
- **Total Games Played** - How many games you've started
- **Games Won** - How many games you successfully completed
- **Best Score** - Your lowest number of attempts to guess correctly

### 💡 Hint System
Immediate feedback after each guess:
- Shows if your guess is above or below the target
- Updates the valid range automatically
- Helps you make more strategic guesses

## Code Structure

- **`display_header()`** - Displays the game title banner
- **`display_range_bar(low, high, total=100)`** - Shows visual representation of the current valid range
- **`play_game()`** - Main game loop for a single round
  - Handles user input validation
  - Provides hints and feedback
  - Tracks guesses and attempts
  - Returns the number of attempts taken
- **`main()`** - Main application loop
  - Manages multiple game sessions
  - Tracks game statistics
  - Prompts for replaying

## Platform Compatibility

✅ **Works on:**
- Windows
- macOS
- Linux

## Game Strategy Tips

1. **Use Binary Search** - Guess the middle of the range for optimal narrowing
2. **Start with 50** - This divides the range perfectly in half
3. **Pay Attention to Range** - Let the range bar guide your strategy
4. **Learn from History** - Review previous guesses before making your next guess

### Optimal Performance
- **1 guess:** Impossible (unless you're extremely lucky!)
- **4-5 guesses:** Excellent performance using binary search
- **6-7 guesses:** Good strategy
- **8+ guesses:** You can improve your strategy

## Future Enhancements

Potential improvements for future versions:
- Difficulty levels (different ranges: 1-50, 1-1000, etc.)
- Time-based challenges
- Multiplayer mode
- Save best scores to a file
- Leaderboard system
- Customizable range settings
- Sound effects/notifications
- AI opponent mode (computer also tries to guess)

## Error Handling

- **Invalid Input** - Non-numeric entries are rejected
- **Out of Range** - Numbers outside 1-100 are caught and re-prompted
- **Keyboard Interrupt** - Gracefully handles Ctrl+C
- **EOF Exception** - Properly exits if input stream ends

## License

This project is open source and available for educational purposes.

## Author

**Samarth Rana** - samarthrana027

---

Made with ❤️ for learning Python CLI games and interactive applications

**Challenge:** Can you guess the number in 4 attempts or less? 🎯
