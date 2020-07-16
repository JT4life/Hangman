import sys

#User 1 chooses word
def choose_word():
    word = input("Choose a word for the other player to guess. The word cannot be proper nouns, names, places, and brands. ")
    return word.lower()

#function for playing the game
def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    number_of_guesses = 6
    print("Let's begin Hangman!")
    print(show_hangman(number_of_guesses))
    print(word_complete)
    print("\n")
    try:
        while not guessed and number_of_guesses > 0:
            guess = input("Guess a letter or try to solve the word.").lower()
            if len(guess) == 1 and guess.isalpha(): #must be alphabets
                if guess in guessed_letters:
                    print("You already guessed the letter ", guess, ". Try again.")
                elif guess not in word:
                    print(guess, " is not in the word. Try again.")
                    number_of_guesses -=1
                    guessed_letters.append(guess)
                else:
                    print("Nice! ", guess, "is in the word.")
                    guessed_letters.append(guess)
                    word_is = list(word_complete)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_is[index] = guess
                    word_complete = "".join(word_is)
                    if "_" not in word_complete:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word ", guess,". Try again.")
                elif guess != word:
                    print(guess, " is not the word. Try again.")
                    number_of_guesses -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_complete = word
            else:
                print("Incorrect guess, try again.")
            print(show_hangman(number_of_guesses))
            print(word_complete)
            print("\n")
        if guessed:
            print("Congratulations, you have guessed the word!")
        else:
            print("Nice try but you have run out of guesses. The word was ", word)
    except:
        print(sys.exc_info())

#show our hangman figure to User depending on number of guesses
def show_hangman(number_of_guesses):
    state = [ """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |     / \\
                    |      
                 -------
    """,
    """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |     /
                    |     
                 -------
    """,
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      
                   |
                -------
    """,
    """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      
                   |
                -------
    """,
    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |
                -------
    """,
    """
                  --------
                  |      |
                  |      O
                  |
                  |
                  |
               -------
    """,
    """
                  --------
                  |      |
                  |
                  |
                  |
                  |
               -------
    """
    ]
    return state[number_of_guesses]

def main():
    word = choose_word()
    play(word)
    try:
        while input("Do you want to play again? y for yes, n for no.").lower()=="y":
            word = choose_word()
            play(word)
        print("Thank you for playing Hangman. See you next time!")
    except:
        print(sys.exc_info)
    

if __name__ == "__main__":
    main()

