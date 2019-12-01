#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:10:24 2019

@author: ramonaD
"""
## advent of code 2019
# Day one
import math
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

#part one
with open('input.txt') as f:
    #result = []
    sum = 0
    for line in f:
        print("----------------------")
        operation = line
        partial_result = 0
        while (operation > 0):
            operation = round_down((float(operation)/3)-2)
            print("result", operation)
            if (operation <= 0):
                operation = 0
            partial_result = partial_result + operation
            print("partial result",partial_result)
            if (operation <= 0):
                break
        sum = sum+partial_result
#        print(line, 'fuel required is: ', partial_result)
        print('Total fuel required is: ', sum)
    
#part two


#while (operation>):
    