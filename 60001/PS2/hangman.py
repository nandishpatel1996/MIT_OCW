# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
VOWELS = "aeiou"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = 1
    for letter in secret_word:
        if letter in letters_guessed:
            flag *= 1
        else:
            flag *= 0

    return bool(flag)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            secret_string += letter
        else:
            secret_string += "_"

    return secret_string




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for letter in string.ascii_lowercase:
        if not letter in letters_guessed:
            available_letters += letter

    return available_letters


    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    print("-----------------------------------")
    while (guesses > 0):
        
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters : " + get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter : ")
        if guessed_letter.isalpha() and len(guessed_letter) == 1:
            guessed_letter = guessed_letter.lower()
            if not guessed_letter in letters_guessed:
                letters_guessed.append(guessed_letter)
                if not guessed_letter in secret_word:
                    if guessed_letter in VOWELS: guesses -= 2
                    else:
                        guesses -= 1
                        print("Oops! That letter is not in my word\n" + "Please guess a letter : " + get_guessed_word(secret_word, letters_guessed))
                        print("-----------------------------------")

                else:
                    print("Good guess : " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------------------------------")
                    if not "_" in get_guessed_word(secret_word, letters_guessed):
                        print("Congratulations, you won!")
                        print("Your total score for this game is : " + str(guesses * len(set(secret_word))))
                        break;
            else:
                if warnings > 0: 
                    warnings -= 1
                    print("Oops! You've already guessed that letter. You now have " + str(warnings) + " warnings left : " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------------------------------")
                else:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you loose one guess : " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------------------------------")

                
        else:
            if warnings > 0: 
                warnings -= 1
                print("Oops! That's not a valid letter. You now have " + str(warnings) + " warnings left : " + get_guessed_word(secret_word, letters_guessed))
                print("-----------------------------------")

            else: 
                guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you loose one guess : " + get_guessed_word(secret_word, letters_guessed))
                print("-----------------------------------")

    if guesses == 0:
        print("Sorry, You ran out of guesses")
        print("The word was : " + secret_word)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = 1
    if len(my_word) != len(other_word) : return False
    else:
        index = 0
        while index < len(my_word):
            if my_word[index] != "_":
                my_letter = my_word[index]
                other_letter = other_word[index]
                if (my_letter == other_letter) and (other_word.count(other_letter) == my_word.count(my_letter)):
                    flag *= 1
                else:
                    flag *= 0
            index += 1
    return bool(flag)



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    final_string = ""
    for i in wordlist:
        flag = match_with_gaps(my_word, i)
        if flag : final_string += i + " "

    return final_string



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    print("-----------------------------------")
    while (guesses > 0):
        
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters : " + get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter : ")
        if guessed_letter.isalpha() and len(guessed_letter) == 1:
            guessed_letter = guessed_letter.lower()
            if not guessed_letter in letters_guessed:
                letters_guessed.append(guessed_letter)
                if not guessed_letter in secret_word:
                    if guessed_letter in VOWELS: guesses -= 2
                    else:
                        guesses -= 1
                        print("Oops! That letter is not in my word\n" + "Please guess a letter : " + get_guessed_word(secret_word, letters_guessed))
                        print("-----------------------------------")

                else:
                    print("Good guess : " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------------------------------")
                    if not "_" in get_guessed_word(secret_word, letters_guessed):
                        print("Congratulations, you won!")
                        print("Your total score for this game is : " + str(guesses * len(set(secret_word))))
                        break;
            else:
                if warnings > 0: 
                    warnings -= 1
                    print("Oops! You've already guessed that letter. You now have " + str(warnings) + " warnings left : " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------------------------------")
                else:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you loose one guess : " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------------------------------")

        elif guessed_letter == "*": print("Possible matches are here : \n" + show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

        else:
            if warnings > 0: 
                warnings -= 1
                print("Oops! That's not a valid letter. You now have " + str(warnings) + " warnings left : " + get_guessed_word(secret_word, letters_guessed))
                print("-----------------------------------")

            else: 
                guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you loose one guess : " + get_guessed_word(secret_word, letters_guessed))
                print("-----------------------------------")

    if guesses == 0:
        print("Sorry, You ran out of guesses")
        print("The word was : " + secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
