import random

# I made a small list of words for the game
words = ["python", "hangman", "keyboard", "galaxy", "jungle"]

# These are the hangman drawings, one for each wrong guess
# 0 = empty, 6 = game over
hangman_pics = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

# -------------------------------------------------------
# pick a random word from the list
# -------------------------------------------------------
word = random.choice(words)

# keep track of guessed letters and wrong guesses
guessed_letters = []
wrong_guesses   = 0
max_wrong       = 6

print("\n  Welcome to Hangman!")
print(f"  The word has {len(word)} letters. Good luck!\n")

# -------------------------------------------------------
# main game loop - keeps going until win or 6 wrong guesses
# -------------------------------------------------------
while wrong_guesses < max_wrong:

    # show the hangman drawing
    print(hangman_pics[wrong_guesses])

    # show the word with blanks for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\n  Word:", display)
    print(f"  Wrong guesses left: {max_wrong - wrong_guesses}")

    # show wrong letters if any
    wrong_letters = [l for l in guessed_letters if l not in word]
    if wrong_letters:
        print("  Wrong letters:", " ".join(wrong_letters))

    # check if the player has won
    all_guessed = True
    for letter in word:
        if letter not in guessed_letters:
            all_guessed = False
            break

    if all_guessed:
        print(f"\n  You won! The word was: {word}")
        break

    # ask the player for a letter
    print()
    guess = input("  Enter a letter: ").strip().lower()

    # basic input checks
    if len(guess) != 1 or not guess.isalpha():
        print("  Please enter one letter only.\n")
        continue

    if guess in guessed_letters:
        print(f"  You already guessed '{guess}'. Try a different one.\n")
        continue

    # add the guess to the list
    guessed_letters.append(guess)

    # check if it is in the word
    if guess in word:
        print(f"\n  Good one! '{guess}' is in the word!\n")
    else:
        wrong_guesses += 1
        print(f"\n  Nope! '{guess}' is not in the word.\n")

else:
    # this runs when wrong_guesses hits 6
    print(hangman_pics[6])
    print(f"\n  Game over! The word was: {word}\n")

# ask to play again
again = input("  Play again? (y / n): ").strip().lower()
if again == "y":
    print("\n  Restarting...\n")
    exec(open(__file__).read())
else:
    print("\n  Thanks for playing! Bye!\n")
