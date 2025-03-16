import numpy as np
import random


class Environment:
    def __init__(self, x, y):
        self.state = 0
        self.grid = np.zeroes(x,y)
        
        
        #d_x, d_y = []
        self.x, self.y = (y,x)
        
        # initilaize rain within grid
        
        
    def step(self):
        self.rain = random.randint(0,1)
            
        '''
        for el in grid:
            if self.x == 0 and self.y == 0:
                rain = random.randint(0,1)
        
        
        for i in grid:
            for j in i:
            
                if 
                '''
                    # agent moves
                    # if moves to rain
                    # reset
                    # else
                    # move to next place
             
        
        # features
            # set the dimensions of enviro
        
            # set the behavior metric
        
            # make reset
        
            # make configuration rules
        
        # methods/behaviors

            # define step with params (agent, action)
            
        
            
            
        
        
        
        def initialize(self):
            self.n
        # 
        
        
        
class Agent(Environment):
    def __init__(self, y, x):
        self.actions = {"up": 1, "down": 0, "left": 2, "right": 3}
        self.pos = (y,x)
        # self.type = blue, red
    
    def move(self):
        if Environment.state == 0:
            print("restart")
            return 0
        else:
            
    

#def __name__ if main

    #reset_sim()