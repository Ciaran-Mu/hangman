# Import required modules 
import random

class Hangman:
    '''
    This class is used to play a game of hangman using a word list to chose from and taking input from the user

    Attributes:
        word_list (list): list of possible words supplied to the class.
        word (str): a word chosen at random from word_list.
        word_guessed (list): a list of strings representing the work in progress guesses from the user (initially populated by "_").
        num_letters (int): the number of unique letters left to guess in word.
        num_lives (int): number of lives remaining (default = 5).
        list_of_guesses (list): a list to keep track of previously guessed letters.
    '''
    def __init__(self, word_list: list, num_lives: int = 5):
        '''
        See help(Hangman) for accurate signature.
        '''
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in range(len(self.word))]
        self.num_letters = len({char for char in self.word})
        self.num_lives = num_lives
        self.list_of_guesses = []

    def __update_guess(self, guess):
        '''
        This function is used to update the word_guessed list with the guess in the correct place(s) and decrement the counter of unique letteres remaining.

        Args:
            guess (str): a guess of a single alphabetical character
        '''
        # Update the word_guessed list
        for index, letter in enumerate(self.word):
             if guess == letter:
                self.word_guessed[index] = letter
        # Reduce the number of unique letters left to guess by 1
        self.num_letters -= 1

    def __check_guess(self, guess):
        '''
        This function is used to check whether a given guess is in the randomly chosen word. The result will be output to the screen.

        Args:
            guess (str): a guess of a single alphabetical character
        '''
        guess = guess.lower()
        # Check if the guessed letter is in the chosen word
        if guess in self.word:
            # Guess is correct
            print(f"Good guess! {guess} is in the word.")
            # Update the word_guessed list
            self.__update_guess(guess)
            # Show the user their guesses so far
            word_guessed_output = "".join(self.word_guessed)
            print(f"Your guesses so far: {word_guessed_output}")
        else:
            # Reduce the number of lives left by 1
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.\n You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        '''
        This function asks for input from the user a validates that it is a single alphabetical character that has not been guessed previously.
        '''
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
            self.__check_guess(guess)
            self.list_of_guesses.append(guess)

# Play game function
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break



# Create a word list to choose from
word_list = ["apple", "banana", "orange", "blueberry", "raspberry"]

# Play the game
play_game(word_list)