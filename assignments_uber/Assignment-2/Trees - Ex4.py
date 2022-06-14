from numpy import insert


class Node:
    def __init__(self, val,left=None, right=None): #Node class for each node in tree
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'node: {} and left is {} and right is {}'.format(self.val,self.left,self.right)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self,root, key):
        """
        Inserts a key into this binary search tree.
        * If there are n nodes in the tree, then the average runtime of this method should be log(n)
        """
        if root==None:
            root = key
        elif key.val < root.val:
            if root.left == None:
                root.left = key
            self.insert(root.left,key)
        else:
            if root.right == None:
                root.right = key
            else:
                self.insert(root.right,key)

    def find(self,root,key):
        """
        * Checks whether or not a key exists in this binary search tree.
   * If there are n nodes in the tree, then the average runtime of this method should be log(n).
        """
        if root == None:
            return False
        if key.val == root.val:
            return True
        elif key.val < root.val:
            return self.find(root.left,key)
        else:
            return self.find(root.right,key)

a = Node(1)
b = Node(2)
c = Node(3)
tree  = Tree(c)
tree.insert(c,b)
#print(c)
print(tree.find(c,b))
print(tree.find(c,a))