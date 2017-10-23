#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:35:58 2017

@author: shane
"""

from sympy import *

def transMat(q, alpha, d, a):
    T = Matrix([[           cos(q),           -sin(q),           0,             a],
                [sin(q)*cos(alpha), cos(q)*cos(alpha), -sin(alpha), -sin(alpha)*d],
                [sin(q)*sin(alpha), cos(q)*sin(alpha),  cos(alpha),  cos(alpha)*d],
                [                 0,                0,           0,             1]])
    return T

q1, q2, q3, q4, q5, q6, q7 = symbols('q1:8')
d1, d2, d3, d4, d5, d6, d7 = symbols('d1:8')
a0, a1, a2, a3, a4, a5, a6 = symbols('a0:7')
alpha0, alpha1, alpha2, alpha3, alpha4, alpha5, alpha6 = symbols('alpha0:7')


s = {alpha0:     0,    a0:      0,    d1: 0.68,
     alpha1: -pi/2,    a1:   0.42,    d2:    0,    q2: (q2 - pi/2),
     alpha2:     0,    a2:   1.25,    d3:    0,
     alpha3: -pi/2,    a3: -0.054,    d4:  1.5,
     alpha4:  pi/2,    a4:      0,    d5:    0,
     alpha5: -pi/2,    a5:      0,    d6:    0,
     alpha6:     0,    a6:      0,    d7: 0.11,    q7: 0}

T0_1 = transMat(q1, alpha0, d1, a0)
T1_2 = transMat(q2, alpha1, d2, a1)
T2_3 = transMat(q3, alpha2, d3, a2)
T3_4 = transMat(q4, alpha3, d4, a3)
T4_5 = transMat(q5, alpha4, d5, a4)
T5_6 = transMat(q5, alpha5, d6, a5)
T6_7 = transMat(q7, alpha6, d7, a6)

T0_1 = T0_1.subs(s)
T1_2 = T1_2.subs(s)
T2_3 = T2_3.subs(s)
T3_4 = T3_4.subs(s)
T4_5 = T4_5.subs(s)
T5_6 = T5_6.subs(s)
T6_7 = T6_7.subs(s)

T0_2 = T0_1*T1_2
T0_3 = T0_2*T2_3
T0_4 = T0_3*T3_4
T0_5 = T0_4*T4_5
T0_6 = T0_5*T5_6
T0_7 = T0_6*T6_7

R0_1 = T0_1[0:3,0:3]
R1_2 = T1_2[0:3,0:3]
R2_3 = T2_3[0:3,0:3]
R3_4 = T3_4[0:3,0:3]
R4_5 = T4_5[0:3,0:3]
R5_6 = T5_6[0:3,0:3]
R6_7 = T6_7[0:3,0:3]