#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:15:52 2017

Write a function that returns the elements on odd positions in a list.

@author: shane
"""

def oddElements(someList):
    
    """Function developed with a list comprehension"""
    return [someList[i] for i in range(0,len(someList)) if i%2 == 0]
    
    
    """
    Function developed with normal for loops
    newList = []
    for e in someList[1:len(someList):2]:
        newList.append(e)
    
    return newList
    """