'''
Rahul Bhattachan
KU ID: 3050953
Last Modified:10/25/22
Lab 6
Purpose:Stack class
'''
from Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self,entry):
        if self.is_empty():
            self.top = Node(entry)
        else:
            self.top = self.top.next
            self.top = Node(entry)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("stack is empty")
        else:
            value = self.top
            self.top = self.top.next
            return value.entry

    def peek(self):
        if self.is_empty():
            raise RuntimeError("stack is empty")
        else:
            return self.top.entry
    def __str__(self):
        return f"{self.top}"
    def clear(self):
        self.top = None

