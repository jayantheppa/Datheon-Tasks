# Hangman Game (Python)

A simple, terminal-based Hangman game written in Python. Guess the hidden word one letter at a time before the gallows drawing is complete.

## Features

- Random word selection from a built-in word list
- ASCII gallows that updates after each incorrect guess
- A maximum of 6 incorrect guesses per round
- Tracks letters already guessed
- Prevents duplicate guesses from costing an attempt
- Validates input so each guess must be one alphabet letter
- Shows correctly guessed letters and hides the remaining letters
- Option to play multiple rounds
- Uses only Python's standard library

## Requirements

- Python 3.8 or newer recommended
- A terminal, Command Prompt, PowerShell, or Visual Studio Code

No extra packages are required.

## Project Structure

```text
hangman-project/
├── hangman.py
└── README.md
```

## How to Run

### 1. Download or clone the project

If you have Git installed:

```bash
git clone YOUR_REPOSITORY_URL
cd hangman-project
```

Alternatively, download the project files and open the folder in Visual Studio Code.

### 2. Open a terminal

In VS Code, select **Terminal → New Terminal**.

### 3. Run the game

On Windows, try:

```bash
python hangman.py
```

If that command is not recognized, try:

```bash
py hangman.py
```

On macOS or Linux, you may need:

```bash
python3 hangman.py
```

## How to Play

1. Start the program.
2. The game selects a random word and displays underscores for hidden letters.
3. Enter one alphabet letter when prompted.
4. Correct guesses reveal the letter in the word.
5. Incorrect guesses add a part to the gallows drawing.
6. Repeated guesses and invalid input do not use an attempt.
7. Guess the full word before making 6 incorrect guesses to win.
8. Choose `y` to play another round or `n` to quit.

## Example Output

```text
====================================
          WELCOME TO HANGMAN
====================================
Guess the hidden word one letter at a time.
You can make up to 6 incorrect guesses.

Word: _ _ _ _ _ _
Incorrect guesses: 0/6
Guessed letters: None
Guess a letter: p
Correct! That letter is in the word.
```

The selected word and exact output will vary from game to game.

## Concepts Used

- Variables and constants
- Lists and strings
- `random.choice()` for random word selection
- Sets to track guessed letters
- Loops and conditional statements
- Functions and modular program design
- Input validation and exception handling

## Customization

To add or change words, edit the `WORDS` list near the top of `hangman.py`:

```python
WORDS = [
    "python",
    "computer",
    "developer",
]
```

Keep each word alphabetic and lowercase for the simplest gameplay.

## Future Improvements

- Difficulty levels
- Score tracking
- Categories such as technology, animals, and sports
- Colorful terminal output
- A larger external word list

## License

This project is provided for learning and educational use. You may adapt it for your own practice projects.
