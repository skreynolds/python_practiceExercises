#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:47:47 2018

@author: shane
"""

def collatz(number):
    if number%2 == 0:
        x = number // 2
    else:
        x = 3*number + 1
    
    print(x)
    
    return x

if __name__ == '__main__':
    
    '''User input number'''
    print('Input a number:')
    number = input()
    try:
        number = int(number)
        '''Loop until number converges to 1'''
        while number != 1:
            number = collatz(number)
    except:
        print('This is not a number.')
    