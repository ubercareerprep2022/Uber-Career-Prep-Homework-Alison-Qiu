class Stack:
    """
    A simple implementation of a LIFO stack.
    """
    def __init__(self):
        """
        Initialize the stack.
        """
        self._stack = []

    def size(self):
        """
        Returns an integer value with the count of elements in the stack
        """
        return len(self._stack)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        strg = ""
        for item in self._stack:
            strg += str(item)
        return strg

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
       
        self._stack.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        if not self.isEmpty():
            return self._stack.pop()
        else:
            print ("can't pop because stack is empty")

    def top(self):
        """
        Looks at the top value, and returns it. Does not manipulate the stack.
        """
        if not self.isEmpty():
            return self._stack[len(self._stack)-1]
        else:
            print ("no top value because stack is empty")

    def isEmpty(self):
        """
        Returns True or False if the stack is Empty or not, respectively.
        """
        if self._stack:
            return True
        else:
            return False

myStack = Stack()
myStack.push(42)
print ('Top of stack:', myStack.top())
# prints “Top of stack: 42”
print ('Size of stack:', myStack.size())
# prints “Size of stack: 1”
popped_value = myStack.pop()
print ('Popped value:', popped_value)
popped_value = myStack.pop()
# prints “Popped value: 42”
print ('Size of stack:', myStack.size())
# prints “Size of stack: 0”


class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    def __init__(self):
        """
        Initialize the queue.
        """
        self._queue = []

    def __str__(self):
        strg = ""
        for item in self._queue:
            strg += str(item)
        return strg

    def enqueue(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
       
        self._queue.append(item)

    def dequeue(self):
        """
        removes an item from the queue
        """
        return self._queue.pop(0)

    def rear(self):
        """
        returns the item at the end of the queue
        """
        return self._queue[len(self._queue)-1]
        

    def front(self):
        """
        returns the item at the end of the queue
        """
        return self._queue[0]
    
    def size(self):
        """
        returns the size of the queue
        """
        return len(self._queue)
    
    def isEmpty(self):
        """
        returns whether or not the queue is empty
        """
        if self._queue:
            return True
        else:
            return False

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print ('Size of queue: ', myQueue.size())
# prints “Size of queue: 3”
