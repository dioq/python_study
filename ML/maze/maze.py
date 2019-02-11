__author__ = 'alan'
from random import randrange, shuffle
from mouse import *

sys.setrecursionlimit(100000)

BOTTOM_WALL = 0
RIGHT_WALL = 1
VISITED = 2
E, S, W, N = 0, 1, 2, 3
DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
CELL_WIDTH = 30


class Maze:
    def __init__(self, row, col, canvas):
        self.canvas = canvas
        self.mouse = Mouse(self)
        self.gif = PhotoImage(file='./image/flag.gif')
        self.image = None

        self.directs = [0b1111 for i in range(row * col)]
        self.actions = [[] for i in range(row * col)]
        self.row, self.col = row, col
        self.maze = [[[True, True, False] for c in range(col)] for r in range(row)]
        self.makepath(randrange(row), randrange(col))
        self.draw()

        for i in range(self.row * self.col):
            left, right, top, bottom = self.getNeighbor(i)
            if left < 0:
                self.directs[i] &= 0b0111  # 边缘，自身左侧有墙
            else:
                pass

            if right < 0:
                self.directs[i] &= 0b1101  # 边缘，自身右侧有墙
            else:
                if self.maze[i // self.col][i % self.col][RIGHT_WALL]:
                    self.directs[i] &= 0b1101
                    self.directs[right] &= 0b0111

            if top < 0:
                self.directs[i] &= 0b1110

            if bottom < 0:
                self.directs[i] &= 0b1011
            else:
                if self.maze[i // self.col][i % self.col][BOTTOM_WALL]:
                    self.directs[i] &= 0b1011
                    self.directs[bottom] &= 0b1110

        # 根据directs生成actions
        #          0      1     2     3
        # return [left, right, top, bottom]

        for (index, direct) in enumerate(self.directs):
            if direct == 1:  # 上
                self.actions[index].append(self.getNeighbor(index)[2])
            elif direct == 2:  # 右
                self.actions[index].append(self.getNeighbor(index)[1])
            elif direct == 3:  # 右上
                self.actions[index].append(self.getNeighbor(index)[1])
                self.actions[index].append(self.getNeighbor(index)[2])
            elif direct == 4:  # 下
                self.actions[index].append(self.getNeighbor(index)[3])
            elif direct == 5:  # 上下
                self.actions[index].append(self.getNeighbor(index)[2])
                self.actions[index].append(self.getNeighbor(index)[3])
            elif direct == 6:  # 右下
                self.actions[index].append(self.getNeighbor(index)[1])
                self.actions[index].append(self.getNeighbor(index)[3])
            elif direct == 7:  # 右上下
                self.actions[index].append(self.getNeighbor(index)[1])
                self.actions[index].append(self.getNeighbor(index)[2])
                self.actions[index].append(self.getNeighbor(index)[3])
            elif direct == 8:  # 左
                self.actions[index].append(self.getNeighbor(index)[0])
            elif direct == 9:  # 左上
                self.actions[index].append(self.getNeighbor(index)[0])
                self.actions[index].append(self.getNeighbor(index)[2])
            elif direct == 10:  # 左右
                self.actions[index].append(self.getNeighbor(index)[0])
                self.actions[index].append(self.getNeighbor(index)[1])
            elif direct == 11:  # 左右上
                self.actions[index].append(self.getNeighbor(index)[0])
                self.actions[index].append(self.getNeighbor(index)[1])
                self.actions[index].append(self.getNeighbor(index)[2])
            elif direct == 12:  # 左下
                self.actions[index].append(self.getNeighbor(index)[0])
                self.actions[index].append(self.getNeighbor(index)[3])
            elif direct == 13:  # 左上下
                self.actions[index].append(self.getNeighbor(index)[0])
                self.actions[index].append(self.getNeighbor(index)[2])
                self.actions[index].append(self.getNeighbor(index)[3])
            elif direct == 14:  # 左右下
                self.actions[index].append(self.getNeighbor(index)[0])
                self.actions[index].append(self.getNeighbor(index)[1])
                self.actions[index].append(self.getNeighbor(index)[3])

    def getNeighbor(self, id):
        left = right = top = bottom = -1
        if id % self.col == 0:
            left = -1
        else:
            left = id - 1

        if (id + 1) % self.col == 0:
            right = -1;
        else:
            right = id + 1;

        if (id - self.col) >= 0:
            top = id - self.col
        else:
            top = -1

        if (id + self.col) < self.row * self.col:
            bottom = id + self.col
        else:
            bottom = -1

        return [left, right, top, bottom]

    def makepath(self, r, c, direct=None):

        maze = self.maze

        maze[r][c][VISITED] = True

        if direct == N: maze[r][c][BOTTOM_WALL] = False
        if direct == S: maze[r - 1][c][BOTTOM_WALL] = False
        if direct == W: maze[r][c][RIGHT_WALL] = False
        if direct == E: maze[r][c - 1][RIGHT_WALL] = False

        directs = []
        if r > 0: directs.append(N)
        if r < self.row - 1: directs.append(S)
        if c > 0: directs.append(W)
        if c < self.col - 1: directs.append(E)

        shuffle(directs)

        for d in directs:

            dr, dc = DIRECTION[d]

            if not maze[r + dr][c + dc][VISITED]:
                self.makepath(r + dr, c + dc, d)

    def draw_mouse(self, canvas):
        self.mouse.draw(canvas)

    def draw(self):
        canvas = self.canvas
        self.mouse.draw(canvas)

        print('draw')

        if self.image == None:
            self.image = canvas.create_image((20 + (self.col - 1) * 30 + 30 / 2, 20 + (self.row - 1) * 30 + 30 / 2),
                                             anchor='center', image=self.gif)

        d = 20

        canvas.config(width=d * 2 + self.col * CELL_WIDTH, height=d * 2 + self.row * CELL_WIDTH)
        line = canvas.create_line
        line(d, d, self.col * CELL_WIDTH + d, d)
        line(d, d, d, self.row * CELL_WIDTH + d)

        for r in range(self.row):
            for c in range(self.col):
                canvas.create_text(d + c * CELL_WIDTH + CELL_WIDTH / 2, d + r * CELL_WIDTH + CELL_WIDTH / 2,
                                   text=r * self.col + c,
                                   anchor='center')

                if self.maze[r][c][BOTTOM_WALL]:
                    line(c * CELL_WIDTH + d, r * CELL_WIDTH + CELL_WIDTH + d, c * CELL_WIDTH + CELL_WIDTH + d,
                         r * CELL_WIDTH + CELL_WIDTH + d)

                if self.maze[r][c][RIGHT_WALL]:
                    line(c * CELL_WIDTH + CELL_WIDTH + d, r * CELL_WIDTH + d, c * CELL_WIDTH + CELL_WIDTH + d,
                         r * CELL_WIDTH + CELL_WIDTH + d)
