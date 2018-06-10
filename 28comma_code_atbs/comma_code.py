#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:23:35 2018

@author: shane
"""

def comma_code(list_items):
    
    string = ''
    
    for i, e in enumerate(list_items):
        if i != (len(list_items)-1):
            string = string + e + ', '
        else:
            string = string +  'and ' + e

    return string

if __name__ == '__main__':

    spam = ['apples', 'bananas', 'tofu', 'cats']

    output = comma_code(spam)
    print(output)