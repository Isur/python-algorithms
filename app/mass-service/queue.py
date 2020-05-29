"""
    Kolejka.
"""


class Queue(object):
    arr = []
    curr_len = 0

    def __init__(self, max=10):
        self.max_len = max

    def __str__(self):
        if self.isEmpty():
            return "Queue is empty"
        return ", ".join(map(str, self.arr))

    def isEmpty(self):
        return self.arr == []

    def isFull(self):
        return self.curr_len == self.max_len

    def enqueue(self, item):
        if self.isFull():
            return
        new_len = self.curr_len + 1
        new_arr = [0] * (new_len)
        new_arr[0] = item
        for i in range(self.curr_len):
            new_arr[i + 1] = self.arr[i]
        self.arr = new_arr
        self.curr_len = new_len

    def dequeue(self):
        if self.isEmpty():
            return
        new_len = self.curr_len - 1
        new_arr = [0] * new_len
        for i in range(new_len):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.curr_len = new_len


q = Queue(3)
print(q)
q.enqueue("1")
print(q)
q.enqueue("2")
print(q)
q.enqueue("3")
print(q)
q.enqueue("4")
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
