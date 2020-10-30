from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def parse_list_to_op_string(pathlist):
    string = ''
    prev_x = -1
    prev_y = -1
    for x, y in pathlist:
        if prev_x == -1 and prev_y == -1:
            prev_x = x
            prev_y = y
            continue
        else:
            if prev_x == x and prev_y < y:  # moved only downwards
                string += 'd'
            elif prev_x == x and prev_y > y:  # moved only upwards
                string += 'a'
            elif prev_y == y and prev_x > x:  # moved only left
                string += 'w'
            elif prev_y == y and prev_x < x:  # moved only right
                string += 's'

            prev_x = x
            prev_y = y

    return string


def solve_maze(maze):
    level = []
    for row in maze:
        newrow = []
        for element in row:
            if(element == '#'):
                newrow.append(0)
            elif(element == ' '):
                newrow.append(1)
            elif(element == 'P'):
                newrow.append(2)
            elif(element == 'G'):
                newrow.append(3)
        level.append(newrow)

    grid = Grid(matrix=level)

    start_y, start_x = index_2d(level, 2)
    end_y, end_x = index_2d(level, 3)
    start_node = grid.node(start_x, start_y)
    end_node = grid.node(end_x, end_y)

    finder = AStarFinder()
    path, runs = finder.find_path(start_node, end_node, grid)

    output = parse_list_to_op_string(path)

    return output
