__author__ = 'alan'

from tkinter import *


class Mouse:
    def __init__(self, maze):
        self.maze = maze
        self.id = 0
        self.x = self.y = 20
        self.gif = PhotoImage(file='./image/mouse.gif')
        self.image = None

    def move_left(self):
        if self.maze.directs[self.id] & 7 != self.maze.directs[self.id]:
            self.x -= 30
            self.id -= 1
            self.draw(self.maze.canvas)

    def move_right(self):
        if self.maze.directs[self.id] & 13 != self.maze.directs[self.id]:
            self.x += 30
            self.id += 1
            self.draw(self.maze.canvas)

    def move_up(self):
        if self.maze.directs[self.id] & 14 != self.maze.directs[self.id]:
            self.y -= 30
            self.id -= self.maze.col
            self.draw(self.maze.canvas)

    def move_down(self):
        if self.maze.directs[self.id] & 11 != self.maze.directs[self.id]:
            self.y += 30
            self.id += self.maze.col
            self.draw(self.maze.canvas)

    def draw(self, canvas):
        if self.image == None:
            self.image = canvas.create_image((20 + 30 / 2, 20 + 30 / 2), anchor='center', image=self.gif)
        canvas.coords(self.image, (self.x + 30 / 2, self.y + 30 / 2))

    def set_position(self, id):
        self.x = 20 + 30 * (id % self.maze.col)
        self.y = 20 + 30 * (id // self.maze.col)
        self.draw(self.maze.canvas)