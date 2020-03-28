"""
    Lista dwukierunkowa.
"""

class Node(object):
    def __init__(self, value, next_node, prev_node):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return f"{self.value}"

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.head:
            return "Linked list is empty"
        string = ""
        current = self.head
        while current:
            string += str(current)
            current = current.next
        return string
    
    def insert_beginning(self, value):
        new_head = Node(value, self.head, None)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def insert_last(self, value):
        if not self.head:
            self.head = Node(value, None, self.head)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value, None, current)

    def find(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        return current
    
    def remove(self, value):
        node = self.find(value)
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None

linked = DoublyLinkedList()
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
linked.remove(3)
print(linked)
linked.remove(4)
print(linked)
linked.remove(6)
print(linked)
print("Search:")
print(linked.find(3))
print(linked.find(2))