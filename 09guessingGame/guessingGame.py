#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:31:16 2017

Write a guessing game where the user has to guess a secret number. After
every guess the program tells the user whether their number was too large
or too small. At the end the number of tries needed should be printed. I
counts only as one try if they input the same number multiple times
consecutively.

@author: shane
"""

number = int(input("Enter a number: "))

while(True):
    guess = int(input("Guess the number: "))
    if (guess < number):
        print("Your guess is too low.")
        continue
    elif (guess > number):
        print("Your guess is too high.")
        continue
    else:
        print("You guessed the number")
        break