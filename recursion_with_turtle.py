# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:02:12 2021

@author: - Benjamin Strope
Stack Frames: Turtle!!!!
"""

import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)
        
#draw_spiral(my_turtle, 100)
#my_win.exitonclick()

import random
def tree(branch_len, t):
    if branch_len > 5:
        t.pensize(branch_len // 10)
        t.forward(branch_len)
        t.right(random.randrange(15,45))
        tree(branch_len - random.randrange(5,20),t)
        t.left(random.randrange(15,45) * 2)
        tree(branch_len - random.randrange(5,20),t)
        t.right(random.randrange(15,45))
        t.backward(branch_len)
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75,t)
    my_win.exitonclick()
main()