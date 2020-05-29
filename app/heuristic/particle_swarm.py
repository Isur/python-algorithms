"""
    Rój cząstek (particle swarm)
"""
from random import uniform, randint, random
import functions
import sys
import time
import math


class Particle(object):
    def __init__(self, bounds, vars):
        self.vars = vars
        self.bounds = bounds
        self.value = None
        self.velocity = []
        self.best = [None, None]
        self._construct()

    def __str__(self):
        return " ".join(str(self.position)) + f" = {self.value}"

    def _construct(self):
        pos = []
        vel = []
        for i in range(self.vars):
            pos.append(uniform(self.bounds[0], self.bounds[1]))
            vel.append(uniform(-1, 1))
        self.velocity = vel
        self.position = pos

    def evaluate(self, func):
        self.value = func(self.position)
        if self.best[1] is None or self.value < self.best[1]:
            self.best = [self.position, self.value]

    def calculate_velocity(self, best):
        pb = self.best
        gb = best
        for i in range(self.vars):
            r1 = random()
            r2 = random()
            c1 = 1
            c2 = 2
            v1 = c1 * r1 * (pb[0][i] - self.position[i])
            v2 = c2 * r2 * (gb[0][i] - self.position[i])
            self.velocity[i] = self.velocity[i] + v1 + v2

    def move(self):
        for i in range(self.vars):
            self.position[i] += self.velocity[i]
            if self.position[i] > self.bounds[1]:
                self.position[i] = self.bounds[1]
            if self.position[i] < self.bounds[0]:
                self.position[i] = self.bounds[0]


class ParticleSwarm(object):
    def __init__(self, swarm_size, vars, bounds, func, expert, precission):
        self.swarm_size = swarm_size
        self.vars = vars
        self.bounds = bounds
        self.func = func
        self.expert = expert
        self.precission = precission
        self.swarm = []
        self.best = [None, None]
        self._swarm_init()

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
            if abs(r[1] - self.expert) < self.precission:
                break
        self.results = results
        return [r, len(results)]

    def _swarm_init(self):
        for i in range(self.swarm_size):
            self.swarm.append(Particle(self.bounds, self.vars))

    def _run(self):
        for i in range(self.swarm_size):
            self.swarm[i].evaluate(self.func)
            if self.best[1] is None or self.swarm[i].value < self.best[1]:
                self.best[0] = list(self.swarm[i].position)
                self.best[1] = float(self.swarm[i].value)
        for i in range(self.swarm_size):
            self.swarm[i].calculate_velocity(self.best)
            self.swarm[i].move()
        return self.best


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

vars = 2
pop_size = 1000
max_runs = 20000
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}")


for fun in funcs:
    print(fun)
    genetic = ParticleSwarm(pop_size, vars,
                            fun.range, fun.function,
                            fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best[0]} - {best[1]}\n in {n} generations")
    print("=====")
