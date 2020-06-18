#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:39:21 2020

@author: ksripinyo
"""
import string

letters_guessed = ['a','x','c','e','q','p']

def get_available_letters(letters_guessed):
    """
    Takes in letters_guessed and returns a string of lowercase english letters
    that are available to be guessed.
    
    """
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

print (get_available_letters(letters_guessed))
    