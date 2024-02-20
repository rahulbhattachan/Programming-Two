'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/13/22
Lab: lab 2
Last modified: 9/20/22
Purpose: The purpose of the queue class is to add items to the back of the queue remove items from the front of the queue, return items in the front of the queue, and check to see if the queue is empty or not.
       
'''
from node import Node
 
 
class LinkedQueue:
    # Intializes the attributes of this class
    def __init__(self):
        self.front = None
        self.back = None
    # checks if queue is empty
    def is_empty(self):
        return (self.front == None and self.back == None)
    # Adds item to the back of the queue
    def enqueue(self, entry):
        var = Node(entry)
        if not self.is_empty():
            self.back.next = var
            self.back = var
        else:
            self.front = var
            self.back = var
    # Removes item from the front of the queue. Returns the item
    def dequeue(self):
        if not self.is_empty():
            if self.front == self.back:
                var = self.front
                self.front == None
                self.back == None
                return var.entry
            else:
                var = self.front
                self.front = self.front.next
                return var.entry
        else:
            raise RuntimeError("Nothing in the queue")
     # returns item in the front of the queue
    def peek_front(self):
        if self.front != None and self.back != None:
            return self.front.entry
        else:
            raise RuntimeError("Nothing in the queue")
