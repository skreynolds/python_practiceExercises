#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:46:49 2017

Write a function that returns the largest element in a list.

@author: shane
"""

def maxvalue(someList):
    
    maxElement = None
    
    for e in someList:
        if (maxElement == None) or (e > maxElement):
            maxElement = e
    return maxElement