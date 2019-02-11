__author__ = 'alan'
import numpy as np


class Q:
    def __init__(self, row, col, maze):
        self.maze = maze
        self.row = row
        self.col = col
        self.R = np.zeros((row * col, row * col))
        self.Q = np.zeros((row * col, row * col))
        self.R[:, row * col - 1] = 100
        print(self.R)

    def __episode(self, root):
        s = np.random.randint(self.row * self.col)  # 随机选择一个节点作为起点
        while s != self.row * self.col - 1:  # 不等于终点就一直循环
            s1 = a = np.random.choice(self.maze.actions[s])
            self.Q[s, a] = self.R[s, a] + 0.8 * self.Q[s1].max()
            s = s1

            # self.maze.mouse.set_position(s)
            # root.update()
            # print('训练节点：', s)

    def train(self, root, count):
        '''
        训练机器count次，使之Q矩阵收敛
        :param root: 为了更新界面用
        :param count: 训练次数
        :return: 
        '''
        for i in range(count):
            self.__episode(root)
        print(self.Q)

    def test(self, s):
        print(s)
        while s < self.row * self.col - 1:
            s = self.Q[s].argmax()
            print("->", s, )
