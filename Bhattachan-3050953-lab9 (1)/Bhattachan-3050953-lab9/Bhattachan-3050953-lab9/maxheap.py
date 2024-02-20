'''
Rahul Bhattachan
KU ID: 3050953
Purpose: This files purpose is to build a Maxheap that will be called upon in the executive file
Lab #9
Last Modified:11/29/22
'''


class MaxHeap:

    def __init__(self):
        self.heap = []
    
    def length(self):
        return len(self.heap)

    def add(self,entry):
        self.heap.append(entry)
        self.upheap(len(self.heap)-1)

    def next(self):
        if len(self.heap) > 0: return self.heap[0]
        else: return None

    def upheap(self, index):
        if index == 0:
            return
        if self.heap[index] > self.heap[(index-1)//2]:
            var = self.heap[index]
            self.heap[index] = self.heap[(index-1)//2]
            self.heap[(index-1)//2] = var
            self.upheap((index-1)//2)

    def left_child(self, index):
        return (2*index)+1

    def right_child(self, index):
        return (2*index)+2

    def swap(self,index1, index2):
        var = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = var

    def children(self, index):
        if self.right_child(index) < len(self.heap):
            return 2
        elif self.left_child(index) < len(self.heap):
            return 1
        else: 
            return 0 

    def end(self):
        return len(self.heap) - 1

    def remove(self):
        self.swap(0, -1)
        self.heap.pop(-1)
        self.downheap(0)


    def downheap(self, index):
        if self.children(index) == 0:
            return
        if self.children(index) == 1:
            if self.heap[self.left_child(index)] > self.heap[index]:
                self.swap(index, self.left_child(index))
                self.downheap(self.left_child(index))
        else:
            minimum = min(self.heap[self.left_child(index)], self.heap[self.right_child(index)])
            if self.heap[index] < minimum:
                if self.heap[self.left_child(index)] > self.heap[self.right_child(index)]:
                    self.swap(index, self.left_child(index))
                    self.downheap(self.left_child(index))
            else:
                self.swap(index, self.right_child(index))
                self.downheap(self.right_child(index))