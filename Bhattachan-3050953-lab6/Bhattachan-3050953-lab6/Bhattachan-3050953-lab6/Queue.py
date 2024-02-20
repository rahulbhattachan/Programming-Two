'''
Rahul Bhattachan
KU ID: 3050953
Last Modified:10/25/22
Lab 6
Purpose:Queue class
'''
from Node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._back = None
    def is_empty(self):
        return self._front == None

    def enqueue(self,entry):
        if self.is_empty():
            self._front = Node(entry)
            self._back = self._front
        else:
            self._back.next = Node(entry)
            self._back = self._back.next
    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("queue is empty")
        else:
            value = self._front
            self._front = self._front.next
            return value.entry
    def peek_front(self):
        if self.is_empty():
            raise RuntimeError('queue is empty')
        else:
            return self._front.entry
    def clear(self):
        self._front = None
        self._back = None

