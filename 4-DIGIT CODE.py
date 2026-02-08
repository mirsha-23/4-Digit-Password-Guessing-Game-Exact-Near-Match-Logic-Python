import random

def generate_secret_code():
    # Generates a 4-digit secret code (digits 0–9)
    code = [random.randint(0, 9) for _ in range(4)]
    return code


def feedback(secret_code, guess):
    exact_match = 0
    near_match = 0

    # Count exact matches
    for i in range(4):
        if secret_code[i] == guess[i]:
            exact_match += 1

    # Count near matches
    for digit in set(guess):
        count_secret = secret_code.count(digit)
        count_guess = guess.count(digit)
        near_match += min(count_secret, count_guess)

    near_match -= exact_match

    return exact_match, near_match


def play_game():
    secret_code = generate_secret_code()
    attempts = 10

    print("🔐 4-Digit Password Guessing Game")
    print("You have 10 attempts to guess the password.")

    for attempt in range(1, attempts + 1):
        guess = input(f"\nAttempt {attempt}/{attempts} – Enter your 4-digit guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("❌ Invalid input! Enter exactly 4 digits.")
            continue

        guess = [int(digit) for digit in guess]
        exact, near = feedback(secret_code, guess)

        print(f"Exact Matches: {exact}, Near Matches: {near}")

        if exact == 4:
            print("🎉 Congratulations! You cracked the password!")
            return

    print("\n❌ Game Over!")
    print("The secret code was:", secret_code)


if __name__ == "__main__":
    play_game()
