__author__ = 'alan'

from maze import *
from q import *

def printKey(event):
    if event.keysym == 'Left':
        maze.mouse.move_left()

    elif event.keysym == 'Right':
        maze.mouse.move_right()

    elif event.keysym == 'Up':
        maze.mouse.move_up()

    elif event.keysym == 'Down':
        maze.mouse.move_down()

    elif event.keysym == 't':
        q = Q(row, col,maze)
        q.train(root,30)
        q.test(0)


root = Tk()
root.title("我的迷宫")
root.bind('<KeyPress>', printKey)
canvas = Canvas(root)

canvas.pack()

row = 15
col = 15
maze = Maze(row, col, canvas)

root.mainloop()
