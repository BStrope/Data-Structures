# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:21:53 2021
Last Edited Mar 23 14:26 2021
@author: - Benjamin Strope
"""
class HashTable:
    '''hash_function implements the remainder method
        collision resolution technique is linear probing with plus 1 rehash
        function'''
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def hash_function(self,key,size):
        return key % size
    def rehash(self,old_hash,size):
        return (old_hash + 1) % size
    
    def put(self,key,data):
        hash_value = self.hash_function(key,len(self.slots))
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data #replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and \
                    self.slots[next_slot] != key:
                        next_slot = self.rehash(next_slot,len(self.slots))
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data #replace
    
    def get(self,key):
        start_slot = self.hash_function(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data 

#next two methods allow access using '[]' and familiar index operator can be used
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
            
def sequential_search(a_list,item):
    ''' search a list one item at a time at each index in a row'''
    pos = 0
    found = False
    
    while not found and pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            pos +=1
    return found 

def ordered_sequential_search(a_list,item):
    pos = 0
    
    while a_list[pos] <= item and pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            pos += 1
    return False

def binary_search(a_list,item):
    
    low = 0
    high = len(a_list) - 1
    
    found = False
    
    while low <= high and not found:
        mid = (low + high) // 2
        
        if a_list[mid] == item:
            found = True
        elif a_list[mid] < item:
            low = mid + 1
        elif a_list[mid] > item:
            high = mid - 1
    
    return found

def binary_search_recursive(a_list,item):
    
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        
        if a_list[midpoint] == item:
            return True
        elif a_list[midpoint] < item:
            return binary_search_recursive(a_list[midpoint + 1:], item)
        elif a_list[midpoint] > item:
            return binary_search_recursive(a_list[:midpoint - 1], item)
        
