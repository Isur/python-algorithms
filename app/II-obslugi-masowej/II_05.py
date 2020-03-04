"""
    Lista dwukierunkowa.
"""
class Elem(object):
    def __init__(self, prev, value, next):
        self.prev = prev
        self.value = value
        self.next = next
        if next is not None:
            next.prev = self
        if prev is not None:
            prev.next = self
    
    def __str__(self):
        return f"{self.value}"

    def printAllNext(self):
        print("This and next...:")
        print(f"{self.value}")
        n = self.next
        while n is not None:
            print(f"{n.value}")
            n = n.next

    def printAllPrev(self):
        print("This and prev...:")
        print(f"{self.value}")
        n = self.prev
        while n is not None:
            print(f"{n.value}")
            n = n.prev
            
    def add(self, elem):
        self.next = elem

    
elem = Elem(None, 1, None)
elemPrev = Elem(None, 0, elem)
elemNext = Elem(elem, 2, None)

elem.printAllNext()
elem.printAllPrev()
