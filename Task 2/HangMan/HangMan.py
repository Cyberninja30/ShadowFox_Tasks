HangMan

import random

# List of words for the game
words = ['python', 'hangman', 'computer', 'keyboard', 'mouse', 'monitor', 'program', 'algorithm']

def choose_word():
    """Choose a random word from the list of words."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with dashes for unguessed letters."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    
    word = choose_word()  # Choose a random word
    guessed_letters = []  # List to store guessed letters
    attempts = 6  # Number of attempts allowed
    
    print("Hint: It's a", len(word), "letter word.")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        # Check if the guessed letter is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)  # Add the guessed letter to the list
        
        # Check if the guessed letter is in the word
        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1
        
        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    
    # If the player runs out of attempts
    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()

# Run the game
hangman()
