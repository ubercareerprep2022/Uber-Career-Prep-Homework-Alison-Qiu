'''Implement reverseLinkedList() which takes in a linked list and returns
 a new linked list with the same elements in reverse order. For example, if 
 the representation of your Linked List is “1, 2, 3, 4”, then reversing it 
 would return “4, 3, 2, 1”.
'''
from Part4 import Node,LinkedList

#iterative

# 1 --> 2 --> 3 --> 4 --> 5 --> None
# 5 --> 4 --> 3 --> 2 --> 1 --> None
# 2 -->1 --> None
def reverseLinkedList(lst):
    cur = lst.head
    #1
    prev = None
    #2
    print(cur)
    while cur:
        temp = cur.next_node
        prev,cur.next_node = cur.next_node,prev
        cur=temp


        
    
#Leaning on our knowledge of stacks, can you think of a way to utilize a stack to solve this problem with a time complexity of O(n)?
#Recursively



l = LinkedList()
l.push(Node('1'))
l.push(Node('2'))
l.push(Node('3'))
l.push(Node('4'))
l.push(Node('5'))
print(l.printList())
l= reverseLinkedList(l)
#print(l.printList())