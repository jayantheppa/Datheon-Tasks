
import random

# Words for the game
words = ["python", "computer", "program", "hangman", "developer"]

# ASCII gallows stages
stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

print("=" * 35)
print("       WELCOME TO HANGMAN")
print("=" * 35)

while wrong_guesses < max_attempts:
    print(stages[wrong_guesses])

    # Display the hidden word
    display = " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in word
    )

    print("Word:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word.upper())
        break

    print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
    guess = input("Guess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter! Try another.\n")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess! Try again.\n")

else:
    print(stages[wrong_guesses])
    print("Game over! The word was:", word.upper())

print("\nThanks for playing Hangman!")
