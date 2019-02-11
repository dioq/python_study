__author__ = 'alan'
import numpy as np

S = np.matrix([[0.1, 0.2 ,0.7]])
P = np.matrix([[0.5 ,0.3, 0.2],
               [0.3, 0.6, 0.1],
               [0.1 ,0.5 ,0.4]])
print(S)
# print(P)
# print('....')

for i in range(30):
    S = S*P
    print(S*P)