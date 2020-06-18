# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:54:45 2020

@author: Kirk
"""
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

VOWELS = 'aeiou'
hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
word = "honey"


word_list = load_words()

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
    freq = get_frequency_dict(word)#for letter in word:
        
    def letters_in_hand(freq):
        print (freq)
        for i in freq:
            print ('Testing '+ i)
            print ('# of '+i+' = '+str(freq[i])+'# of '+i+' in hand = '+str(hand.get(i,0)))
            if freq[i] > hand.get(i,0):
                print ('"'+i+'"'+ ' not in hand, about to return False.')
                return False
        return True

    
    def substar_search(word):
        wcpos = word.find('*')
        print ("In substar_search.")
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
                print (word)
                if word in word_list:
                    return True
            
    if '*' not in word:   
        if not letters_in_hand(freq):
            return False
        elif letters_in_hand(freq) and word in word_list:
            return True
    else:
        if letters_in_hand(freq) and substar_search(word):
            return True
        return False
         
    
 # TO DO... Remove this line when you implement this function


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

