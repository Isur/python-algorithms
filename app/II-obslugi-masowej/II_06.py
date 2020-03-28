"""
    Lista cykliczna.
"""


class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"{self.value}"


class CircularList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if not self.head:
            return "Linked list is empty"
        string = ""
        current = self.head
        while current:
            string += str(current)
            current = current.next
            if current is self.head:
                break
        return string

    def insert_beginning(self, value):
        if not self.head:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.next = self.head
            return
        self.head = Node(value, self.head)
        self.tail.next = self.head

    def insert_last(self, value):
        if not self.head:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.next = self.head
            return
        new_node = Node(value, self.head)
        self.tail.next = new_node
        self.tail = new_node

    def find(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
            if current is self.tail:
                return None
        return current

    def remove(self, value):
        current = self.head
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next
            if current is self.head:
                return
        if previous is None:
            self.head = current.next
            self.tail.next = self.head
        elif current:
            if current is self.tail:
                self.tail = previous
            previous.next = current.next
            current.next = None


linked = CircularList()
print(linked)
linked.insert_beginning(1)
print(linked)
linked.insert_beginning(2)
print(linked)
linked.insert_beginning(3)
print(linked)
linked.insert_last(4)
print(linked)
linked.insert_last(5)
print(linked)
linked.insert_last(6)
print(linked)
linked.remove(1)
print(linked)
linked.remove(3)
print(linked)
linked.remove(6)
print(linked)

print(linked.find(4))
print(linked.find(8))
