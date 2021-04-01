# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-
#
# Reference:
#   https://docs.python.org/3/library/tkinter.html

from tkinter import *
from maze_matrix import Maze
from random import choice


class MazeGUI(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Hobby")
        self.master.geometry("500x500")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.top = Frame(self.master)
        self.middle = Frame(self.master)
        self.bottom = Frame(self.master)

        self.info = Label(self.top, text="Connect the dots in the maze.")
        self.info.pack(side="left")

        self.status = Label(self.bottom, text="Use the left mouse button to draw.")
        self.status.pack(side="left")

        self.canvas = Canvas(self.middle, height=450, width=500)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.pack()
        self.maze()

        self.top.pack()
        self.middle.pack()
        self.bottom.pack()

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2)

    def maze(self):

        style = [[10, 40], [12, 30], [15, 28], [18, 24], [20, 20], [25, 16],
                 [30, 14], [35, 12], [45, 10]]
        cells, size = choice(style)

        m = Maze(cells, cells)
        if choice([True, False]): m.reverse()
        rows, cols = m.size

        y = (450 - (size * rows)) / 2
        for r in range(rows):
            x = (500 - (size * cols)) / 2
            for c in range(cols):
                fill = "#00f" if m.maze[r * cols + c] else "#fff"
                if [c, r] == m.first: fill = "#0f0"
                if [c, r] == m.last: fill = "#f00"
                self.canvas.create_rectangle(x, y,x + size, y + size, fill=fill)
                x += size
            y += size


if __name__ == '__main__':
    root = Tk()
    app = MazeGUI(master=root)
    app.mainloop()
