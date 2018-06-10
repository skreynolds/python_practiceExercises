# -*- coding: utf-8 -*-
"""

Your task is to make a function that can take any non-negative integer as a
argument and return it with its digits in descending order. Essentially,
rearrange the digits to create the highest possible number.

Spyder Editor

This is a temporary script file.
"""

def numord(num):
    
    temp = [e for e in str(num)]
    temp.sort()
    temp = reversed(temp)
    out = int(''.join(temp))
    
    return out

if __name__ == '__main__':
    print(numord(21445))
    print(numord(145263))