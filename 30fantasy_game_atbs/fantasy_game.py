#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:39:11 2018

@author: shane
"""

def displayInventory(inv_dict):
    print('Inventory:')
    
    for k, v in inv_dict.items():
        print(str(v) + ' ' + str(k))
    
    total = sum(list(inv_dict.values()))

    print('Total number of items: ' + str(total))

def addToInventory(inv, loot):
    # Update the inventory
    for item in loot:
        if item in inv.keys():
            inv[item] += 1
        else:
             inv[item] = 1
    
    return inv

if __name__ == '__main__':
    
    stuff = {'rope':1,
             'torch': 6,
             'gold coin': 42,
             'dagger': 1,
             'arrow': 12}
    
    displayInventory(stuff)
    
    print('\n')
    
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    
    inv = addToInventory(inv, dragonLoot)
    
    displayInventory(inv)