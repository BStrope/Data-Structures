# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:41:38 2021

@author: - Benjamin Strope
"""
from datatypes import Queue

def hot_potato(players,passes):
    q = Queue()
    for player in players:
        q.enqueue(player)
    
    while q.size() > 1:
        for i in range(passes):
                has_potato = q.dequeue()
                q.enqueue(has_potato)
        q.dequeue()
    return q.dequeue()
        
print(hot_potato(['Bill','David','Susan','Jane','Kent','Brad'], 7))