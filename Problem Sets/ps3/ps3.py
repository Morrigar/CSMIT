# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    wordscore = 0
    for c in word: #lookup and add all the values for each letter over the word
        wordscore += SCRABBLE_LETTER_VALUES[c]
    wordscore *= max (7*len(word)-3*(n-len(word)),1)
    return wordscore

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand ['*'] = 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    word = word.lower()
    for letter in word:
        if hand.get(letter,0):
            newHand[letter] = newHand.get(letter,0) - 1
            if newHand.get(letter,0) < 0:
                newHand[letter] = 0
    return newHand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    lettersforword = get_frequency_dict(word)#for letter in word:
        
    def have_word_in_hand(lettersforword):
        #print (freq)
        for i in lettersforword:
            #print ('Testing '+ i)
            #print ('# of '+i+' = '+str(freq[i])+'# of '+i+' in hand = '+str(hand.get(i,0)))
            if lettersforword[i] > hand.get(i,0):
                #print ('"'+i+'"'+ ' not in hand, about to return False.')
                return False
        return True

    
    def substar_search(word):
        wcpos = word.find('*')
        #print ("In substar_search.")
        if wcpos == 0:
            for c in VOWELS:
                word =  c + word [1:len(word)]
                if word in word_list:
                    return True
            
        elif wcpos == len(word):
            for c in VOWELS:
                word = word [0:len(word)]+c
                if word in word_list:
                    return True
        else:
            for c in VOWELS:
                word = word [0:wcpos]+c+word[wcpos+1:len(word)]
                #print (word)
                if word in word_list:
                    return True
            
    if '*' not in word:   
        if have_word_in_hand(lettersforword) and word in word_list:
            return True
        else:
            return False
    else:
        if have_word_in_hand(lettersforword) and substar_search(word):
            return True
        else: 
            return False
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    countstring=''
    for letter in hand.keys():
        for j in range(hand[letter]):
             countstring += letter      # print all on the same line    
    
    return len(countstring)


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    totalscore = 0
    handlen = calculate_handlen(hand)
    
    # As long as there are still letters left in the hand:
    while handlen>0:    
        print ('Current hand: ', end ='')
        display_hand(hand)
        word = input ('Enter Word or \"!!\" to indicate that you are finished: ')    
        #print (is_valid_word(word, hand, word_list))
        if word == '!!':
            break
        else:
            if is_valid_word(word, hand, word_list):
                totalscore += get_word_score(word, handlen)    
                print ('\"'+word+'\" earned ' + str(get_word_score(word, handlen))+\
                       ' points. Total: ' + str(totalscore))
                hand = update_hand(hand, word)
                handlen = calculate_handlen(hand)
            else: 
                print ('\"'+word + '\" is not a valid word.')
                hand = update_hand(hand, word)                    
                handlen = calculate_handlen(hand)            
    print ('Your score for this hand was: '+str(totalscore))
    return totalscore
#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    copies = hand.get(letter,0)
    newHand = hand.copy()
    allletters = VOWELS+CONSONANTS    
    if not copies:
        print ('You don\'t have a '+letter+' in your hand.')
        return hand
    else:
        for c in newHand:
            if c =='*':
                pass
            elif allletters.find(c)==0:                
                #print ('Removing '+c+'.')
                allletters = allletters[1:]
            elif allletters.find(c)==len(allletters):
                #print ('Removing '+c+'.')
                allletters = allletters[0:len(allletters)]
            else:
                #print ('Removing '+c+'.')
                allletters = allletters[0:allletters.find(c)] + allletters[allletters.find(c)+1:]
    #print ('Choice for newletter: '+allletters)
    newHand[letter]=0
    for i in range (copies):
        newletter = random.choice(allletters)
        print ('Dealing new letter '+newletter)
        newHand[newletter] = newHand.get(newletter, 0)+1
        
    return newHand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    handsub = False
    replay = False
    seriesScore = 0
    hand_size = 12
    print('Welcome to the Word Game!') # TO DO... Remove this line when you implement this function
    print('Special rules:  Once per game you can replay a hand for a better score and once')
    print('per game you can exchange all copies of one letter from your hand for new letters.')
    totalhands = 0
    while True:
        try:
            totalhands = int(input('Enter the number of hands you would like to play: '))
        except ValueError:
            print ('Enter a whole number for the total hands to play.')
        else:
            break
    totalhands = abs(totalhands)
    while totalhands > 0:
        originalhand = deal_hand(hand_size)
        hand = originalhand.copy()
        print ('Your current hand is: ', end='')
        display_hand(hand)
        handscore = 0
        if handsub==False:
            subchoice = ''
            while subchoice.lower() != 'yes' or subchoice.lower() != 'y': 
                subchoice = input ('Would you like to substitute a letter, yes or no? ')
                if subchoice.lower() == 'yes' or subchoice.lower()== 'y':
                    lettersub = input ('What letter would you like to substitute this will substitutes all copies of the letter):') 
                    hand = substitute_hand(hand, lettersub)
                    handsub = True
                    break
                elif subchoice.lower() == 'no' or subchoice.lower()== 'n':
                    print ('Ok, you can sub a letter later if you want.')
                    break
                else:
                    print ('Enter y or n.')
        handscore = play_hand(hand, word_list)
        if replay==False:
            subchoice = ''
            while subchoice.lower() != 'yes': 
                subchoice = input ('Would you like to replay that hand and see if you can beat it? ')
                if subchoice.lower() == 'yes' or subchoice.lower()== 'y':    
                    replay = True
                    replayscore = play_hand(hand, word_list)
                    if replayscore > handscore:
                        print ('You did better!  Your score for that hand will be: '+str(replayscore))
                        handscore = replayscore
                    break
                elif subchoice.lower() == 'no' or subchoice.lower()== 'n':
                    print ('Ok, you can replay a hand later if you want.')
                    break 
                else:    
                    print ('Enter y or n.')
        seriesScore += handscore
        print ('Your total score after that hand is: '+str(seriesScore))
        totalhands -= 1
    print ('Great job!  Your final score was : '+str(seriesScore))


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
