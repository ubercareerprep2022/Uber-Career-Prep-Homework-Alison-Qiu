"""Searching Exercise 10: Valid Words
Given a dictionary and a character array, print all valid words that are possible using characters from the array.
Input :    Dict: {"go","bat","me","eat","goal", "boy", "run"}
     arr[]: {'e','o','b', 'a','m','g', 'l'}

Output : go, me, goal.
"""
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_node = False
    def __str__(self):
        string = ''
        for key,val in self.children.items():
            string += "key: {} val: {}".format(key,val)
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


def validWords(dict,arr):
     t = Trie()
     for word in dict:
          t.insert(word)
     chars = set(arr)
     def find(chars,cur_string,res):
          if len(chars)==0:
               return
          if t.search(cur_string) == True:
               res.add(cur_string)
          for char in chars:
               string = cur_string+ char
               if t.startsWith(string):
                    chars.remove(char)
                    find(chars,string,res)
                    chars.add(char)
          return res
     result = find(chars,'',set())
     return result

arr = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
dict = ["go", "bat", "me", "eat", "goal", "boy", "run"] 
print(validWords(dict,arr))
