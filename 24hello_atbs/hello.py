#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:20:26 2018

@author: shane
"""

# This program is the introductory program for automate the boring stuff

print('Hello World!')
print('What is your name?') # ask for name

myName = input()

print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for age

myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')