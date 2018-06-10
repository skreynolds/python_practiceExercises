#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function FirstReverse(str) take the str
parameter being passed and return the string in reversed order. For example:
if the input string is "Hello World and Coders" then your program should return
the string sredoC dna dlroW olleH.

Created on Fri Jun  8 08:41:21 2018

@author: shane
"""

def FirstReverse(str): 
    
    # Assert that the string has to have characters in it    
    assert len(str) != 0
    
    # Reverse the string
    str = list(str)
    str = str[::-1]
    str = ''.join(str)
    
    return str

if __name__ == '__main__':
    # keep this function call here  
    print(FirstReverse(input()))