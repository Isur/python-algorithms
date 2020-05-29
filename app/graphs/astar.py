"""
    A*
"""
import math

"""
Maze elements:
0 - Empty
1 - Wall
2 - Start Point
3 - End Point
4 - Path
"""

example_maze = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Default values
start_point = (1, 1)
end_point = (2, 17)

# directions for movements
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


class Node(object):
    """ Node for the A* algorithm """
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.dist_g = 0  # distance to node
        self.dist_h = 0  # heuristic distance
        self.dist_f = 0  # g + h

    def __eq__(self, other):
        return self.position == other.position


def a_star(maze, start, end):
    """ A*  algorithm

    Args:
        maze: array of arrays
        start: [x,y] start here
        end: [x,y] end here
    Returns:
        path
    """

    # Initialization
    start_node = Node(None, start)
    end_node = Node(None, end)
    open_list = []
    closed_list = []
    open_list.append(start_node)

    # Loop until find the end
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for node_index, node in enumerate(open_list):
            if node.dist_f < current_node.dist_f:
                current_node = node
                current_index = node_index

        open_list.pop(current_index)
        closed_list.append(current_node)

        # If end, create and return path
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # reversed path

        children = []
        for new_pos in DIRECTIONS:
            node_position = (current_node.position[0] + new_pos[0],
                             current_node.position[1] + new_pos[1])
            # Verify if position is ok
            if node_position[0] > len(maze) - 1 or \
               node_position[0] < 0 or \
               node_position[1] > len(maze[len(maze)-1]) - 1 or \
               node_position[1] < 0:
                continue

            # Verify if can move on new position:
            if maze[node_position[0]][node_position[1]] == 1:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            tmp = False
            for closed_child in closed_list:
                if child == closed_child:
                    tmp = True
            if tmp is True:
                continue

            child.dist_g = current_node.dist_g + 1
            child.dist_h = heuristic(child.position, end_node.position)
            child.dist_f = child.dist_g + child.dist_h
            tmp = False
            for open_node in open_list:
                if child == open_node and child.dist_g > open_node.dist_g:
                    tmp = True
            if tmp is True:
                continue
            open_list.append(child)


def heuristic(a, b):
    """ Euclidean Distance """
    x1, y1 = a
    x2, y2 = b
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance


def print_maze(maze):
    """ Print maze

    Args:
        maze: array of array
    """
    for row in maze:
        for item in row:
            if item == 0:
                i = " "
            elif item == 1:
                i = "█"
            elif item == 2:
                i = "S"
            elif item == 3:
                i = 'E'
            elif item == 4:
                i = '*'
            print(i, end=" ")
        print()


def print_path(maze, path):
    m = maze.copy()
    for p1, p2 in path:
        m[p1][p2] = 4
    return m


print("Maze with S as starting point, and E as ending point:")
example_maze[start_point[0]][start_point[1]] = 2
example_maze[end_point[0]][end_point[1]] = 3
print_maze(example_maze)
print("Path calculated with A* algorithm: ")
path = a_star(example_maze, start_point, end_point)
maze_with_path = print_path(example_maze, path)
print_maze(maze_with_path)
