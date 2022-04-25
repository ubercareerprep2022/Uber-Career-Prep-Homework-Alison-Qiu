
class Node(object):
    def __init__ (self,data=None):
        self.data = data
        self.next_node = None
    def __str__(self):
        return str(self.data)
    def setNextNode(self,node):
        self.next_node = node
    def getNextNode(self):
        return self.next_node

class LinkedList(object):
    def __init__ (self):
        self.head = None
    def push(self, node):
        #if current list is empty
        if not self.head:
            self.head = node
        #else find it's head node
        else:
            cur = self.head
            while cur.next_node is not None:
                cur = cur.next_node
            cur.next_node = node
    def pop(self):
        cur = self.head
        while cur.next_node is not None:
            prev = cur
            cur = cur.next_node
        if cur != self.head:
            prev.next_node = None
            return cur
        else:
            print('temp is ',self.head)
            temp = Node(self.head.data)
            self.head = None
            return temp
    
    def findCurAndPrev(self,index):
        i = 0
        cur = self.head
        prev = None
        out_of_bound = False
        while i<index and cur:
            i+=1
            prev = cur
            cur = cur.next_node
            if cur == None:
                out_of_bound = True
        return out_of_bound,prev,cur
        
    def insert(self,index,node):
        out_of_bound,prev,cur = self.findCurAndPrev(index)
        #print('prev,cur',out_of_bound,prev,cur)
        if not out_of_bound:
            node.setNextNode(cur)
        if prev:
            prev.setNextNode(node)
        else:
            self.head = node

    def remove(self,index):
        out_of_bound,prev,cur = self.findCurAndPrev(index)
        if not out_of_bound:
            next = cur.next_node
            cur = None
            if prev:
                prev.setNextNode(next)
            else:
                self.head = next

    def element_at(self,index):
        return self.findCurAndPrev(index)[2]

    def size(self):
        return len(self.printList())

    def printList(self):
        cur = self.head
        lst = []
        while cur is not None:
            lst.append(cur.data)
            print('lst:',lst)
            if cur.next_node:
                cur = cur.next_node
            else:
                cur = None
            cur = self.head
        return lst

    def hasCycle(self):
        '''
        a “cycle” occurs if a given node in the Linked List references an earlier node f
        or its “next” reference.
        '''
        prev_nodes = []
        cur = self.head
        while cur:
            if cur.data in prev_nodes:
                return True
            prev_nodes.append(cur.data)
            cur = cur.next_node
        return False

    def isPalindrome(self):
        #print('isPalindrome')
        lst = self.printList()
        l = 0
        r = len(lst)-1
        while r>=l:
            if lst[l] != lst[r]:
                return False
            l+=1
            r-=1
        return True

llist = LinkedList()
 


a = Node('8')
llist.push(Node('cycle'))
llist.push(Node('lol'))
llist.push(Node('3'))
llist.push(Node('7'))
print(llist.printList())
llist.pop()
print(llist.printList())
llist.push(Node('lol'))
print(llist.printList())
print('insert 8')
llist.insert(2,a)
print(llist.printList())
print('remove element')
llist.remove(3)
print(llist.printList())
print('element at ')
print(llist.element_at(4))
print(llist.size())
print('has cycle: ', llist.hasCycle())
print(llist.printList())
print('has cycle: ', llist.hasCycle())
llist.insert(3,a)
#print(llist.printList())
#print(llist.isPalindrome())


