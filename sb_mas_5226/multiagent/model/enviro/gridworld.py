import random as rd
import numpy as np


# row
m = 3
# column 
n = 3

grid_states = [
        [0,1,2,3,4],
        [5,6,7,8,9],
        [10,11,12,13,14],
        [15,16,17,18,19],
        [20,21,22,23,24]
        ]

reward_vector = np.array([-0.1,-0.1,-0.1,-0.1,1])

transition_matrix = np.zeroes(m,n)

'''need to saisfy the closed form solution of the bellman equation
    need to solve values function: V=(I-gamma*P)*R
        I := identity matrix
        P := trans Pr matrix
        R := reward vector
'''

# create identity matrix
I = np.eye(n*m)

# compute matrix invere
    # @ R := performs the vector multiplcation
V = np.linalg.inv(transition_matrix) @ reward_vector