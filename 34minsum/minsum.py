#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a function that returns the sum of the two lowest positive numbers
given an array of minimum 4 integers. No floats or empty arrays will be passed.

Created on Wed Jun 13 12:21:22 2018

@author: shane
"""

def minsum(arr):
    arr.sort()
    return arr[0]+arr[1]

if __name__ == '__main__':
    print(minsum([19, 5, 42, 2, 77]))