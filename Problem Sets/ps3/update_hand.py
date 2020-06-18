# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:39:14 2020

@author: Kirk
"""
hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}


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
    print()   

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

    
  