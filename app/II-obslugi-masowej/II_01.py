"""
    Kolejka.
"""

class Queue:
    arr = []
    def enqueue(self, elem):
        self.arr.append(elem)
    def dequeue(self):
        if len(self.arr) > 0:
            self.arr.pop(0)
        else:
            print("queue is empty")

que = Queue()
print(que.arr)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
print(que.arr)
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
print(que.arr)