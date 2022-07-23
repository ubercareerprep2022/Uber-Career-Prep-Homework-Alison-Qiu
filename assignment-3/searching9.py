"""
Searching Exercise 9: Prefix Length
Given an array of strings arr[] and given some queries where each query consists of a string str and an integer k. 
The task is to find the count of strings in arr[] whose prefix of length k matches with the k length prefix of str.
Input: arr[] = {"abba", "abbb", "abbc", "abbd", "abaa", "abca"}, 
     str   = "abbg", 
     k     = 3
Output: 4
"""
from collections import defaultdict
import string

class TrieNode:
     def __init__(self):
          self.children = defaultdict(TrieNode)
          self.end_node = False
     def __str__(self):
          string = "cur node's children:\n"
          for key,val in self.children.items():
               string += "key: {} val: {}".format(key,val)
               string += "-----"
          return string


        
class Trie:

     def __init__(self):
          self.root = TrieNode()

     def insert(self, word: str) -> None:
          root = self.root
          for letter in word:
               prev = root
               root = root.children[letter]
          prev.end_node = True
          

     def search(self, word: str) -> bool:
          if not word:
               return None
          root = self.root
          for letter in word:
               if letter in root.children:
                    prev = root
                    root = root.children[letter]
               else:
                    return False
          return prev.end_node
                    

     def startsWith(self, prefix: str) -> bool:
        root = self.root
        for letter in prefix:
            #print(letter)
            if root.children and letter in root.children:
                #print(type(root.children[letter]))
                root = root.children[letter]
            else:
                return False
        return True
     def prefixLength1(self, s, k):
         
        _in = 0
        count = 0
        cur = self.root
 
        # Traverse the string
        for i in range(len(s)):
            _in = ord(s[i]) - ord('a')
 
            # If there is no node then return 0
            if cur.children[_in] == None:
                return 0
 
            # Else traverse to the required node
            cur = cur.children[_in]
 
            count += 1
 
            # Return the required count
            if count == k:
                return cur.freq
        return 0
     def prefixLength(self,prefix):
          #find how many words in trie has the prefix
          
          root = self.root
          for letter in prefix:
               if root.children and letter in root.children:
                    root = root.children[letter]
               else:
                    return 0
          self.count = 1 if root.end_node else 0
          def dfs(node):
               if not node.children:
                    self.count += 1
                    return
               else:
                    for child in node.children:
                         c = node.children[child]
                         dfs(c)
          dfs(root)
          return self.count


arr1 = ["abba", "abbb", "abbc", "abbd", "abaa",'abbag', 'abbaf',"abca"] #6
arr2 = ["abb","abbc","abca"] #2
arr3 = ['geeks', 'geeksforgeeks', 'forgeeks'] #2
strg = "abbg"
k  = 3
str = 'geeks'
m = 2 #2


def find(arr,strg,k):
     t = Trie()
     for word in arr:
          t.insert(word)
     prefix = strg[:k]
     return t.prefixLength(prefix)
     r#eturn t.prefixLength1(strg,k)

print(find(arr1,strg,k))
print(find(arr2,strg,k))
print(find(arr3,str,m))
