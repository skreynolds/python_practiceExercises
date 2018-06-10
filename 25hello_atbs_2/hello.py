#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:40:44 2018

@author: shane
"""

def spam_test(spam):
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Greetings!')
        
if __name__ == '__main__':
    spam = 1
    spam_test(spam)
    spam = 2
    spam_test(spam)
    spam = 'spam'
    spam_test(spam)