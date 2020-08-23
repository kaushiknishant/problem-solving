from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

if __name__ == '__main__':
    s = Stack()
    string = 'We will conquere COVID-19'
    for st in string:
        s.push(st)
    while s.size() > 0:
        print(s.peek())
        s.pop()
    

