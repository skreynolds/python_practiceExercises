#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function AlphabetSoup(str) take the str
string parameter being passed and return the string with the letters in
alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation
symbols will not be included in the string.

Created on Sun Jun 10 10:20:21 2018

@author: shane
"""

def AlphabetSoup(str):
    out = list(str)
    out.sort()
    out = ''.join(out)
    return out 

if __name__ == '__main__':
    print(AlphabetSoup(input()))