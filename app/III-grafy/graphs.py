exampleGraph_1 = {
    '0': ['1', '2', '3', '4'],
    '1': ['0', '2', '5', '6'],
    '2': ['0', '1', '4', '5'],
    '3': ['0', '5', '7'],
    '4': ['0', '2', '6', '7'],
    '5': ['1', '2', '3', '6', '7'],
    '6': ['1', '4', '5', '7'],
    '7': ['3', '4', '5', '6']
}

exampleGraph_2 = {
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
