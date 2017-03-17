#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:00:00 2017

Modify the previous program such that only multiples of three or five are
considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

@author: shane
"""

number = int(input("Enter a number:"))

list_comprehension = [x for x in range(1,number+1) if x%3 == 0 or x%5 == 0]

print(sum(list_comprehension))