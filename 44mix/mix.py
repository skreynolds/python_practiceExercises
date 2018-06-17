#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given two strings s1 and s2, we want to visualize how different the two strings
are. We will only take into account the lowercase letters (a to z). First let
us count the frequency of each lowercase letters in s1 and s2.

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3
from s2. In the following we will not consider letters when the maximum of
their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string:
"1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the
maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb
because the maximum for b is 3.

Created on Sun Jun 17 11:57:45 2018

@author: shane
"""

def mix(s1, s2):
    
    # create a dictionary of letter for s1 and s1
    s1_dict = {key:s1.count(key) for key in set(s1) if key.isalpha() and key.islower()}
    s2_dict = {key:s2.count(key) for key in set(s2) if key.isalpha() and key.islower()}
    
    allkeys = list(set().union(*[s1_dict.keys(), s2_dict.keys()]))
    allkeys.sort()
    
    out_dict = {}
    
    for key in allkeys:
        
        # there may be key errors present here
        try:
            s1_value = s1_dict[key]
        except KeyError:
            s1_value = 0
            
        # there may be key errors present here
        try:
            s2_value = s2_dict[key]
        except KeyError:
            s2_value = 0
        
        if s1_value > s2_value:
            out_dict[str(s1_value) + str(key)] = '1:'
        elif s1_value < s2_value:
            out_dict[str(s2_value) + str(key)] = '2:'
        else:
            out_dict[str(s1_value) + str(key)] = '=:'
    
    final_list = sorted(list(out_dict.keys()))
    final_list.reverse()
    
    return '/'.join([out_dict[key] + int(key[:-1])*key[-1] for key in final_list])
        

if __name__ == '__main__':
    print(mix("Are they here", "yes, they are here"))
    