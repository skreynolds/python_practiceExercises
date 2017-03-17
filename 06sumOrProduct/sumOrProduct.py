#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:16:44 2017

Write a program that asks the user for a number n and gives him the
possibility to choose between computing the sum and computing the product of 1,…,n.

@author: shane
"""

import numpy as np

number = int(input("Enter a number:"))
selection = input("Sum or Product?")

if (selection == "Sum"):
    print(sum(list(range(1,number+1))))
elif (selection == "Product"):
    print(np.prod(np.array(list(range(1,number+1)))))