"""
    Stogowe (Heap sort)
"""
from tester import Sorter


class Heap_sort(Sorter):
    def __str__(self):
        return "Heap sort"

    def sort(self):
        arr = self.array
        length = len(arr)
        for i in range(length//2 - 1, -1, -1):
            self.heapify(length, i)

        for i in range(length - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(i, 0)

    def heapify(self, length, i):
        arr = self.array
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < length and arr[i] < arr[left]:
            largest = left
        if right < length and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(length, largest)


def main():
    sort = Heap_sort()
    sort.main()
    sort.print_results()
