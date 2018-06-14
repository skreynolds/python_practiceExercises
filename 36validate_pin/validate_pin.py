#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Created on Wed Jun 13 12:38:26 2018

@author: shane
"""

def validate_pin(pin):
    output = False
    if ((len(pin) == 4) or (len(pin) == 6)) and pin.isdigit():
        output = True
    return output

if __name__ == '__main__':
    print(validate_pin("12345"))