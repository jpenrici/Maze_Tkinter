# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-
#
# Reference:
#   https://docs.python.org/3/library/tkinter.html

from tkinter import *
from tkinter import messagebox
from maze_matrix import Maze
from random import choice


class MazeGUI(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Hobby")
        self.master.bind("<KeyPress>", self.action)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.top = Frame(self.master)
        self.middle = Frame(self.master)
        self.bottom = Frame(self.master)

        self.info = Label(self.top, text="Connect the dots in the maze.")
        self.info.pack(side="left")

        text = "Use the LEFT MOUSE BUTTON to draw. " \
               "Or press SPACE to change the maze."
        self.status = Label(self.bottom, text=text)
        self.status.pack(side="left")

        self.height, self.width = 500, 550
        self.canvas = Canvas(self.middle, height=self.height, width=self.width)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.pack()
        self.make()

        self.top.pack()
        self.middle.pack()
        self.bottom.pack()

    def action(self, event):
        if event.keycode == 65:  # BackSpace
            self.make()
            print(self.maze)

    def paint(self, event):
        x, y = event.x, event.y
        if x < self.borderX or x > (self.width - self.borderX): return
        if y < self.borderY or y > (self.height - self.borderY): return

        mx = int((x - self.borderX) / self.size)
        my = int((y - self.borderY) / self.size)
        if self.maze.maze[my * self.cols + mx]:
            messagebox.showinfo("Error", "Try again!")
            self.render()
            return

        self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1)

    def make(self):
        style = [[10, 40], [12, 30], [15, 28], [18, 24], [20, 20], [25, 16],
            [30, 14], [35, 12], [45, 10]]  # [Cells, Size]
        self.cells, self.size = choice(style)
        self.maze = Maze(self.cells, self.cells)
        if choice([True, False]): self.maze.reverse()
        self.render()

    def render(self):
        self.rows, self.cols = self.maze.size
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="#fff")
        self.borderX = (self.width - (self.size * self.cols)) / 2
        self.borderY = (self.height - (self.size * self.rows)) / 2
        y = self.borderY
        for r in range(self.rows):
            x = self.borderX
            for c in range(self.cols):
                fill = "#00f" if self.maze.maze[r * self.cols + c] else "#fff"
                if [c, r] == self.maze.first: fill = "#0f0"
                if [c, r] == self.maze.last: fill = "#f00"
                self.canvas.create_rectangle(x, y, x + self.size, y + self.size,
                    fill=fill)
                x += self.size
            y += self.size


if __name__ == '__main__':
    root = Tk()
    app = MazeGUI(master=root)
    app.mainloop()
