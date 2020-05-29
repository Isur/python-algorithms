"""
    Scalanie (mergesort)
"""
from tester import Sorter


class Merge_sort(Sorter):
    def __str__(self):
        return "Merge Sort"

    def sort(self):
        self.mergeSort(self.array)

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        self.mergeSort(left)
        self.mergeSort(right)
        self.merge(left, right, arr)

    def merge(self, left, right, arr):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def main():
    sort = Merge_sort()
    sort.main()
    sort.print_results()


if __name__ == "__main__":
    main()
