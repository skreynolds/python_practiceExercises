#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function called that takes a string of parentheses, and determines
if the order of the parentheses is valid. The function should return true if
the string is valid, and false if it's invalid.

Created on Sun Jun 17 16:07:23 2018

@author: shane
"""

def valid_parentheses(string):
    
    
    stack = []
    
    for e in string:
        if e == '(':
            stack.append(e)
        elif e == ')':
            try:
                stack.pop()
            except:
                return False
            
    return len(stack) == 0

if __name__ == '__main__':
    print(valid_parentheses("hi(hi)("))