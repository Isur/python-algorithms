from insert_sort import Insert_Sort
from bubble_sort import Bubble_sort
from quick_sort import Quick_sort
from heap_sort import Heap_sort
from merge_sort import Merge_sort
from tester import Setting


class Test_All_Sorts(object):
    def __init__(self, array=[]):
        self.array = array
        self.results = []
        self.sorting_settings = [
            Setting(100, 10, 100),
            Setting(50, 100, 1000),
            Setting(25, 1000, 10000),
            Setting(12, 10000, 100000),
            Setting(1, 100000, 1000000)
        ]
        self.create_sorters()

    def create_sorters(self):
        insert = Insert_Sort()
        bubble = Bubble_sort()
        quick = Quick_sort()
        heap = Heap_sort()
        merge = Merge_sort()
        self.sorters = [insert, bubble, quick, heap, merge]

    def work(self):
        i = j = 0
        for setting in self.sorting_settings:
            j = 0
            print(setting)
            for sorter in self.sorters:
                print(sorter)
                if i > 2 and j < 2:
                    avg = 'too much '
                else:
                    avg = sorter.test(setting.tests,
                                      setting.min_array_size,
                                      setting.max_array_size, verbose=True)
                self.results.append([avg, str(sorter), str(setting)])
                j += 1
            i += 1
        self.results_print()

    def results_print(self):
        print("============")
        i = 0
        for res in self.results:
            if i % 5 == 0:
                print(res[2])
            i += 1
            print(f"{res[1]} in {res[0]}s")
        print("============")


Test_All_Sorts().work()
