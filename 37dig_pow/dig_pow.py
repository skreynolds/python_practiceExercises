#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a positive integer n written as abcd... (a, b, c, d... being digits) and
a positive integer p we want to find a positive integer k, if it exists, such
as the sum of the digits of n taken to the successive powers of p is equal to
k * n. In other words:

Is there an integer k such as :
    (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n, p will always be given as strictly positive integers.

Created on Thu Jun 14 10:15:30 2018

@author: shane
"""

def dig_pow(n, p):
    
    num = str(n)
    out = []
    '''
    while num != 0:
        out.append(num % 10)
        num = num // 10
    out.reverse()
    '''
    for digit in num:
        out.append(int(digit))
    
    k = (1/n)*sum([e**(p+i) for i,e in enumerate(out)])
    print(k)
    if k.is_integer():
        return int(k)
    
    return -1

if __name__ == '__main__':
    print(dig_pow(5468, 3))