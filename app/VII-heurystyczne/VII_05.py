"""
    Pszczeli (Bee algorithm).
"""
from random import uniform, choice, randint
import functions
import sys
import math


class Bee(object):
    def __init__(self, bounds, vars):
        self.vars = vars
        self.bounds = bounds
        self.value = None
        self._construct()

    def _construct(self):
        pos = []
        for i in range(self.vars):
            pos.append(uniform(self.bounds[0], self.bounds[1]))
        self.position = pos

    def evaluate(self, func):
        self.value = func(self.position)

    def move(self, bee, func):
        r = uniform(-1.0, 1.0)
        k = randint(0, self.vars - 1)
        k_pos = self.position[k] + r * (self.position[k] - bee.position[k])

        if k_pos > self.bounds[1]:
            k_pos = self.bounds[1]
        if k_pos < self.bounds[0]:
            k_pos = self.bounds[0]

        candidate = []
        for i in range(self.vars):
            if i != k:
                candidate.append(self.position[i])
            else:
                candidate.append(k_pos)

        if func(candidate) < self.value:
            self.position = candidate
            self.evaluate(func)

    def __str__(self):
        return f"{self.position} - {self.value}"


class BeeAlg(object):
    def __init__(self, colony_size, vars, bounds, func, expert, precission):
        self.colony_size = colony_size
        self.vars = vars
        self.bounds = bounds
        self.func = func
        self.expert = expert
        self.precission = precission
        self.colony = []
        self._init_colony()

    def progress(self, progress):
        sys.stdout.write(f"\r{round(progress,2)}%")
        sys.stdout.flush()

    def run(self, generations):
        results = []
        for i in range(generations):
            r = self._run()
            results.append(r)
            progress = (i + 1) / generations * 100
            self.progress(progress)
            if abs(r.value - self.expert) < self.precission:
                break
        self.results = results
        return [r, len(results)]

    def _run(self):
        self._calculate()
        for bee in self.colony:
            top_bees = self._top()
            random_top = choice(top_bees)
            bee.move(random_top, self.func)
        return self._best()

    def _calculate(self):
        for agent in self.colony:
            agent.evaluate(self.func)

    def _sort(self):
        self.colony.sort(key=lambda x: x.value)

    def _top(self, n=None):
        if n is None:
            n = self.colony_size // 10
        self._sort()
        return self.colony[:n]

    def _best(self):
        best = self.colony[0]
        for bee in self.colony:
            if bee.value < best.value:
                best = bee
        return best

    def _init_colony(self):
        for i in range(self.colony_size):
            self.colony.append(Bee(self.bounds, self.vars))


class Func(object):
    def __init__(self, range, func, expert=None, precission=1e-06):
        self.range = range
        self.function = func
        self.expert = expert
        self.precission = precission
        self.__name__ = func.__name__

    def __str__(self):
        return (f"{self.__name__} in range {self.range}"
                f" with expert knowlnegde {self.expert}"
                f" with precission {self.precission}")


funcs = [Func([-10, 10], functions.rastragin, 0),
         Func([-10, 10], functions.rosenbrock, 0, 1e-04),
         Func([-100, 100], functions.hyper_ellipsoid, 0),
         Func([-10, 10], functions.sphere, 0),
         Func([-10, 10], functions.sum_squares, 0),
         Func([-10, 10], functions.styblinski_tang, -39.2, 1e-02)]

vars = 4
pop_size = 100
max_runs = 2000
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}")


for fun in funcs:
    print(fun)
    genetic = BeeAlg(pop_size, vars,
                     fun.range, fun.function,
                     fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best} \n in {n} generations")
    print("=====")
