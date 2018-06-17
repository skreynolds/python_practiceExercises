#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as
parameter. If the board is valid return 'Finished!', otherwise return
'Try again!'

Created on Sun Jun 17 14:36:25 2018

@author: shane
"""

import numpy as np

def done_or_not(board): #board[i][j]
    np_board = np.asarray(board)
    
    for i in range(9):
        if set(np_board[i,:]) != set([1,2,3,4,5,6,7,8,9]):
            return 'Try again!'
    
    for j in range(9):
        if set(np_board[:,j]) != set([1,2,3,4,5,6,7,8,9]):
            return 'Try again!'
    
    for i in range(3):
        for j in range(3):
            if set(np_board[3*i:3*i+3,3*j:3*j+3].flatten()) != set([1,2,3,4,5,6,7,8,9]):
                return 'Try again!'
            
    return 'Finished!'

if __name__ == '__main__':
    print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))
    print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))