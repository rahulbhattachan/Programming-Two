'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/13/22
Lab:lab 2
Last modified:9/20/22
Purpose: CPU_Scheduler is a class that is designed to act as the main executive class. It imports other classes such as process and linked queue to create a mock CPU scheduler. It will also take in the file provided from the user and then run it through the replicated CPU scheduler. 
       
'''
from process import Process
from linkedqueue import LinkedQueue
from function import Function
 
 
class CPU_Scheduler():

    #Initializes the class' attributes
    def __init__(self, file):
        self.processes = LinkedQueue()
        self.parse(file)
    #Contains the main chunk of code that is called by main
    def parse(self, file):
        text = open(file, 'r')
        for line in text:
            check = ""
            store = ""
            for keyword in line.split():
 
                if store != "":
                    copy = self.processes.peek_front()
                    self.processes.peek_front().call(Function(store, keyword))
                    self.processes.dequeue()
                    self.processes.enqueue(copy)
                    store = ""
 
                if check != "START" and check != "CALL" and check != "RETURN" and check != "RAISE":
                    check = keyword
                elif check == "START":
                    self.processes.enqueue(Process(keyword))
                    print(f"{keyword} added to queue")
                elif check == "CALL":
                    store = keyword
 
                if keyword == "RETURN":
                    print(
                        f"{self.processes.peek_front().get_name()} returns from {self.processes.peek_front().top().get_name()}")
                    if self.processes.peek_front().top().get_name() == "main":
                        print(
                            f"{self.processes.peek_front().get_name()} process has ended")
                        self.processes.dequeue()
                    else:
                        copy = self.processes.peek_front()
                        self.processes.dequeue()
                        self.processes.enqueue(copy)
                elif keyword == "RAISE":
                    process = self.processes.peek_front().get_name()
                    error = False
                    if self.processes.peek_front().top().get_exception() == "yes":
                        print(
                            f"{self.processes.peek_front().get_name()} has exception handled by: {self.processes.peek_front().top().get_name()}")
                    else:
                        try:
                            while self.processes.peek_front().top().get_exception() == "no":
                                if error == False:
                                    print(
                                        f"{self.processes.peek_front().get_name()} encountered a raised exception by: {self.processes.peek_front().top().get_name()}")
                                error = True
                                print(
                                    f"{self.processes.peek_front().get_name()} ends {self.processes.peek_front().top().get_name()} due to an unhandled exception")
                                self.processes.peek_front().tick()
                        except:
                            print(f"{process} process has ended")
                            break
                        if self.processes.peek_front().top().get_exception() == "yes":
                            print(
                                f"{self.processes.peek_front().get_name()} has exception handled by: {self.processes.peek_front().top().get_name()}")
 

