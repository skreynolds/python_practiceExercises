#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:06:12 2017

Write a program that prints a multiplication table for numbers up to 12.

@author: shane
"""

number = int(input("Enter a number: "))

for n in range(1,13):
    print(str(n) + "x" + str(number) + "=" + str(n*number))