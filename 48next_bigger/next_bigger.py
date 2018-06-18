#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 19:40:21 2018

@author: shane
"""
import itertools as it

def next_bigger(n):
    num = [int(e) for e in str(n)]
    perm_tuple = list(it.permutations(num,len(num)))
    perm_list = []
    
    for tup in perm_tuple:
        perm_list.append(int(''.join(str(w) for w in tup)))
    
    perm_list.sort()
    
    for number in perm_list:
        if number > n:
            return number
    
    return -1

if __name__ == '__main__':
    print(next_bigger(2541))