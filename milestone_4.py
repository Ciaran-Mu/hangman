# Import required modules 
import random

class Hangman:
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in range(len(self.word))]
        self.num_letters = len({char for char in self.word})
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        # Check if the guessed letter is in the chosen word
        if guess in self.word:
            # Guess is correct
            print(f"Good guess! {guess} is in the word.")
            # Update the word_guessed list
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = letter
            # Reduce the number of unique letters left to guess by 1
            self.num_letters -= 1

            # print(f"word guessed: {self.word_guessed}, num_letters: {self.num_letters}")
        else:
            # Reduce the number of lives left by 1
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.\n You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            guess = input("Please enter your guess of one letter: ")
            # Check the validity of the guess
            if guess.isalpha() != 1 or len(guess) != 1:
                # Guess is not valid (not a single letter in the alphabet)
                print("Invalid letter. Please, enter a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                # Already guessed
                print("You already tried that letter!")
            else:
                # Guess is valid so pass onto the check_guess function and add to list
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


word_list = ["Apple", "Banana", "Orange", "Blueberry", "Raspberry"]
#print(word_list)

hangman = Hangman(word_list)
#print(hangman.word)
#print(hangman.word_guessed)
hangman.ask_for_input()