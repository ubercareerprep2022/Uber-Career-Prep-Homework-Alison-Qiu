"""Add-and-Search Words
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ‘.’. A ‘.’ means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") ⇒ false
search("bad") ⇒ true
search(".ad") ⇒ true
search("b..") ⇒ true
Note: You may assume that all words consist of lowercase letters a-z.
"""
from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end_node = False
    def __str__(self):
        string = ''
        string += str(self.end_node)
        for key,val in self.children.items():
            string += "key: {}".format(key)
        return string
    
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for letter in word:
            prev = root
            root = root.children[letter]
        root.end_node = True
            

    def search(self, word: str) -> bool:
        
        def dfs(word,root):
            print("word is {} and root is {}".format(word,root))

            # print("word[0] is {} and root is {}".format(word[0],root))
            # print('')
            if word =='':
                if root.end_node == True:
                    print("root.end_node == True")
                    return True
                return False

            if word[0] == ".":
                for child in root.children:
                    #print("child",child)
                    if dfs(word[1:],root.children[child]) == True:
                        return True
            if  (word[0] not in root.children):
                return False
            return dfs(word[1:],root.children[word[0]])        
                
        
        return dfs(word,self.root)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# print(wordDictionary.search("mad")) 
# print(wordDictionary.search("pad")) 
# print(wordDictionary.search("bad")) 
# print(wordDictionary.search(".ad"))
# print(wordDictionary.search("b.."))

["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"]
[[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]]
#[true,true,true,false,true,false,true,true]

# wordDictionary.addWord("a");
# wordDictionary.addWord("ab");
# print(wordDictionary.search("a"))  #t
# print(wordDictionary.search("a.")) 
# print(wordDictionary.search("ab")) 
# print(wordDictionary.search(".a")) 
# print(wordDictionary.search(".b"))
# print(wordDictionary.search("ab."))
# print(wordDictionary.search(".")) #t
# print(wordDictionary.search("..")) 
# #tttftftt

# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

wordDictionary.addWord("at");
wordDictionary.addWord("and");
wordDictionary.addWord("an");
wordDictionary.addWord("add");
print(wordDictionary.search("a")) #f
print(wordDictionary.search(".at")) 
wordDictionary.addWord("bat");
print(wordDictionary.search(".at")) 
print(wordDictionary.search("an."))
print(wordDictionary.search("a.d."))
print(wordDictionary.search("b.")) 
print(wordDictionary.search("a.d"))
print(wordDictionary.search(".")) 