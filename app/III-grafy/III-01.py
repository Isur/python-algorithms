"""
    Prim
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
        '6': 2,
    },
}

MAGIC = 6666666  # To make life easier


class Prim(object):
    """Prim algorithm"""
    def __init__(self, graph):
        self.graph = graph
        self.size = len(self.graph)

    def _init(self, start):
        """Initialization for new calculations

        Args:
            start: key of node
        """
        self.visited = {}   # All visited nodes
        self.visited[start] = {}  # Start node set up as visited
        self.totalWeight = 0  # Total weight after calculations

    def _minEdge(self):
        """Find edge with minimum weight for not visited nodes.
        Update visited and total weight
        """
        min = MAGIC  # lowest weight to compate with
        vertex = None  # vertex with lowest weight
        n = None  # node with egde to vertex
        for node in self.visited:
            for edge in self.graph[node]:
                if edge not in self.visited:
                    weight = self.graph[node][edge]
                    if weight < min:
                        min = weight
                        vertex = edge
                        n = node
        self.visited[vertex] = {}
        self.visited[vertex][n] = min
        self.totalWeight += min

    def prim(self, start):
        """
        Prim algorithm

        Args:
            start: name of node in graph

        Returns:
            minimum spanning tree, total weight
        """
        self._init(start)
        while len(self.visited) != self.size:
            self._minEdge()
        return self.visited, self.totalWeight


def printGraph(graph):
    " Print all nodes with neighbours and weights"
    for node in graph:
        print(f"{node}: {graph[node]}")


p = Prim(exampleGraph)
for n in exampleGraph:
    print("")
    print(f"Starting point at {n}")
    mst, total = p.prim(n)
    printGraph(mst)
    print(f"Total weight: {total}")
