# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:47:26 2021

@author: -Benjamin Strope
"""
from stack import Stack

def infix_to_postfix(infix_expression):
    
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expression.split()
    operator = '*+-/)(^'
    for token in token_list:
        if token not in operator:
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.empty()) and \
                (prec[op_stack.peek()] >= prec[token]):
                    postfix_list.append(op_stack.pop())
            op_stack.push(token)
    
    while op_stack.empty() == False:
        postfix_list.append(op_stack.pop())
    
    return ''.join(postfix_list)

def postfix_eval(postfix_expression):
    eval_stack = Stack()
    
    token_list = postfix_expression.split()
    for token in token_list:
        if token in '0123456789':
            eval_stack.push(int(token))
        else:
            operand2 = eval_stack.pop()
            operand1 = eval_stack.pop()
            result = do_math(token,operand1,operand2)
            eval_stack.push(result)
    return eval_stack.pop()

def do_math(token,operand1,operand2):
    if token == '*':
       result = operand1 * operand2
    elif token == '+':
        result = operand1 + operand2
    elif token == '-':
        result = operand1 - operand2
    elif token == '^':
        result = operand1 ** operand2
    else:
        result = operand1 / operand2
    return result

    