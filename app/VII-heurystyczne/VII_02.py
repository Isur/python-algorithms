"""
    Różnicowy (differential evolution)
"""
from random import randint, choice, uniform, sample
import sys
import functions


class Agent(object):
    def __init__(self, genes):
        self.genes = genes
        self.size = len(genes)
        self.value = None

    def mutate(self, others, F, func):
        r1, r2, r3 = others
        new_genes = []
        for i in range(self.size):
            g = r1.genes[i] + F * (r2.genes[i] - r3.genes[i])
            new_genes.append(g)
        return Agent(new_genes)

    def cross(self, agent, CR):
        new_genes = []
        for i in range(self.size):
            if randint(0, 100) < CR:
                new_genes.append(agent.genes[i])
            else:
                new_genes.append(self.genes[i])
        return Agent(new_genes)

    def evaluation(self, eval):
        self.value = eval(self.genes)

    def __str__(self):
        return " ".join(str(self.genes)) + f" = {self.value}"


class DE(object):
    def __init__(self, range,
                 args, func,
                 size, CR, F,
                 expert=None,
                 precission=0.000001):
        self.min = range[0]
        self.max = range[1]
        self.args = args
        self.size = size
        self._init_population()
        self.func = func
        self.expert = expert
        self.precission = precission
        self.cross_rate = CR
        self.mutation_constant = F

    def progress(self, progress):
        sys.stdout.write(f"\r{round(progress,2)}%")
        sys.stdout.flush()

    def run(self, generations):
        results = []
        for i in range(generations):
            r = self._run_de()
            results.append(r)
            progress = (i + 1) / generations * 100
            self.progress(progress)
            if abs(r.value - self.expert) < self.precission:
                break
        self.results = results
        return [self._select_best(results), len(results)]

    def _run_de(self):
        new_pop = []
        for agent in self.population:
            randoms = self._find_3_random(agent)
            mutated = agent.mutate(randoms, self.mutation_constant, self.func)
            crossed = agent.cross(mutated, self.cross_rate)
            agent.evaluation(self.func)
            crossed.evaluation(self.func)
            if crossed.value < agent.value:
                new_pop.append(crossed)
            else:
                new_pop.append(agent)
        self.population = new_pop
        return self._select_best()

    def _find_3_random(self, agent):
        randoms = []
        while len(randoms) == 0 or agent in randoms:
            randoms = sample(self.population, 3)
        return randoms

    def _random_index(self):
        return randint(1, self.args)

    def _init_population(self):
        self.population = []
        for i in range(self.size):
            genes = []
            for j in range(self.args):
                genes.append(uniform(self.min, self.max))
            self.population.append(Agent(genes))

    def _sort(self):
        self.population.sort(key=lambda x: x.value)

    def _select_best(self, agents=None):
        if agents is None:
            agents = self.population
        best = agents[0]
        for agent in agents:
            if agent.value < best.value:
                best = agent
        return best


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

vars = 7
pop_size = 200
max_runs = 100000
CR = 90
F = 0.5
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}"
      f"\n cross rate: {CR}"
      f"\n mutation const: {F}")
for fun in funcs:
    print(fun)
    genetic = DE(fun.range, vars,
                 fun.function, pop_size, CR, F,
                 fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best}\n in {n} generations")
    print("=====")
