#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


class Stack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        if self.min != None:
            self.min = min(self.min, val)
        else:
            self.min = val

    def pop(self) -> None:
        if self.stack:
            (val, prior_min) = self.stack.pop()
            self.min = prior_min
            return val
        
        return False
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        
        return False

    def getMin(self) -> int:
        if self.stack:
            return self.min
        
        return False
  
