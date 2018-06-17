#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROT13 is a simple letter substitution cipher that replaces a letter with the
letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar
cipher.

Create a function that takes a string and returns the string ciphered with
Rot13. If there are numbers or special characters included in the string, they
should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
Created on Sun Jun 17 15:40:23 2018

@author: shane
"""

import string
from codecs import encode as _dont_use_this_

def rot13(message):
    
    alph = 'abcdefghijklmnopqrstuvwxyz'
    
    #initialise output
    out_string = ''
        
    for e in message:
        
        num = (ord(e.lower()) - 97) + 13
        
        if num > 26:
            num -= 26
        
        if e.isupper():
            out_string += chr(num+97).upper()
        else:
            out_string += chr(num+97)
            
    return out_string
        

if __name__ == '__main__':
    print(rot13("Test"))