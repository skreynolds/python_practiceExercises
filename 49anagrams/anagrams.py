#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function that will find all the anagrams of a word from a list. You
will be given two inputs a word and an array with words. You should return an
array of all the anagrams or an empty array if there are none. 

Created on Mon Jun 18 20:53:45 2018

@author: shane
"""

def anagrams(word, words):
    
    output = []
    
    word = list(word)
    word.sort()
    
    for item in words:
        temp = list(item)
        temp.sort()
        if temp == word:
            output.append(item)
            
    return output

if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))