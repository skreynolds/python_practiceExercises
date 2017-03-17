#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:09:50 2017

Write a program that prints all prime numbers up to a given number.

@author: shane
"""

import math

number = int(input("Enter a number: "))

for n in range(1, number+1):
    
    sentinel = True
    
    upperLim = math.floor(n**0.5)
    
    for i in range(2,upperLim+1):
        if (n%i == 0):
            sentinel = False
            break
    if (sentinel == True):
        print(n)