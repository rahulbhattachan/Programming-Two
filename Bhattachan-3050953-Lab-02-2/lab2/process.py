'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/13/22
Lab: lab 2
Last modified: 9/20/22
Purpose: The purpose of the process class is to contain a call stack and manage it by making additional calls, removing calls from the call stack, and haveing the function class and the LinkedStack classes raise exceptions.
       
'''
       

from linkedstack import LinkedStack
from function import Function
 
 
class Process:
    # initializes the class attributes
    def __init__(self, name):
        self.name = name
        self.calls = LinkedStack()
        self.calls.push(Function('main', 'no'))
    # Returns the priority process
    def top(self):
        return self.calls.peek()
    # Pushes the stack
    def call(self, function):
        self.calls.push(function)
        print(f"{self.name} calls {function.get_name()}")
    # deletes the finished process
    def tick(self):
        self.calls.pop()
    # returns the name of the process
    def get_name(self):
        return self.name
