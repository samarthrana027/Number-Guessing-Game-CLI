import random


def display_header():
    print("\n" + "=" * 45)
    print("       NUMBER GUESSING GAME")
    print("=" * 45)


def display_range_bar(low, high, total=100):
    bar_width = 30

    left_pct = (low - 1) / (total - 1)
    right_pct = (high - 1) / (total - 1)

    left_pos = int(left_pct * (bar_width - 1))
    right_pos = int(right_pct * (bar_width - 1))

    bar = ["-"] * bar_width

    for i in range(left_pos, right_pos + 1):
        if 0 <= i < bar_width:
            bar[i] = "█"

    print(f"\n  Range: [{low} — {high}]")
    print(f"  1 {''.join(bar)} 100")


def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    low, high = 1, 100
    guesses = []

    print("\n  Guess a number between 1 and 100.")
    print("  Type 'quit' to exit.\n")

    while True:
        display_range_bar(low, high)

        if guesses:
            history = "  Previous guesses: " + ", ".join(
                f"{g['val']}({'↑' if g['hint'] == 'high' else '↓' if g['hint'] == 'low' else '✓'})"
                for g in guesses
            )
            print(history)

        try:
            raw = input(f"\n  Attempt #{attempts + 1} — Your guess: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n\n  Thanks for playing! Goodbye.\n")
            return None

        if raw == "quit":
            print(f"\n  The number was {secret}. Better luck next time!\n")
            return None

        if not raw.isdigit():
            print("  Please enter a valid number between 1 and 100.")
            continue

        val = int(raw)

        if val < 1 or val > 100:
            print("  Number must be between 1 and 100.")
            continue

        attempts += 1

        if val > secret:
            high = min(high, val - 1)
            print(f"\n  Too high! Try something lower than {val}.")
            guesses.append({"val": val, "hint": "high"})

        elif val < secret:
            low = max(low, val + 1)
            print(f"\n  Too low! Try something higher than {val}.")
            guesses.append({"val": val, "hint": "low"})

        else:
            guesses.append({"val": val, "hint": "correct"})

            print("\n" + "=" * 45)

            if attempts == 1:
                print("  INCREDIBLE! First try!")
            elif attempts <= 5:
                print(f"  EXCELLENT! You got it in {attempts} attempts!")
            elif attempts <= 10:
                print(f"  Nice! Found {secret} in {attempts} attempts.")
            else:
                print(f"  Got it! The number was {secret} ({attempts} attempts).")

            print("=" * 45 + "\n")
            return attempts


def main():
    display_header()
    print("\n  Welcome! Try to guess the secret number.")

    best_score = None
    total_wins = 0
    total_games = 0

    while True:
        result = play_game()
        total_games += 1

        if result is not None:
            total_wins += 1

            if best_score is None or result < best_score:
                best_score = result
                print(f"  New best score: {best_score} attempts!\n")

        print(
            f"  Stats — Wins: {total_wins}/{total_games} | Best: {best_score or '-'} attempts"
        )

        again = input("\n  Play again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("\n  Thanks for playing!")
            print(f"  Games played : {total_games}")
            print(f"  Games won    : {total_wins}")
            print(f"  Best score   : {best_score or '-'} attempts")
            break


if __name__ == "__main__":
    main()