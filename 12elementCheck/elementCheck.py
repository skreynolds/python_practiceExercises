#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:03:15 2017

Write a function that checks whether an element occurs in a list.

@author: shane
"""

def elementCheck(someList,element):
    
    inList = False
    
    for e in someList:
        if (e == element):
            inList = True
    
    return inList