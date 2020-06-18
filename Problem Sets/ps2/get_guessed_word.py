# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:50:17 2020

@author: Kirk
"""

secret_word = "apple"
letters_guessed = ['e','i',',k','p','r','s','l']

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
    return mw

print(get_guessed_word(secret_word, letters_guessed))
                