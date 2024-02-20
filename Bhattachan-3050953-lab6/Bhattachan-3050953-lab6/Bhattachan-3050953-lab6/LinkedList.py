'''
Rahul Bhattachan
KU ID: 3050953
Last Modified:10/25/22
Lab 6
Purpose:Linked list class
'''
class LinkedList:

    def __init__(self):
        self._front = None
        self._length = 0

    def printlist(self):
        jumper = self._front
        print(f"printing list...")
        print(f"length: {self._length}")
        if jumper != None:
            while jumper != None:
                print(jumper.entry)
                if jumper.next != None:
                    print(f"my next is {jumper.next.entry}\n")
                else:
                    print("i have no next")
                jumper = jumper.next
        else:
            print("the list is empty")
            
    def reverse(self):
        b = None
        temp = self._front
        while temp != None:
            a = temp.next
            temp.next = b
            b = temp
            temp = a
        self._front = b

    def length(self):
        return self._length

    def insert(self,index,entry):
        if 0 <= index <= self._length:
            if index == 0:
                entry.next = self._front
                self._front = entry
            elif index < (self._length) and index > 0:
                temp = self._front
                for node in range(index-1):
                    temp = temp.next
                entry.next = temp.next
                temp.next = entry

            elif index == self._length:
                temp = self._front
                for web in range(index):
                    b = temp
                    temp = temp.next
                b.next = entry
                entry.next = temp
            self._length += 1
        else:
            raise RuntimeError("invaid index")

    def get_entry(self,index):
        temp = self._front
        if 0 <= index <= (self._length):
            for nodes in range(index):
                temp = temp.next
            return temp.entry
        else:
            raise RuntimeError('invaid index')

    def clear(self):
        self._front = None
        self._length = 0

    def remove(self,index):
        temp = self._front
        if index == 0:
            temp = self._front
            self._front = self._front.next
            self._length -= 1
            return temp.entry
        elif 0 < index <= (self._length - 1):
            for node in range(index-1):
                temp = temp.next
            temp2 = temp.next
            temp.next = temp.next.next
            self._length -= 1
            return temp2.entry
        elif self._length == 0:
            raise RuntimeError("list is empty")
        else:
            raise RuntimeError("invaid input")

    def set_entry(self,index,entry):
        temp = self._front
        if index == 0:
            self._front = entry
            self._length += 1
        elif 0 < index <= (self._length-1):
            for node in range(index):
                temp = temp.next
            temp.entry = entry
        else:
            raise RuntimeError("invaid index")
