'''
Rahul Bhattachan
KU ID: 3050953
Lab 6
Last Modified: 10/25/22
Purpose: Contains the main chunk of code that will be called by the driver.
'''

import time

from Node import Node
from Stack import Stack
from Queue import Queue
from LinkedList import LinkedList


def nanosec_to_sec(ns): # Converts nanoseconds to seconds
    BILLION = 1000000000
    return ns/BILLION

class Executive:

    def __init__(self): # Initializes class attributes
        self.stack = Stack()
        self.queue = Queue()
        self.linklist = LinkedList()
    
    def main(self): # Contains the items that have to be timed
        self.pop_item()
        self.pop_all()
        self.enqueueing()
        self.get_index_one()
        self.get_last_index()
        self.print_list()

    def pop_item(self): # Times how long it takes to pop an item of a stack
        num = 0
        print("Beginning the timing code...")
        results = open("pop_one_results.txt", "w")
        for _ in range(100):
            num += 1000
            self.stack.clear()
            for _ in range(num):
                self.stack.push(_)
            start_time = time.process_time_ns()
            self.stack.pop()
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time}\n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def pop_all(self): # Times how long it takes to pop all items of a stack
        results = open("pop_results.txt","w")
        num = 0
        print("Beginning the timing code...")
        for _ in range(100):
            num += 1000
            self.stack.clear()
            for _ in range(num):
                self.stack.push(_)

            start_time = time.process_time_ns()
            while self.stack.top != None:
                self.stack.pop()
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def enqueueing(self): # Times how long it takes to enqueue items to a stack
        print("Beginning the timing code...")
        num = 0
        results = open("enqueue_results.txt", "w")
        for _ in range(100):
            num += 1000
            self.queue.clear()
            start_time = time.process_time_ns()
            for _ in range(num):
                self.queue.enqueue(_)
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def get_index_one(self): # Times how long it takes to get the first index of a list
        print("Beginning the timing code...")
        num = 0
        results = open("get_index_one.txt", "w")
        for _ in range(100):
            num += 1000
            self.linklist.clear()
            start_time = time.process_time_ns()
            for i in range(num):
                self.linklist.insert(0,Node(i))
            self.linklist.get_entry(0)
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def get_last_index(self): # Times how long it takes to get the last index of a list
        print("Beginning the timing code...")
        num = 0
        results = open("get_last_index.txt", "w")
        for _ in range(100):
            num += 1000
            self.linklist.clear()
            start_time = time.process_time_ns()
            for i in range(num):
                self.linklist.insert(0, Node(i))
            self.linklist.get_entry(self.linklist._length-1)
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def print_list(self): # Times how long it takes print all items in a list
        print("Beginning the timing code...")
        num = 0
        results = open("full_list_result.txt", "w")
        for _ in range(100):
            num += 1000
            self.linklist.clear()
            start_time = time.process_time_ns()
            for i in range(num):
                self.linklist.insert(0, Node(i))
            for node in range(self.linklist._length):
                print(self.linklist.get_entry(node))
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()