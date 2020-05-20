"""
    Wstawianie (insert)
"""
from tester import Sorter


class Insert_Sort(Sorter):
    def sort(self):
        length = len(self.array)
        arr = self.array
        for i in range(1, length):
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j+1] = arr[j]
                j -= 1
            arr[j + 1] = temp

    def __str__(self):
        return "Insert Sort"


def main():
    ins = Insert_Sort()
    ins.main(2)
    ins.print_results()
