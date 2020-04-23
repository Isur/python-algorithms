"""
    Floyd.
"""

M = 66666666  # to make things easier
Z = 0

exampleGraph = [
    [Z, 2, 2, 6, 3, M, M, M],
    [2, Z, 2, M, M, 1, 1, M],
    [2, 2, Z, M, 2, 1, M, M],
    [6, M, M, Z, M, 5, M, 3],
    [3, M, 2, M, Z, M, 4, 5],
    [M, 1, 1, 2, M, Z, 2, 2],
    [M, 1, M, M, 4, 2, Z, 2],
    [M, M, M, 3, 4, 2, 2, Z]
]


def floyd(g):
    d = g
    length = len(g)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def printSolution(d):
    for i in d:
        for j in i:
            if j == M:
                print("X", end=" ")
            else:
                print(j, end=" ")
        print(" ")


printSolution(floyd(exampleGraph))
