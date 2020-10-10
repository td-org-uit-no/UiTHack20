from random import random, shuffle, randrange
import sys


def make_maze(w=100, h=300):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["# "] * w + ['#'] for _ in range(h)] + [[]]
    hor = [["##"] * w + ['#'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "# "
            if yy == y:
                ver[y][max(x, xx)] = "  "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])

    rows = [list(row) for row in s.split('\n') if len(row) > 0]

    return rows


if __name__ == '__main__':
    sys.setrecursionlimit(50000)
    maze = make_maze()

    for row in maze:
        print(row)

    print(len(maze[0]), ',', len(maze))
