import random

words = [
    "python",
    "coding",
    "developer",
    "computer",
    "keyboard",
    "laptop",
    "internet",
    "programming",
    "software",
    "mobile"
]

hangman_stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("=" * 35)
print("      WELCOME TO HANGMAN")
print("=" * 35)

while attempts > 0:

    print(hangman_stages[attempts])

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter!")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Attempts left:", attempts)

    else:
        print("✅ Correct guess!")

if attempts == 0:
    print(hangman_stages[0])
    print("\n💀 Game Over!")
    print("The word was:", word)