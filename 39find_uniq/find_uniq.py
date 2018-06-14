#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
There is an array with some numbers. All numbers are equal except for one.
Try to find it!

Created on Thu Jun 14 11:31:11 2018

@author: shane
"""

def find_uniq(arr):
    arr_set = set(arr)
    for e in arr_set:
        if arr.count(e) == 1:
            n = e
            break
    return n   # n: unique integer in the array
    
if __name__ == '__main__':
    print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))