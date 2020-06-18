#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:21:59 2020

@author: ksripinyo
"""

def dictionary_shift (shift):
    """ Expects a value to shift the dictionary by, returns a shifted
    upper and lowercase dictionary """
    
    dictionary = {}
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = shift % 26
    print (shift)
    
    for i in range (0, 26-shift):
        dictionary[lower[i]]=lower[i+shift]
    for i in range (26-shift, 26):
        dictionary[lower[i]] = lower [abs(26-shift-i)]
    for i in range (0, 26-shift):
        dictionary[upper[i]]=upper[i+shift]
    for i in range (26-shift, 26):
        dictionary[upper[i]] = upper [abs(26-shift-i)]
    return dictionary

def dictionary_shift2 (shift):
    """ Expects a value to shift the dictionary by, returns a shifted
    upper and lowercase dictionary """
    
    dictionary = {}
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = shift % 26
    print (shift)
    slower = lower[shift:]+lower[0:shift]
    supper = upper[shift:]+upper[0:shift]
    
    for i in range (0,26):
        dictionary[lower[i]]=slower[i]
        dictionary[upper[i]]=supper[i]
    
    return dictionary