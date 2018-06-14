#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A digital root is the recursive sum of all the digits in a number. Given n,
take the sum of the digits of n. If that value has two digits, continue
reducing in this way until a single-digit number is produced. This is only
applicable to the natural numbers.

Created on Thu Jun 14 10:52:33 2018

@author: shane
"""

def digital_root(n):
    
    num = list(str(n))
    
    if len(num) == 2:
        return int(num[0]) + int(num[1])
    elif len(num) == 1: 
        return int(num[0])
    else:
        return digital_root(sum([int(e) for e in num]))
    
if __name__ == '__main__':
    print(digital_root(16))
    print(digital_root(99999999999999))