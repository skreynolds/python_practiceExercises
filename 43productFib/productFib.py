#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 11:02:36 2018

@author: shane
"""
'''

This is the recursive method of performing fibonnaci method

Very computationally expensive - the cheaper way is to use a generator

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
'''

# Using a generator to create the fibonnaci sequence

def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b


def productFib(prod):
    
    # initialise fibonnaci generator
    fib_gen = fib()
    f1 = next(fib_gen)
    f2 = next(fib_gen)
    
    while(True):
        
        # evaluation of fibonnaci product
        temp = f1*f2
        
        # check conditions
        if temp == prod:
            out = [f1, f2, True]
            break
        elif temp > prod:
            out = [f1, f2, False]
            break
        
        # iterate the fibonnaci generator forward by one
        f1 = f2
        f2 = next(fib_gen)
        
    return out
    

if __name__ == '__main__':
    print(productFib(5895))