'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/13/22
Lab: lab 2
Last modified: 9/20/22
Purpose: The purpose of the Function class is to return process names and raise exceptions
       
'''
class Function:
    # initializes the attributes of this class
    def __init__(self, name, exception):
        self.name = name
        self.exception = exception
    # returns name of process
    def get_name(self):
        return self.name
    # returns exception
    def get_exception(self):
        return self.exception
