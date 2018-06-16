#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function that takes a string of braces, and determines if the order of
the braces is valid. It should return true if the string is valid, and false
if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new
characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses,
brackets and curly braces: ()[]{}.

Created on Sat Jun 16 11:50:42 2018

@author: shane
"""

def validBraces_better(string):
    
    braces = {'(':')', '[':']', '{':'}'}
    stack = []
    
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
            
    return len(stack) == 0

if __name__ == '__main__':
    print(validBraces_better("[({"))
    print(validBraces_better("([{}])"))