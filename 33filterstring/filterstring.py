#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In this kata you will create a function that takes a list of non-negative
integers and strings and returns a new list with the strings filtered out.

Created on Mon Jun 11 09:04:50 2018

@author: shane
"""

def filter_string(input_list):
    return [e for e in input_list if type(e) != str]

if __name__ == '__main__':
    print(filter_string([1,2,'a','b']))
    print(filter_string([1,2,'aasf','1','123',123]))
    