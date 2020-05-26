"""
    Świetlika (Firefly algorithm)
"""
from random import uniform, choice, randint
import functions
import sys
import math


class Firefly(object):
    def __str__(self):
        return f"{self.position} - {self.value}"

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


class FirAlg(object):
    def __init__(self, colony_size, vars, bounds, func, expert, precission):
        self.colony_size = colony_size
        self.vars = vars
        self.bounds = bounds
        self.func = func
        self.expert = expert
        self.precission = precission
        self.colony = []
        self.best = None
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
        for i in range(self.colony_size):
            ffi = self.colony[i]
            for j in range(self.colony_size):
                ffj = self.colony[j]
                if ffj.value < ffi.value:
                    dist = self._dist(ffi, ffj)
                    new_pos = self._new_pos(ffi, ffj, dist)
                    new_val = self.func(new_pos)
                    if new_val < ffi.value:
                        ffi.value = new_val
                        ffi.position = new_pos
                        if self.best is None or ffi.value < self.best.value:
                            self.best = ffi
        return self._best()

    def _new_pos(self, ffi, ffj, dist):
        new_pos = []
        gamma = 1
        beta = 1
        alpha = 0.1
        scale = self.bounds[1] - self.bounds[0]
        for i in range(self.vars):
            m1 = beta*math.exp(-gamma*(dist**2))
            m2 = ffj.position[i] - ffi.position[i]
            some_math = ffi.position[i] + m1 * m2 + alpha*scale*uniform(-1,1)
            new_pos.append(min(max(some_math, self.bounds[0]), self.bounds[1]))
        return new_pos

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
            firefly = Firefly(self.bounds, self.vars)
            firefly.evaluate(self.func)
            self.colony.append(firefly)

    def _dist(self, ffi, ffj):
        dist = 0
        for i in range(ffi.vars):
            dist += (ffi.position[i] - ffj.position[i])**2
        return dist


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

vars = 2
pop_size = 150
max_runs = 200
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}")


for fun in funcs:
    print(fun)
    genetic = FirAlg(pop_size, vars,
                     fun.range, fun.function,
                     fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best} \n in {n} generations")
    print("=====")
