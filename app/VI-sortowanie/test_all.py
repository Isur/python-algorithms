from VI_01 import Insert_Sort
from VI_02 import Bubble_sort
from VI_03 import Quick_sort
from VI_04 import Heap_sort
from VI_05 import Merge_sort
from tester import Setting
import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()


class Test_All_Sorts(object):
    def __init__(self, array=[]):
        self.array = array
        self.results = []
        self.sorting_settings = [
            Setting(100, 10, 100),
            Setting(50, 100, 1000),
            Setting(25, 1000, 10000),
            Setting(12, 10000, 100000),
            Setting(3, 100000, 1000000)
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
        i = 1
        for res in self.results:
            print(f"{res[1]} with {res[2]} in {res[0]}s")
            if i % 5 == 0 and i > 3:
                print()
            i += 1


Test_All_Sorts().work()
