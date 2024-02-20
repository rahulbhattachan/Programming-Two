'''
Rahul Bhattachan
KU ID: 3050953
Purpose: Binary Search Tree Node 
Lab #7
Last Modified:10/31/22
'''
class BSTNode:

    def __init__(self, val = None, data = None):#initializes values
        self.left = None
        self.right = None
        self.val = val
        self.data = data

    def insert (self, val, data):#adds value to pokedex
        if not self.val:
            self.val = val
            self.data = data
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val, data)
                return
            self.left = BSTNode(val, data)
            return
        if self.right:
            self.right.insert(val, data)
            return
        self.right = BSTNode(val, data)

    def exists(self, val):#checks if value is in pokedex
        if val == self.val:
            ret = str(self.val) + ', English: ' + self.data.val1 + ', Japanese: ' + self.data.val2
            return ret
        if val < self.val:
            if self.left == None:
                ret = "No entry found"
                return ret
            return self.left.exists(val)
        if self.right == None:
            ret = "No entry found"
            return ret
        return self.right.exists(val)

    def doExists(self, val):#returns value if its in the pokedex
        if val == self.val:
            return True
        if val < self.val:
            if self.left == None:
                return False
            return self.left.doExists(val)
        if self.right == None:
            return False
        return self.right.doExists(val)

    def inorder(self, val):#returns pokedex in order
        if self.left is not None:
            self.left.inorder(val)
        if self.val is not None:
            val.append(str(self.val) + ', English: ' + self.data.val1 + ', Japanese: ' + self.data.val2)
        if self.right is not None:
            self.right.inorder(val)
        return val

    def preorder(self, val):#returns pokedex in preorder
        if self.val is not None:
            val.append(str(self.val) + ', English: ' + self.data.val1 + ', Japanese: ' + self.data.val2)
        if self.left is not None:
            self.left.preorder(val)
        if self.right is not None:
            self.right.preorder(val)
        return val

    def postorder(self, val):#returns pokedex in preorder
        if self.left is not None:
            self.left.postorder(val)
        if self.right is not None:
            self.right.postorder(val)
        if self.val is not None:
            val.append(str(self.val) + ', English: ' + self.data.val1 + ', Japanese: ' + self.data.val2)
        return val