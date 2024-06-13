import random

# Get the word to guess
word = random.choice(["apple", "banana", "cherry"])

# Create a list of the guessed letters
guessed_letters = []

# Get the user's guess
guess = input("Guess a letter: ")

# Check if the guess is correct
while guess not in word and guess not in guessed_letters:
  guessed_letters.append(guess)
  print("Incorrect guess.")

  # Get the next guess
  guess = input("Guess a letter: ")

# Print the winning message
print("You win!")
