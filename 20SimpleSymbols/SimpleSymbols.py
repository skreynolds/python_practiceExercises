#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function SimpleSymbols(str) take the str
parameter being passed and determine if it is an acceptable sequence by either
returning the string true or false. The str parameter will be composed of +
and = symbols with several letters between them (ie. ++d+===+c++==a) and for
the string to be true each letter must be surrounded by a + symbol. So the
string to the left would be false. The string will not be empty and will have
at least one letter. 

Created on Sat Jun  9 08:13:16 2018

@author: shane
"""

def SimpleSymbols(str): 
    
    out = 'true'

    if str[0].isalpha() and str[1] == '+': return 'false'
    if str[-1].isalpha() and str[-2] == '+': return 'false'
    
    if len(str) > 2:
        for i, e in enumerate(str):
            if e.isalpha() and (i != 0 or i != len(str)):
                if str[i-1] != '+' or str[i+1] != '+':
                    out = 'false'
    str = out
    
    return str

if __name__ == '__main__':
    # keep this function call here  
    print(SimpleSymbols(input()))