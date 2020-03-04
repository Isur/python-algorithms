"""
    Lista jednokierunkowa.
"""

class Elem(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __str__(self):
        return f"{self.value}"

    def printAll(self):
        print(f"{self.value}")
        n = self.next
        while n is not None:
            print(f"{n.value}")
            n = n.next
            
    def add(self, elem):
        self.next = elem

    
elem = Elem(1, None)
elem2 = Elem(2, elem)
elem3 = Elem(3, elem2)
elem4 = Elem(4, elem3)
elem4.printAll()
