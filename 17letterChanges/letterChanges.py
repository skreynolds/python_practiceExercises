#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function LetterChanges(str) take the str
parameter being passed and modify it using the following algorithm. Replace
every letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
(a, e, i, o, u) and finally return this modified string.

Created on Fri Jun  8 08:56:55 2018

@author: shane
"""

def LetterChanges(str): 
    
    # Ensure that the string entered has characters
    assert len(str) != 0
    
    # Ensure that string is all lower case
    str = str.lower()           
    
    # Iniitalise the out string
    out = ''
    
    # Perform desired action
    for e in str:
        if e.isalpha():
            if e == 'z':
                temp = 'a'
            else:        
                temp = chr(ord(e) + 1)
                if temp in ['a','e','i','o','u']:
                    out += temp.upper()
                else:
                    out += temp
        else:
            out += e
    
    str = out
    
    return str

if __name__ == '__main__':
    # keep this function call here  
    print(LetterChanges(input()))  