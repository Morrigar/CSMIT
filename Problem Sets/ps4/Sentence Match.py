# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:50:49 2020

@author: Kirk
"""
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

wordlist = load_words('words.txt')

def word_match_count (sentence):

    splitwords = sentence.split (' ')
    realWordCount = 0
    for i in range (0,len(splitwords)):
        splitwords[i] = splitwords[i].strip(' !@#$%^&*()-_+={}[]|\:;<>?,./\"\'')
    
    for word in splitwords:
        if word.lower() in wordlist:
            realWordCount +=1
        
    return (splitwords, realWordCount)

 

