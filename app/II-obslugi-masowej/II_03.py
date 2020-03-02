"""
    Stos.
"""

class Stack(object):
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        str = ""
        for elem in self.stack:
            str += f"{elem}\n"
        return str
    
    def put(self, item):
        self.stack.append(item)
    
    def take(self):
        self.stack.pop()
    
stack = Stack()
for i in range(0,10):
    stack.put(i)
print(stack)
stack.take()
print(stack)