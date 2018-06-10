#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the Python language, have the function TimeConvert(num) take the num
parameter being passed and return the number of hours and minutes the parameter
converts to (ie. if num = 63 then the output should be 1:3). Separate the
number of hours and minutes with a colon.

Created on Sun Jun 10 10:13:33 2018

@author: shane
"""

def TimeConvert(num):
    # Convert the input to an integer
    num = int(num)
    # Return the time
    return str(num // 60) + ':' + str(num % 60)

if __name__ == '__main__':
    print(TimeConvert(input()))