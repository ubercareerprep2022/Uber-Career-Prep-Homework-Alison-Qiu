##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node 
class Node:

# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
      self.root = None

  def find_largest_smaller_key(self, num):
    node = self.root
    cur_max = float('-inf')
    while node:
      if node.key > num:
        node = node.left
      else:
        cur_max = node.key
        node = node.right
    return cur_max


  def insert(self, key):

      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

  ######################################### 
  # Driver program to test above function #
  #########################################

bst  = BinarySearchTree()

# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

result = bst.find_largest_smaller_key(17)

print ("Largest smaller number is %d " %(result))

bst2 = BinarySearchTree()

# Create the tree given in the above diagram 
bst2.insert(5)
bst2.insert(2);
bst2.insert(12);
bst2.insert(1);
bst2.insert(3);
bst2.insert(9);  
bst2.insert(21);    
bst2.insert(19);    
bst2.insert(25)

result = bst2.find_largest_smaller_key(24)
result2 = bst2.find_largest_smaller_key(3)

print ("Largest smaller number is %d and %d" %(result,result2))

