# Import required modules 
import random

# Define functions
def check_guess(guess):
    guess = guess.lower()
    # Check if the guessed letter is in the chosen word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    # Loop to continuously ask user for a letter input and check if it is valid
    while True:
        guess  = input("Please enter your guess of one letter: ")
        # Check the validity of the guess
        if guess.isalpha() and len(guess) == 1:
            # Guess is valid (a single letter in the alphabet)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    # Use the acquired letter guess as arguement for the check_guess function
    check_guess(guess)

# Define a list of 5 fruits as possible words for hangman
word_list = ["Apple", "Banana", "Orange", "Blueberry", "Raspberry"]
print(word_list)

# Choose one of these words from the list at random
word = random.choice(word_list)

ask_for_input()