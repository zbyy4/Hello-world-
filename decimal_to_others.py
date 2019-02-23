# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 02:19:12 2019

@author: Bill Liu
"""

decimal_number = eval(input('Please input the decimal number:'))
base = 2
number_fractional_postions = 10
integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part
target_interger = list()

while integer_part != 0:
    remainder = integer_part % base
    target_interger.append(remainder)
    integer_part = integer_part//base

target_interger.reverse()

for i in range(len(target_interger)):
    print(target_interger[i], end = '')

#for i in range(len(target_interger) - 1, -1, -1):
#    print(target_interger[i], end = '')

print('.', end = '')

for j in range(number_fractional_postions):
    integer_part = int(fractional_part * base)
    fractional_part = fractional_part * base - integer_part
    print(integer_part, end = '')