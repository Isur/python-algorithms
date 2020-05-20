import random
import time
import sys
from abc import ABC, abstractmethod


class Setting(object):
    def __init__(self, tests, min_array_size, max_array_size):
        self.tests = tests
        self.min_array_size = min_array_size
        self.max_array_size = max_array_size

    def __str__(self):
        return (f"{self.tests} sorts with min "
                f"{self.min_array_size} and max "
                f"{self.max_array_size} elements in array")


class Sorter(object):
    def __init__(self, array=[]):
        self.array = array
        self.results = []
        self.settings = [
            Setting(10, 10, 100),
            Setting(10, 100, 1000),
            Setting(10, 1000, 10000),
        ]

    @classmethod
    @abstractmethod
    def sort(self):
        ...

    @abstractmethod
    def __str__(self):
        ...

    def print_results(self):
        print(f"Summary {self}")
        for i in self.results:
            print(i)

    def random_array(self, length):
        arr = []
        for i in range(length):
            arr.append(random.randint(0, 10000))
        self.array = arr

    def random_array_sort(self, length):
        self.random_array(length)
        start = time.time()
        self.sort()
        return time.time() - start

    def progress(self, progress):
        sys.stdout.write(f"\r{round(progress,2)}%")
        sys.stdout.flush()

    def test(self, number, min_size, max_size, verbose=True):
        results = []
        for i in range(number):
            random_size = random.randint(min_size, max_size)
            sort_time = self.random_array_sort(random_size)
            results.append(sort_time)
            if verbose:
                progress = (i + 1) / number * 100
                self.progress(progress)

        if verbose is True:
            print()
        avg = sum(results) / len(results)
        res = (f"{number} of lists "
               f"with min {min_size} and max {max_size} elements "
               f"has been sorted in average {avg}s")
        self.results.append(res)
        return avg

    def main(self, lvl=None):
        if lvl is None:
            lvl = len(self.settings)
        for i in range(lvl):
            print((
                f"{self}: {self.settings[i].tests} sorts"
                f" with min {self.settings[i].min_array_size}"
                f" and max {self.settings[i].min_array_size} elements."
            ))
            self.test(self.settings[i].tests,
                      self.settings[i].min_array_size,
                      self.settings[i].max_array_size)

    def correct_test(self):
        self.random_array(10)
        self.sort()
        correct = True
        for i in range(1, len(self.array)):
            if self.array[i - 1] > self.array[i]:
                correct = False
        print("Correct" if correct else "Incorrect")
