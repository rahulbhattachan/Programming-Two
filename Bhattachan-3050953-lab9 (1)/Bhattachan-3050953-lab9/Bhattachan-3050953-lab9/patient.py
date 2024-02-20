'''
Rahul Bhattachan
KU ID: 3050953
Purpose: This files purpose is to intitalize a pateint class that will be used in the executive class
Lab #9
Last Modified:11/29/22
'''
class Patient:

    def __init__(self, firstname, lastname, age, illness, severity):
        self.firstname = firstname
        self.lastname = lastname
        self.age = int(age)
        self.illness = illness
        self.severity = int(severity)

    def __lt__(self, other):
        if self.severity == other.severity:
            return self.age < other.age
        else: 
            return self.severity < other.severity

    def __gt__(self, other):
        if self.severity == other.severity:
            return self.age > other.age
        else: 
            return self.severity > other.severity
     