# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 03:02:07 2019

@author: Bill Liu
"""

number = input('Please input the number:')
number_list = number.split('.')
interger_part = number_list[0]
base = 2

if len(number_list) > 1:
    fractional_part = number_list[1]
else:
    fractional_part = '0'

target_number = 0

for i in range(len(interger_part) - 1, -1, -1):
    target_number = target_number + int(interger_part[i]) * (base**(len(interger_part) - 1 - i))

for j in range(len(fractional_part)):
    target_number = target_number + int(fractional_part[j]) * (base ** (-j - 1))

print(target_number)