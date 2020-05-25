"""
    Mrówkowy (ant algorithm)
"""
from random import uniform, choice, randint
import functions
import sys


class Ant(object):
    def __str__(self):
        return f"{self.position} - {self.value}"

    def __init__(self, bounds, vars):
        self.vars = vars
        self.bounds = bounds
        self.horizont = abs(bounds[1])
        self.value = None
        self._construct()

    def _construct(self):
        pos = []
        for i in range(self.vars):
            pos.append(uniform(self.bounds[0], self.bounds[1]))
        self.position = pos

    def evaluate(self, func):
        self.value = func(self.position)

    def move(self, best, func):
        for i in range(self.vars):
            move = uniform(-self.horizont, self.horizont)
            self.position[i] = best[0][i] + move
            if self.position[i] < self.bounds[0]:
                self.position[i] = self.bounds[0]
            if self.position[i] > self.bounds[1]:
                self.position[i] = self.bounds[1]
        self.horizont *= 0.9
        self.evaluate(func)


class AntAlg(object):
    def __init__(self, colony_size, vars, bounds, func, expert, precission):
        self.colony_size = colony_size
        self.vars = vars
        self.bounds = bounds
        self.func = func
        self.expert = expert
        self.precission = precission
        self.colony = []
        self.best = [None, None]
        self._init_colony()
        self._set_best()

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
        self._move_all()
        self._set_best()
        return self._best()

    def _move_all(self):
        for ant in self.colony:
            ant.move(self.best, self.func)

    def _sort(self):
        self.colony.sort(key=lambda x: x.value)

    def _top(self, n=None):
        if n is None:
            n = self.colony_size // 10
        self._sort()
        return self.colony[:n]

    def _best(self):
        best = self.colony[0]
        for ant in self.colony:
            if ant.value < best.value:
                best = ant
        return best

    def _set_best(self):
        best = self.colony[0]
        for ant in self.colony:
            if ant.value < best.value:
                best = ant
        self.best = [best.position, best.value]

    def _init_colony(self):
        for i in range(self.colony_size):
            ant = Ant(self.bounds, self.vars)
            ant.evaluate(self.func)
            self.colony.append(ant)

    def show(self, ants):
        for ant in ants:
            print(ant)


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
         Func([-10, 10], functions.sum_squares, 0)]

vars = 3
pop_size = 1000
max_runs = 2000
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}")


for fun in funcs:
    print(fun)
    genetic = AntAlg(pop_size, vars,
                     fun.range, fun.function,
                     fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best} \n in {n} generations")
    print("=====")
