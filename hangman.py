import random
from word_list import word_list

name = input("Enter your name: ")
def intro(name): #Intro of the game
    print("Hello, Welcome to Hangman " + name)     #prints out the greetings
intro(name)

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    guessed = False
    # How many chances the player is going to be given
    chances = 6
    guessed_letters = []
    guessed_words = []
    print(display_hangman(chances))
    print("\n")
    under_scores = "_" * len(word)  # Creates the underscores for the guesser to know how many letters the word is consisted of
    print(under_scores)
    #To make sure that the user has valid chances
    while not guessed and chances > 0:
        guess = input("Guess the letter or the word: ").upper()
        #When the user guesses the letter
        if len(guess) == 1:
            # When the guessed letter is not in the word
            if guess not in word and guess in guessed_letters:
                print("Sorry, you already guessed this letter. Try again.")
                print("The letters you guessed so far are: " + guessed_letters)
            #When the guessed letter is in the word
            elif guess not in word and guess not in guessed_letters:
                print("Sorry, " + guess + " is not in the word")
                chances -= 1
                guessed_letters.append(guess)

            #Replace the correct letter with the underscore after dividing the word into separated letters using enumerate function
            else:
                print("Nice job,", guess, "is in the word!")
                print("\n")
                guessed_letters.append(guess)
                word_as_list = list(under_scores)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                under_scores = "".join(word_as_list)
                if "_" not in under_scores:
                    guessed = True
        #When the user guessed the word
        elif len(guess) == len(word):
            #When the user got the correct word
            if guess == word:
                print("Congrats, " + name + ", you guessed the correct word.")
            #When the user got the wrong word
            elif guess != word:
                    print("Not a valid guess, maybe try again")
                    
                    guessed_words.append(guess)
            else:
                guessed = True

        else:
            print("not a valid guess")
        print(display_hangman(chances))
        print(under_scores)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")



# To print out the current state of hangman depending on the chances left
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

