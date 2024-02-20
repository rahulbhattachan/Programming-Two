'''
Rahul Bhattachan
KU ID: 3050953
Purpose: Main chunk of code that will be run on the driver file
Lab #9
Last Modified:11/29/22
'''

from patient import Patient
from maxheap import MaxHeap

class Executive:

    def __init__(self, filename):      
        self.heap = MaxHeap()

        file = open(filename, "r")
        my_list = []

        for line in file:
            my_list.append(line.split())

        for stuff in my_list:
            if stuff[0] == "ARRIVE":
                p = Patient(stuff[1],stuff[2],stuff[3],stuff[4],stuff[5])
                self.heap.add(p)
            elif stuff[0] == "NEXT":
                next_patient = self.heap.next()
                if next_patient != None:
                    print("Next patient:")
                    print("   Name:", next_patient.firstname, next_patient.lastname)
                    print("   Age:", next_patient.age)
                    print("   Suffers from:", next_patient.illness)
                    print("   Illness severity:", next_patient.severity)
                else:
                    print("Nobody is next in line.")
            elif stuff[0] == "TREAT":
                if self.heap.length() == 0:
                    print("Nobody is there to treat.")
                else:
                    self.heap.remove()
            elif stuff[0] == "COUNT":
                if (self.heap.length()) > 0:
                    print("There are", self.heap.length(), "patients waiting.")
                elif (self.heap.length()) == 0:
                    print("Nobody is waiting.")