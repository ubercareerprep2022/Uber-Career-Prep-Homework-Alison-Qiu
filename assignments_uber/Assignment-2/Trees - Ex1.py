class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [Trees - Ex1] Exercise: Printing a tree
# Implement a method called print() to print the values of the data in all the TreeNodes in a Tree above. For example, running print() on the Tree above should produce one of the three values below:

# 1 7 17 6 3
# 7 1 6 17 3
# 7 6 3 17 1 


def print_tree (root):
    if root == None:
        return None
    else:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)



e = TreeNode(3)
d = TreeNode(6)
c = TreeNode(17,d,e)
b = TreeNode(7)
a = TreeNode(1,b,c)

print_tree(a)

# k = TreeNode('Sales Intern')
# j = TreeNode('engineer')
# i
# h = TreeNode('engineer')
# g = TreeNode('engineer')
# f = TreeNode('engineer')
# e = TreeNode(3)
# d = TreeNode(6)
# c = TreeNode(17,d,e)
# b = TreeNode(7)
# a = TreeNode(1,b,c)

def  printLevelByLevel(root):
    queue = [root]
    while queue != None:
        cur = queue.dequeue()
        print(cur)
        queue.extend([employee for employee in cur.directReports])

