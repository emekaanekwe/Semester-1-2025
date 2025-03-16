import numpy as np


i_state = ((1, 2, 3,
            4, 0, 6,
            7, 5, 8))
g_state = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)
   
# return all valid next states    
def get_neighbors():
    
    moves = {"Up": (0,0), "Down": (1,1), "Left": (1,0), "Right": (0,1)}
    
    # bfs
    traversed = []
    while i_state:
        state, path = i_state.pop(0)
        if state == g_state:
            print(i_state)
            return path
        
        if state not in traversed:
            traversed.add(state)
            for next in get_neighbors(state):
                i_state.append((next, path + [next]))
        
        
            
            
            
    