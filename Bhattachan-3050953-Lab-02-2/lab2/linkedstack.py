'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/13/22
Lab: lab 2
Last modified: 9/20/22
Purpose: The purpose of the stack class is create a stack in which items
         can be added, removed, and checked to see if it is empty.
       
'''
from node import Node
 
 
class LinkedStack:
    #initializes the class attribute
    def __init__(self):
        self.top = None
    # adds an entry and pushes all the entires in the stack
    def push(self, entry):
        pushed = Node(entry)
        if self.top != None:
            pushed.next = self.top
            self.top = pushed
        else:
            self.top = pushed
    # checks if the current stack is emptry
    def is_empty(self):
        return (self.top == None)
    # removes the entry at the top of the stack
    def pop(self):
        if self.is_empty():
            raise RuntimeError("Nothing in the stack")
        removed = self.top.entry
        self.top = self.top.next
        return removed
    # returns the entry at the top of the stack
    def peek(self):
        if self.is_empty():
            raise RuntimeError("Nothing in the stack")
        return self.top.entry


