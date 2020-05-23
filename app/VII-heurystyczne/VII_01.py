"""
    Genetyczny (genetic)
"""
from random import randint, choice, uniform
import sys
import functions


class Individual(object):
    def __init__(self, genes):
        self.genes = genes
        self.size = len(genes)
        self.value = None

    def mutation(self, probability):
        for i in range(self.size):
            if randint(0, 100) < probability:
                self.genes[i] += self._mutate(self.genes[i])

    def cross(self, ind):
        if self.size != ind.size:
            raise ValueError("Those individuals are not same size")
        return self._avg_crossover(ind)

    def evaluation(self, eval):
        self.value = eval(self.genes)

    def set_probability(self, prob):
        self.probability = prob

    def _uniform_crossover(self, ind):
        new_genes = []
        for i in range(self.size):
            if i % 2 == 0:
                new_genes.append(self.genes[i])
            else:
                new_genes.append(ind.genes[i])
        return Individual(new_genes)

    def _avg_crossover(self, ind):
        new_genes = []
        for i in range(self.size):
            new_genes.append((self.genes[i] + ind.genes[i]) / 2)
        return Individual(new_genes)

    def _mutate(self, gene):
        percent = randint(-10, 10)
        return gene * (percent / 100)

    def __str__(self):
        return " ".join(str(self.genes)) + f" = {self.value}"


class GeneticAlgorithm(object):
    def __init__(self, range,
                 args, func,
                 size, expert=None,
                 precission=0.000001):
        self.min = range[0]
        self.max = range[1]
        self.args = args
        self.size = size
        self._init_population()
        self.func = func
        self.expert = expert
        self.precission = precission

    def show_population(self):
        for agent in self.population:
            print(agent)

    def progress(self, progress):
        sys.stdout.write(f"\r{round(progress,2)}%")
        sys.stdout.flush()

    def run(self, generations):
        results = []
        for i in range(generations):
            r = self._run_genetic()
            results.append(r)
            progress = (i + 1) / generations * 100
            self.progress(progress)
            if abs(r.value - self.expert) < self.precission:
                break
        self.results = results
        return [self._select_best(results), len(results)]

    def _run_genetic(self):
        self._evaluate_individuals()
        selected = self._selection()
        self._crossing(selected, 90)
        self._mutating(selected, 10)
        self._populate(selected)
        return self._select_best()

    def _init_population(self):
        self.population = []
        for i in range(self.size):
            genes = []
            for j in range(self.args):
                genes.append(uniform(self.min, self.max))
            self.population.append(Individual(genes))

    def _evaluate_individuals(self, agents=None):
        if agents is None:
            agents = self.population
        for agent in agents:
            agent.evaluation(self.func)

    def _selection(self):
        return self._ranking_selection(len(self.population) // 2)

    def _crossing(self, agents, probability):
        new_agents = []
        for agent in agents:
            if randint(0, 100) <= probability:
                random_agent = choice(agents)
                new_agents.append(agent.cross(random_agent))
        self._evaluate_individuals(new_agents)
        agents += new_agents

    def _populate(self, agents):
        diff = self.size - len(agents)
        self.population = agents
        self._sort()
        if diff > 0:
            copy = diff * 2
            self.population = self.population[:copy] + self.population
            self.population = self.population[:self.size]

    def _mutating(self, agents, probability):
        for agent in agents:
            agent.mutation(probability)

    def _ranking_selection(self, n):
        self._sort()
        return self.population[:n]

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

vars = 2
pop_size = 200
max_runs = 10000
print(f"Settings:"
      f"\n number of variables: {vars}"
      f"\n size of population: {pop_size}"
      f"\n max runs: {max_runs}")
for fun in funcs:
    print(fun)
    genetic = GeneticAlgorithm(fun.range, vars,
                               fun.function, pop_size,
                               fun.expert, fun.precission)
    best, n = genetic.run(max_runs)
    print(f"\n{best}\n in {n} generations")
    print("=====")
