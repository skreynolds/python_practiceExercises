#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The maximum sum subarray problem consists in finding the maximum sum of a
contiguous subsequence in an array or list of integers

Created on Sat Jun 16 10:46:32 2018

@author: shane
"""

def maxSequence(arr):
    
    # initialise values
    n = len(arr)
    max_out = 0
    
    
    if n == 0:
        return 0
    elif n == 1:
        return max_out
    else:
        # create all the different window widths to slide over the array
        for x in range(2,n):
            # slide the current window over the array
            for i in range(n-1):
                temp = sum(arr[i:i+x])
                if temp > max_out:
                    max_out = temp
    
    return max_out

if __name__ == '__main__':
    print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))