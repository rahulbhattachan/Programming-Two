'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/13/22
Lab: lab 2
Last modified: 9/20/22
Purpose: The purpose of the node class is to serve as a building block for the other data structure classes
       
'''
class Node:
    #Initializes the basic but versatile attibutes of this class
    def __init__(self, entry):
        self.entry = entry
        self.next = None
