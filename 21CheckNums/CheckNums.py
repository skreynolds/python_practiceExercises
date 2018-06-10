#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function CheckNums(num1,num2) take both
parameters being passed and return the string true if num2 is greater than
num1, otherwise return the string false. If the parameter values are equal to
each other then return the string -1.

Created on Sat Jun  9 08:32:14 2018

@author: shane
"""

def CheckNums(num1,num2): 
    
    if num1 == num2:
        out = '-1'
    elif num1 > num2:
        out = 'true'
    else:
        out = 'false'
    # code goes here 
    return out

if __name__ == '__main__':
    # keep this function call here  
    print(CheckNums(8,8))