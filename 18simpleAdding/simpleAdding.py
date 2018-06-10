#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function SimpleAdding(num) add up all the
numbers from 1 to num. For example: if the input is 4 then your program should
return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num
will be any number from 1 to 1000.

Created on Fri Jun  8 09:29:50 2018

@author: shane
"""

def SimpleAdding(num): 
    
    num = sum(range(int(num) + 1))
    
    return num

if __name__ == '__main__':
    # keep this function call here  
    print(SimpleAdding(input()))