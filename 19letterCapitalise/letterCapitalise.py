#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function LetterCapitalize(str) take the str
parameter being passed and capitalize the first letter of each word. Words will
be separated by only one space.

Created on Fri Jun  8 09:34:56 2018

@author: shane
"""

def LetterCapitalize(str): 
    
    assert len(str) != 0
    
    str = str.split()
    
    for i, word in enumerate(str):
        word = word[0].upper() + word[1:]
        str[i] = word
           
    str = ' '.join(str)
    
    return str

if __name__ == '__main__':
    # keep this function call here
    print(LetterCapitalize(input()))