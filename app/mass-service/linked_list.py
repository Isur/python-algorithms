"""
    Lista jednokierunkowa.
"""


class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"{self.value}"


class LinkedList(object):
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
        self.head = Node(value, self.head)

    def insert_last(self, value):
        if not self.head:
            self.head = Node(value, None)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value, None)

    def find(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        return current

    def remove(self, value):
        current = self.head
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next
        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None


linked = LinkedList()
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
