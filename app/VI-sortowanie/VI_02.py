"""
    Bąbelkowe  (buble).
"""
from tester import Sorter


class Bubble_sort(Sorter):
    def sort(self):
        arr = self.array
        length = len(arr)
        for i in range(length):
            for j in range(1, length):
                if arr[j - 1] > arr[j]:
                    temp = arr[j - 1]
                    arr[j - 1] = arr[j]
                    arr[j] = temp

    def __str__(self):
        return "Bubble Sort"


def main():
    bubble = Bubble_sort()
    bubble.main(2)
    bubble.print_results()
