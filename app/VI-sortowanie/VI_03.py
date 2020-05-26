"""
    Szybkie (quicksort)
"""
from tester import Sorter
import math


class Quick_sort(Sorter):
    def sort(self, left=0, right=None):
        if right is None:
            right = len(self.array)
        if right <= left:
            return
        piv = self.partition(left, right)
        self.sort(left, piv)
        self.sort(piv + 1, right)

    def partition(self, left, right):
        arr = self.array
        pivot = arr[left]
        i = left + 1
        j = right - 1

        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                arr[left], arr[j] = arr[j], arr[left]
                return j

    def __str__(self):
        return "Quick Sort"


def main():
    quick = Quick_sort()
    quick.main()
    quick.print_results()


if __name__ == "__main__":
    main()
