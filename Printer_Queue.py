# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 13:33:16 2021

@author: -Benjamin Strope
"""
import random
class Printer:
    def __init__(self,ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None
    
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
    
    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 /self.page_rate
    

class Task:
    def __init__(self,time):
        self.time_stamp = time
        self.pages = random.randrange(1,21)
    
    def get_stamp(self):
        return self.time_stamp
    def get_pages(self):
        return self.pages
    def wait_time(self,current_time):
        return current_time - self.time_stamp
        
        