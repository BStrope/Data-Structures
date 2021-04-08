# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:46:33 2021

@author: -Benjamin Strope
"""
from datatypes import Deque

def pal_checker(a_string):
    '''Checks a string entered to see if it is a palindrome'''
    
    d = Deque()
    still_equal = True
    for letter in a_string:
        d.add_rear(letter)
    
    while d.size() > 1 and still_equal:
        front = d.remove_front()
        rear = d.remove_rear()
        if front != rear:
            still_equal = False
    
    return still_equal

print(pal_checker('tacocat'))
print(pal_checker('none'))
