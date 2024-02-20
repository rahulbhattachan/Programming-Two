'''
Rahul Bhattachan
KU ID: 3050953
Last Modified:10/25/22
Lab 6
Purpose:Node class
'''

class Node:
    def __init__(self,entry):
        self.entry = entry
        self.next = None
    def __repr__(self):
        return f"{self.entry}"