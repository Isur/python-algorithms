"""
    Kolejka z priorytetem.
"""

class QueueWithPriority(object):
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        str = ""
        for elem in self.queue:
            str += f"Priority: | {elem[0]} | Value: {elem[1]} \n"
        return str

    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.append(data)
        self.sort()
    
    def dequeue(self):
        self.queue.pop()
    
    def sort(self):
        self.queue.sort()
    
queue = QueueWithPriority()
queue.enqueue((1, '1 In Queue'))
queue.enqueue((2, '21 in Queue'))
queue.enqueue((2, '22 in Queue'))
queue.enqueue((2, '23 in Queue'))
queue.enqueue((2, '24 in Queue'))
queue.enqueue((6, '3 in Queue'))
queue.enqueue((5, '4 in Queue'))
queue.enqueue((3, '5 in Queue'))
queue.enqueue((4, '6 in Queue'))
print(queue)
queue.dequeue()
print(queue)