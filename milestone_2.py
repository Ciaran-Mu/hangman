# Import required modules 
import random

# Define a list of 5 fruits as possible words for hangman
word_list = ["Apple", "Banana", "Orange", "Blueberry", "Raspberry"]
print(word_list)

# Choose one of these words from the list at random
word = random.choice(word_list)
print(word)

# Ask the user for their input
guess = input("Please guess a single letter: ")
if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That's not a valid input.")