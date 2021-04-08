# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:09:09 2021

@author: -
"""

from datatypes import Stack

def base_converter(number,base):
    '''converts numerical to binary,hexadeciman,octal,etc'''
    s = Stack()
    stack_list = []
    digits = '0123456789ABCDEF'
    binary_string = ''
    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base
    
    while s.empty() == False:
        stack_list.append(s.peek())
        binary_string += digits[s.pop()]
    
    return binary_string, stack_list

print(base_converter(17,2))
print(base_converter(45,2))
print(base_converter(96,2))