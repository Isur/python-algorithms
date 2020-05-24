"""
    Kukułki (Cuckoo search)
"""
from random import randint, choice, uniform, sample
import sys
import functions
import math
import time


class Agent(object):
    def __init__(self, genes):
        self.genes = genes
        self.size = len(genes)
        self.value = None

    def mutate(self):
        pass

    def cross(self):
        pass

    def levy_flight(self, func):
        new_genes = []
        for i in range(self.size):
            new_genes.append(self._levy_flight(self.genes[i]))
        agent = Agent(new_genes)
        agent.evaluation(func)
        if agent.value < self.value:
            self.genes = agent.genes
            self.evaluation(func)

    def _levy_flight(self, u):
        if randint(0, 100) < 50:
            return u + 0.1*u
        else:
            return u - 0.1*u

    def evaluation(self, eval):
        self.value = eval(self.genes)

    def __str__(self):
        return " ".join(str(self.genes)) + f" = {self.value}"


class CuckooSearch(object):
    def __init__(self, range,
                 args, func,
                 size,
                 expert=None,
                 precission=0.000001):
        self.min = range[0]
        self.max = range[1]
        self.args = args
        self.size = size
        self.func = func
        self.expert = expert
        self.precission = precission
        self._init_population()

    def progress(self, progress):
        sys.stdout.write(f"\r{round(progress,2)}%")
        sys.stdout.flush()

    def run(self, generations):
        results = []
        self._evaluate()
        for i in range(generations):
            # self.show_population()
            r = self._run_cs()
            results.append(r)
            progress = (i + 1) / generations * 100
            self.progress(progress)
            if abs(r.value - self.expert) < self.precission:
                break
            # time.sleep(1)
        self.results = results
        return [self._select_best(results), len(results)]

    def _run_cs(self):
        r, x = self._random_cockoo()
        r.evaluation(self.func)
        r.levy_flight(self.func)
        x.evaluation(self.func)
        if r.value < x.value:
            x.genes = r.genes
            x.evaluation(self.func)
        self._sort()
        self._limit()
        return self._select_best()

    def _random_cockoo(self):
        return sample(self.population, 2)

    def _init_population(self):
        self.population = []
        for i in range(self.size):
            self._build_nest()

    def _build_nest(self):
        genes = []
        for j in range(self.args):
            genes.append(uniform(self.min, self.max))
        agent = Agent(genes)
        agent.evaluation(self.func)
        self.population.append(agent)

    def _sort(self):
        self.population.sort(key=lambda x: x.value)

    def _limit(self):
        self.population = self.population[:self.size]

    def _evaluate(self):
        for agent in self.population:
            agent.evaluation(self.func)

    def _select_best(self, agents=None):
        if agents is None:
            agents = self.population
        best = agents[0]
        for agent in agents:
            if agent.value < best.value:
                best = agent
        return best

    def show_population(self, pop=None):
        if pop is None:
            pop = self.population
        for agent in pop:
            print(agent)


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
         Func([-10, 10], functions.styblinski_tang, -39.2, 1e-01)]

vars = 2
pop_size = 500
max_runs = 50000
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}")

for fun in funcs:
    print(fun)
    genetic = CuckooSearch(fun.range, vars,
                           fun.function, pop_size,
                           fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best}\n in {n} generations")
    print("=====")
