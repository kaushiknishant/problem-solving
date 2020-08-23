from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]    

    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def enQueue(self,x):
        while self.s1.size() != 0:
            self.s2.push(self.s1.peek())
            self.s1.pop()

        self.s1.push(x)

        while self.s2.size() !=0:
            self.s1.push(self.s2.peek())
            self.s2.pop()
    
    def deQueue(self):
        if self.s1.is_empty():
            print('empty')

        element = self.s1.peek()
        self.s1.pop()
        return element

if __name__ == '__main__':
    q = Queue()
    q.enQueue(45)
    q.enQueue(77)
    q.enQueue(88)
    q.enQueue(99)
    print(q.deQueue())
    q.enQueue(66)
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
