#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 08:54:29 2018

@author: shane

Create a function named divisors/Divisors that takes an integer n > 1 and
returns an array with all of the integer's divisors(except for 1 and the number
itself), from smallest to largest. If the number is prime return the string
'(integer) is prime'

"""

def divisors(n):
    out = []
    for divisor in range(2,n):
        if n % divisor == 0:
            out.append(divisor)
    if len(out) == 0:
        out = str(n) + ' is a prime'
        
    return out

if __name__ == '__main__':
    print(divisors(16))
    print(divisors(13))