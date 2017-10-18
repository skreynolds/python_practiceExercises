#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:16:49 2017

@author: shane
"""

import random as rand
import matplotlib.pyplot as plt

'''Specify the number of people in the simulation and initialise
key simulation parameters'''
num_of_ppl = 31 # number of ppl in the simulation
ppl = list(range(1,num_of_ppl+1)) # create mutable list object of ppl

'''Select initial person to be infected and create initial
time stamp of the simulation'''          
simulation_dict = {} # intialise simulation dict
inf_list = [] # initalise the infection list
rand_int = rand.randint(1,num_of_ppl) # generate rand int
print('********Initialising simulation********\n')
print(str(rand_int) + ' initially infected.')
ppl_idx = ppl.index(rand_int)
person = ppl.pop(ppl_idx) # strip list of infected person
inf_list.append(person) # append the infected person to the list
time = 0 # time is initialised at 0
simulation_dict[time] = inf_list # create a dictionary entry

'''Simulate until all people in the list are infected'''
while ppl:
    print('\n********Iteration number '+str(time+1)+'********\n')
    inf_list = list(inf_list)
    for p in simulation_dict[time]:
        rand_int = rand.randint(1,num_of_ppl) # generate rand int
        if (rand_int not in simulation_dict[time]
            and rand_int not in inf_list):
            
            print(str(rand_int) + ' got infected.')
            ppl_idx = ppl.index(rand_int)
            person = ppl.pop(ppl_idx) # strip list of infected person
            inf_list.append(person) # append the infected person to the list
        
        else:
            print(str(rand_int) + ' is already infected.')
            
    time += 1
    simulation_dict[time] = inf_list



time = [key for key in simulation_dict.keys()]
cum_num_inf = []           
for key in simulation_dict.keys():
    cum_num_inf.append(len(simulation_dict[key]))

plt.stem(time,cum_num_inf)
plt.show()