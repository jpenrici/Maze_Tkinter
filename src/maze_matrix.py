# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

from random import randint, choice


class Maze():

    __limit = 10  # minimum

    def __init__(self, rows, cols, model="basic"):
        self.size = (max(rows, self.__limit), max(cols, self.__limit))
        self.matrix = []  # values: 0 = wall, 1 = free, 2 = route
        self.route = []   # coordinates in matrix

        if model == "spiral":
            self.model = model
            self.spiral()
        else:
            # standard model
            if rows % 2 == 0:
                rows += 1
            self.size = (max(rows, self.__limit), max(cols, self.__limit))
            self.model = "basic"
            self.basic()

    def basic(self):
        rows, cols = self.size
        begin, end = 2, cols - 3
        x = randint(begin, end)
        for y in range(rows):
            if y % 2 == 0:
                self.matrix += [int(i == x) for i in range(cols)]
                self.matrix[y * cols + x] = 2
                self.route += [(x, y)]
            else:
                self.matrix += [int(i % (cols - 1) != 0) for i in range(cols)]
                if choice([True, False]):
                    self.matrix[y * cols + x + 1] = 0
                    x = randint(begin, x)
                else:
                    self.matrix[y * cols + x - 1] = 0
                    x = randint(x, end)

    def spiral(self):
        rows, cols = self.size
        self.matrix = [0 for i in range(rows * cols)]

        step = 0
        x, x0, x1 = 1, 1, cols - 2
        y, y0, y1 = 1, 3, rows - 2
        self.matrix[cols] = 2
        self.route = [(0, 1)]

        while True:
            if x == y:
                self.matrix[y * cols + x] = 2
                self.route += [(x, y)]
            else:
                self.matrix[y * cols + x] = 1
            if step % 4 == 0:
                if x == x1:
                    x1 -= 2
                    step += 1
                else:
                    x += 1
            if step % 4 == 1:
                if y == y1:
                    y1 -= 2
                    step += 1
                else:
                    y += 1
            if step % 4 == 2:
                if x == x0:
                    x0 += 2
                    step += 1
                else:
                    x -= 1
            if step % 4 == 3:
                if y == y0:
                    y0 += 2
                    step += 1
                else:
                    y -= 1
            if x0 > x1 or y0 > y1:
                break

        self.matrix[y * cols + x] = 2
        self.route += [(x, y)]

    def reverse(self):
        matrix = []
        rows, cols = self.size
        for x in range(cols):
            for y in range(rows):
                matrix += [self.matrix[y * cols + x]]
        self.matrix = matrix[::]
        self.size = (cols, rows)
        self.route = [i[::-1] for i in self.route]

    def show(self):
        symbol = ['#', '.', '@']  # [0 = wall, 1 = free, 2 = route]
        rows, cols = self.size
        out = ""
        for i in range(len(self.matrix)):
            if i % cols == 0:
                out += "\n"
            out += symbol[self.matrix[i]]
        print("{}\n".format(out))

    def __str__(self):
        rows, cols = self.size
        out = "Maze {} ({},{}) : Input {} Output {}".format(self.model,
            rows, cols, self.route[0], self.route[-1])
        return out


if __name__ == '__main__':
    # Basic
    maze = Maze(10, 10)
    print(maze)
    maze.reverse()
    print(maze)
    maze.reverse()
    print(maze)
    maze.show()

    # Spiral
    maze = Maze(10, 10, "spiral")
    print(maze)
    maze.reverse()
    print(maze)
    maze.show()
