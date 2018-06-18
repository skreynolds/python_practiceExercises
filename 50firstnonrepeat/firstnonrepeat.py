#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function named firstNonRepeatingLetter† that takes a string input, and
returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the
string.

Created on Mon Jun 18 21:18:06 2018

@author: shane
"""

def first_non_repeating_letter(string):
    
    string_copy = string.lower()
    
    for i,e in enumerate(string_copy):
        if e not in string_copy[:i]+string_copy[i+1:]:
            return string[i]
    return ''
    
if __name__ == '__main__':
    print(first_non_repeating_letter('Basic Tests'))