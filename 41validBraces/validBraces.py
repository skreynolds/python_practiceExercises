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

Created on Sat Jun 16 11:29:03 2018

@author: shane
"""

def validBraces(string):
    
    # initialise storage space
    temp = []
    
    for e in string:
        if e in '({[':
            temp.append(e)
        elif len(temp) == 0:
            return False
        else:
            test = temp.pop()
            if ( e == ')' and test != '('
                    or e == ']' and test != '['
                        or e == '}' and test != '{' ):
                        
                        return False
    
    if len(temp) != 0: return False
    
    return True

if __name__ == '__main__':
    print(validBraces("[({"))
    print(validBraces("([{}])"))