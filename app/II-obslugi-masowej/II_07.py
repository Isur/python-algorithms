"""
    Lista z wartownikiem.
"""


class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.value}"


class SentinelLinkedList(object):
    def __init__(self):
        self.sentinel = Node(value=None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def __str__(self):
        string = ""
        node = self.sentinel.next
        while node is not self.sentinel:
            string += f"|{node.value}|"
            node = node.next
        return string

    def first_node(self):
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.next

    def insert(self, pos, value):
        new_node = Node(value)
        new_node.prev = pos
        new_node.next = pos.next
        pos.next = new_node
        new_node.next.prev = new_node

    def insert_last(self, value):
        last_node = self.sentinel.prev
        self.insert(last_node, value)

    def insert_beggining(self, value):
        self.insert(self.sentinel, value)

    def remove(self, value):
        node = self.find(value)
        if not node:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def find(self, value):
        self.sentinel.value = value

        node = self.first_node()
        while node.value != value:
            node = node.next

        self.sentinel.value = None

        if node == self.sentinel:
            return None
        else:
            return node


linked = SentinelLinkedList()
print(linked)
linked.insert_beggining(1)
print(linked)
linked.insert_beggining(2)
print(linked)
linked.insert_last(3)
print(linked)
linked.insert_last(4)
print(linked)
linked.remove(1)
print(linked)
linked.remove(4)
print(linked)
linked.remove(2)
print(linked)
