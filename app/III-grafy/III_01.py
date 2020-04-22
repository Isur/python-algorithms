"""
    Dijkstra.
"""

exampleGraph = {
    '0': {
        '1': 2,
        '2': 2,
        '3': 6,
        '4': 3,
    },
    '1': {
        '0': 2,
        '2': 2,
        '5': 1,
        '6': 1,
    },
    '2': {
        '0': 2,
        '1': 2,
        '4': 2,
        '5': 1,
    },
    '3': {
        '0': 6,
        '5': 2,
        '7': 3,
    },
    '4': {
        '0': 3,
        '2': 2,
        '6': 4,
        '7': 5,
    },
    '5': {
        '1': 1,
        '2': 1,
        '3': 2,
        '6': 2,
        '7': 2,
    },
    '6': {
        '1': 1,
        '4': 4,
        '5': 2,
        '7': 2,
    },
    '7': {
        '3': 3,
        '4': 5,
        '5': 2,
        '7': 2,
    },
}


MAGIC = 66666666  # to make things easier


class Dijkstra(object):
    def __init__(self, graph):
        self.graph = graph

    def _init(self, start):
        # set stasrt and all
        # not seen to magic number
        # to make calculations easier
        self.path = []
        self.distance = {}
        self.p = {}
        self.notSeen = self.graph.copy()
        for node in self.notSeen:
            self.distance[node] = MAGIC
        self.distance[start] = 0

    def _loop(self):
        # loop through all nodes to find way
        minimum = None
        for node in self.notSeen:
            if minimum is None:
                minimum = node
            elif self.distance[node] < self.distance[minimum]:
                minimum = node

        for node, weight in self.graph[minimum].items():
            if weight + self.distance[minimum] < self.distance[node]:
                self.distance[node] = weight + self.distance[minimum]
                self.p[node] = minimum
        self.notSeen.pop(minimum)

    def _way(self, start, end):
        # find way back
        current = end
        while current != start:
            try:
                self.path.insert(0, current)
                current = self.p[current]
            except KeyError:
                return 'Path not reachable'
                break
        self.path.insert(0, start)
        if self.distance[end] != MAGIC:
            return {
                'distance': self.distance[end],
                'path': self.path,
            }

    def findPath(self, start, end):
        self._init(start)
        while self.notSeen:
            self._loop()
        return self._way(start, end)


d = Dijkstra(exampleGraph)
print(d.findPath('0', '7'))
print(d.findPath('7', '0'))
print(d.findPath('0', '1'))
print(d.findPath('0', '5'))
print(d.findPath('5', '7'))