#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:35:14 2017

Modify the previous program such that only the users Alice
and Bob are greeted with their names.

@author: shane
"""

in_name = input("Enter your name: ")

if (in_name == "Bob" or in_name == "Alice"):
    print("Hello " + in_name + "!")