# -*- coding: utf-8 -*-
"""
Spyder Editor
creator - Benjamin Strope
last Edited: March 12 2021 12:10 
Modules of linear datatypes
"""

class Stack:
    '''linear structure, shortest var in is first one out'''
    def __init__(self):
        self.items = []
    def empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() 
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    
class Queue:
    '''opposite from stack, longest in is removed'''
    def __init__(self):
        self.items = []    
    def empty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item) 
    def dequeue(self):
        return self.items.pop()    
    def size(self):
        return len(self.items)
    
class Deque:
    '''Two sided linear structure, can add to end and front and remove from both'''
    def __init__(self):
        self.items = []        
    def add_front(self,item):
        self.items.append(item)   
    def add_rear(self,item):
        self.items.insert(0, item)       
    def size(self):
        return len(self.items)    
    def empty(self):
        return self.items == []   
    def remove_rear(self):
        return self.items.pop(0)   
    def remove_front(self):
        return self.items.pop()
    
class Node:
    '''creates a node with data for stringing in unordered list class'''
    def __init__(self,init_data):
        self.data = init_data
        self.next = None 
    def get_data(self):
        return self.data 
    def get_next(self):
        return self.next  
    def set_data(self,new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
        
class Unordered_List:
    '''creates an unordered list: indexing from the head. Linked so can 
    traverse the linked nodes
        Still need to make the pop() method O(1)'''
    def __init__(self):
        self.head = None
    def empty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def search(self,item):
        
        current = self.head
        found = False
        while not found and current != None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found 
    
    def size(self):
        counter = 0
        current = self.head 
        while current != None:
            counter += 1
            current.get_next()
        return counter
    
    def remove(self,item):
        previous = None
        current = self.head
        found = False
        while not found:
            if current == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    def append(self,item):
        previous = None
        current = self.head
        
        while current != None:
            previous = current
            current = current.get_next()
        current.set_next(None)
        previous.set_next(item)
    
    def index(self,position):
        current = self.head
        if position == 0:
            return current.get_data()
        else:
            for node in range(1,position):
                current = current.get_next()
        return current.get_data()
                
    def pop(self,position):
        previous = None
        current = self.head
        
        for pos in range(position):
            previous = current
            current = current.get_next()
        pop = current
        previous.set_next(current.get_next())
        return pop
    
    def insert(self,position,item):
        current = self.head
        for pos in range(position):
            current = current.get_next()
        current.set_next(item)

class OrderedList:
    def __init__(self):
        self.head = None
    def empty(self):
        return self.head == None
    def size(self):
        counter = 0
        current = self.head 
        while current != None:
            counter += 1
            current.get_next()
        return counter
    def remove(self,item):
        previous = None
        current = self.head
        found = False
        while not found:
            if current == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
        def search(self,item):
            current = self.head
            found = False
            while found and (current.get_data() <= item):
                if current.get_data() == item:
                    found = True
                else:
                    current = current.get_next()
            return found
        
        def add(self,item):
            stop = False
            previous = None
            current = self.head
            
            while not stop and current != None:
                if current.get_data() >= item:
                    stop = True
                else:
                    previous = current
                    current = current.get_next()
            temp = Node(item)
            if previous == None:
                temp.set_next(self.head)
                self.head = temp
            else:
                temp.set_next(current)
                previous.set_next(temp)
            
                
                    
            
            
            
            
            
            
            
            
            