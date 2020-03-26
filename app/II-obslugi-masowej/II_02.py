"""
    Kolejka z priorytetem.
"""

class QueueWithPriority(object):
    arr = []
    priority = []
    curr_len = 0

    def __init__(self, max=10):
        self.max_len = max

    def __str__(self):
        s = "Current queue state: \n"
        if self.isEmpty():
            s += "Queue is empty\n"
            return s
        for i in range(self.curr_len):
            s += f"{self.arr[i]} with priority {self.priority[i]}\n"
        return s

    def isEmpty(self):
        return self.arr == []

    def isFull(self):
        return self.curr_len == self.max_len

    def enqueue(self, item, priority):
        if self.isFull():
            return
        if self.isEmpty():
            self.curr_len = 1
            self.arr = [item]
            self.priority = [priority]
        else:
            pos = self.find_pos(priority)
            self.insert_into(item, priority, pos)

    def dequeue(self):
        if self.isEmpty():
            return
        new_len = self.curr_len - 1
        new_arr = [0] * new_len
        for i in range(new_len):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.curr_len = new_len

    def find_pos(self, priority):
        for i in range(self.curr_len):
            if(self.priority[i] >= priority):
                return i
        return self.curr_len

    def insert_into(self, item, priority, pos):
        new_len = self.curr_len + 1
        new_arr = [None] * new_len
        new_priority = [None] * new_len
        i = 0
        for i in range(new_len):
            if i < pos:
                new_arr[i] = self.arr[i]
                new_priority[i] = self.priority[i]
            elif i == pos:
                new_arr[pos] = item
                new_priority[pos] = priority
            else:
                new_arr[i] = self.arr[i - 1]
                new_priority[i] = self.priority[i - 1]  

        self.priority = new_priority
        self.arr = new_arr
        self.curr_len = new_len
        
q = QueueWithPriority()
print(q)
q.enqueue("T", 1)
q.enqueue("T", 2)
q.enqueue("T", 3)
q.enqueue("T", 4)
q.enqueue("T", 5)
q.enqueue("T", 4)
q.enqueue("T", 3)
q.enqueue("T", 2)
q.enqueue("T", 1)
q.enqueue("D",1)
print(q)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q)