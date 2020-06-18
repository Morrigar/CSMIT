# Problem Set 2, hangman.py
# Name: Kirk Sripinyo
# Collaborators: None
# Time spent: 46 Years.

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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

def unique_letters(secret_word):
    letters = ''
    for char in secret_word:
        if char not in letters:
            letters +=char
    return len(letters)
            


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
    for char in secret_word:
       #print('Trying '+char+'.')
       if char not in letters_guessed:
           return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    mw=secret_word  #mw is the masked word.
    length = len(mw)
    for i in range (length):
        if i==0:
            if secret_word[i] not in letters_guessed:
                mw = '_'+mw[1:length]
        elif i == length:
            if secret_word[i] not in letters_guessed:
                mw = mw[0:length-1:1]+'_'
        else:
            #print (mw)
            if secret_word[i] not in letters_guessed and i != length:
                mw = mw[0:i:1]+'_'+mw[i+1:length:1]
    spacedmw = ''
    for i in mw:
        spacedmw += str(i)+' '
    return spacedmw



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    availableLetters = list(string.ascii_lowercase)
    for char in letters_guessed:
        #print('Checking '+char)
        if char in availableLetters:
            availableLetters.remove(char)
    def list2string(listOfLetters):
        string = ''
        for char in listOfLetters:
            string += char
        return string        
    return list2string(availableLetters)
    
    

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
    guesses=6
    warnings=3
    letters_guessed = list('')
    validChoices = list(string.ascii_lowercase)
    
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is '+str(len(secret_word))+' letters long.')
    print ('-------------------------------------------')
    
    
    while guesses > 0:    
        print ('The word is: '+str(get_guessed_word(secret_word, letters_guessed)))
        print ('You have '+str(guesses)+' guesses left.')
        print ('Available letters: '+str(get_available_letters(letters_guessed)))
        letterTry = input('Please guess a letter: ')
        letterTry = letterTry.lower()
        if letterTry not in validChoices:
            print ('Oops! '+str(letterTry)+' is not a valid letter.')
            if warnings !=0:
                warnings -= 1
                print ('You have '+str(warnings)+' warnings left before you lose a guess.')
            elif warnings == 0:
                print ('You are out of warnings, you have lost a guess!')
                guesses -= 1
        elif letterTry in letters_guessed:
            print ('You already guessed '+str(letterTry)+'.')
            if warnings !=0:
                warnings -= 1
                print ('You have '+str(warnings)+' warnings left before you lose a guess.')
            elif warnings == 0:
                print ('You are out of warnings, you have lost a guess!')
                guesses -= 1
        else:
            letters_guessed += letterTry
            guesses -= 1
            if letterTry in secret_word:
                print ('Good guess.')
            if letterTry not in secret_word:
                print ('That letter is not in my word.')
            if is_word_guessed(secret_word, letters_guessed):
                break
            
    if is_word_guessed(secret_word, letters_guessed):
        print('The word was: '+str(secret_word))
        print('You guessed the word with '+str(guesses)+' guesses left.')
        print('Your score was: '+str(unique_letters(secret_word))*guesses)
    else:
        print('Sorry, you did not guess the word!') 
        print('The word was: '+str(secret_word))
            
            



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
    my_word = my_word.replace(' ','')
    if len (my_word) != len (other_word):
        return False
    for i in range (len(my_word)):
            if my_word[i] != '_' and my_word[i] != other_word[i]:
                return False
    return True



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
    my_word = my_word.replace(' ','')
    possibleMatches = ''
    for i in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[i]):
            possibleMatches += wordlist[i]+' '
        
    if len(possibleMatches)==0:
        print ('No matches found.')
        
    else:
        print (possibleMatches)


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
    guesses=6
    warnings=3
    letters_guessed = list('')
    validChoices = list(string.ascii_lowercase)
    validChoices += '*'
    
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is '+str(len(secret_word))+' letters long.')
    print ('-------------------------------------------')
    
    
    while guesses > 0:    
        print ('The word is: '+str(get_guessed_word(secret_word, letters_guessed)))
        print ('You have '+str(guesses)+' guesses left.')
        print ('Available letters: '+str(get_available_letters(letters_guessed)))
        letterTry = input('Please guess a letter: ')
        letterTry = letterTry.lower()
        if letterTry not in validChoices:
            print ('Oops! '+str(letterTry)+' is not a valid letter.')
            if warnings !=0:
                warnings -= 1
                print ('You have '+str(warnings)+' warnings left before you lose a guess.')
            elif warnings == 0:
                print ('You are out of warnings, you have lost a guess!')
                guesses -= 1
        elif letterTry in letters_guessed:
            print ('You already guessed '+str(letterTry)+'.')
            if warnings !=0:
                warnings -= 1
                print ('You have '+str(warnings)+' warnings left before you lose a guess.')
            elif warnings == 0:
                print ('You are out of warnings, you have lost a guess!')
                guesses -= 1
        elif letterTry == '*':
            print ('Possible words are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed += letterTry
            guesses -= 1
            if letterTry in secret_word:
                print ('Good guess.')
            if letterTry not in secret_word:
                print ('That letter is not in my word.')
            if is_word_guessed(secret_word, letters_guessed):
                break
            
    if is_word_guessed(secret_word, letters_guessed):
        print('The word was: '+str(secret_word))
        print('You guessed the word with '+str(guesses)+' guesses left.')
        print('Your score was: '+str(unique_letters(secret_word))*guesses)
    else:
        print('Sorry, you did not guess the word!') 
        print('The word was: '+str(secret_word))




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    # to test with known secret word 'apple' uncomment lines below.

    # secret_word = 'apple'
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
