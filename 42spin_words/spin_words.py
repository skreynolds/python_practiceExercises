#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function that takes in a string of one or more words, and returns the
same string, but with all five or more letter words reversed (Just like the
name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Created on Sat Jun 16 11:59:43 2018

@author: shane
"""

def spin_words(sentence):
    # convert string to list of words
    string_list = sentence.split()
    
    for i, word in enumerate(string_list):
        if len(word) > 4:
            word = word[::-1]
            string_list[i] = word
    
    rev_sentence = ' '.join(string_list)
    
    return rev_sentence

if __name__ == '__main__':
    print(spin_words("Hey fellow warriors"))