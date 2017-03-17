#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:58:14 2017

Write function that reverses a list, preferably in place.

@author: shane
"""

def listReverse(someList):
    outputList = []
    copy_someList = someList[:]
    
    for e in someList:
        outputList.append(copy_someList.pop())
        
    return outputList