#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:43:06 2017

Write a program that asks the user for a number n and prints the
sum of the numbers 1 to n

@author: shane
"""

number = int(input("Enter a number: "))
out = 0

print(sum(list(range(1,number+1))))

"""
An alternative way of printing using simple loops
for i in range(1,number+1):
    out += i
    
print(out)
"""