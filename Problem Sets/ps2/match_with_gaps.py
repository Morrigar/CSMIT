# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:09:42 2020

@author: Kirk
"""
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


wordlist = load_words()

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

