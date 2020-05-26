"""
    Nietoperza (bat algorithm)
"""
from random import uniform, choice, randint
import functions
import sys
import math


class Bat(object):
    def __str__(self):
        return f"{self.position} - {self.value}"

    def __init__(self, bounds, vars):
        self.vars = vars
        self.bounds = bounds
        self.value = None
        self.freq = 0.0
        self.A = 0.95
        self.R = 0.1
        self.R0 = 0.1
        self.alpha = 0.95
        self.gamma = 0.95
        self.velocity = [0] * self.vars
        self._construct()

    def _construct(self):
        pos = []
        for i in range(self.vars):
            pos.append(uniform(self.bounds[0], self.bounds[1]))
        self.position = pos

    def evaluate(self, func):
        self.value = func(self.position)

    def move_to_best(self, best, fmin, fmax, func, mean_A):
        r = 1
        if self == best:
            return
        distance = 0
        new_pos = []
        self.freq = fmin + (fmax - fmin) * uniform(0, 1)
        for i in range(self.vars):
            self.velocity[i] += (self.position[i] - best[0][i]) * self.freq
            new_pos.append(self.position[i] + self.velocity[i])
        new_pos = self._norm(new_pos)

        if uniform(0, 1) > self.R:
            for i in range(self.vars):
                new_pos[i] = best[0][i] + uniform(-1.0, 1.0) * mean_A
            new_pos = self._norm(new_pos)

        val = func(new_pos)

        if uniform(0, 1) < self.A and val < self.value:
            self.value = val
            self.position = new_pos

        if self.value < best[1]:
            self.A *= self.alpha
            self.R = self.R0 * (1 - math.exp(-1*self.gamma*i))

    def _norm(self, pos):
        for i in range(len(pos)):
            if pos[i] < self.bounds[0]:
                pos[i] = self.bounds[0]
            if pos[i] > self.bounds[1]:
                pos[i] = self.bounds[1]
        return pos


class BatAlg(object):
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
        self._set_best()
        fmin, fmax = self._find_freq()
        mean_a = self._find_mean_A()
        for bat in self.colony:
            bat.move_to_best(self.best, fmin, fmax, self.func, mean_a)
        return self._best()

    def _sort(self):
        self.colony.sort(key=lambda x: x.value)

    def _find_freq(self):
        freq_min = freq_max = self.colony[0].freq
        for bat in self.colony:
            if bat.freq < freq_min:
                freq_min = bat.freq
            if bat.freq > freq_max:
                freq_max = bat.freq
        return freq_min, freq_max

    def _find_mean_A(self):
        m = 0
        for bat in self.colony:
            m += bat.A
        return m / len(self.colony)

    def _top(self, n=None):
        if n is None:
            n = self.colony_size // 10
        self._sort()
        return self.colony[:n]

    def _best(self):
        best = self.colony[0]
        for bat in self.colony:
            if bat.value < best.value:
                best = bat
        return best

    def _set_best(self):
        best = self._best()
        self.best = [best.position, best.value]

    def _init_colony(self):
        for i in range(self.colony_size):
            bat = Bat(self.bounds, self.vars)
            bat.evaluate(self.func)
            self.colony.append(bat)


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
pop_size = 1000
max_runs = 2000
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}")


for fun in funcs:
    print(fun)
    genetic = BatAlg(pop_size, vars,
                     fun.range, fun.function,
                     fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best} \n in {n} generations")
    print("=====")
