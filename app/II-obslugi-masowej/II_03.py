"""
    Stos.
"""

class Stack(object):
    def __init__(self, max = 10):
        self.arr = []
        self.max_len = max
        self.curr_len = 0

    def __str__(self):
        if self.isEmpty():
            return "Stack is empty"
        return ", ".join(map(str, self.arr))

    def isEmpty(self):
        return self.arr == []

    def isFull(self):
        return self.curr_len == self.max_len
    
    def push(self, item):
        if self.isFull():
            return
        new_len = self.curr_len + 1
        new_arr = [0] * new_len
        for i in range(self.curr_len):
            new_arr[i] = self.arr[i]
        new_arr[self.curr_len] = item
        self.arr = new_arr
        self.curr_len = new_len
    
    def pop(self):
        if self.isEmpty():
            return
        new_len = self.curr_len - 1
        new_arr = [0] * new_len
        for i in range(new_len):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.curr_len = new_len

s = Stack(3)
print(s)
s.pop()
print(s)
s.push(1)
print(s)
s.push(2)
print(s)
s.push(3)
print(s)
s.push(4)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
