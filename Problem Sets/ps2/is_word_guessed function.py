# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:30:59 2020

@author: Kirk
"""


secret_word = 'apple'
letters_guessed = ['a', 'l', 'e']

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
       #print('Trying '+char+'.')
       if char not in letters_guessed:
           return False
    return True
       
print(is_word_guessed(secret_word, letters_guessed))
