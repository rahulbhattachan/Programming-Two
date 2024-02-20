'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/13/22
Lab: lab 2
Last modified: 9/20/22
Purpose: The purpose of driver is to use the CPU_scheduler class to create a mock CPU scheduler. It also holds the main which reads the given file  from the user and then calls specific functions from different classes which are in the CPU_scheduler.
       
'''
from CPU_scheduler import CPU_Scheduler
 
 #Asks user for a file and if the file matches, gives control to CPU_scheduler class
def main():
    start = CPU_Scheduler(input("File name: "))
 
 
if __name__ == "__main__":
    main()
