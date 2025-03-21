import numpy as np
from collections import deque

'''
Using the Sokoban Puzzle to implement BFS

# - walls
$ - box
@ - agent

Questions to ask:

--How is the Agent Function expressed in this puzzle?--

g(f: P* -> A), where g(x) = move box to desired position using smallest state sequence

1. what is P*
    - the grid
    - starting position
    - environment (boxes)

2. What is A
    - g(x): the shortest set sequence 
    
3. What are the constraints of g(f(x))
    - agent can only move u, d, l r
    - box and only be "pushed" and nothing else
    - cannot move through walls
    - box cannot be pushed into a wall

'''

# state space where 

grid = [
    "#######",
    "#  .  #",
    "#  $  #",
    "#  @  #",
    "#######"
    ]

agent = ([])
boxes = set()
goals = set()
directions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}
            # (-1,0) reduce row index by 1
            # (1,0) increase by 1 
            # (0,-1) reduce column index by 1
            # (0,1) increase by 1
            
def get_positions(grid):
    #pos = enumerate(list(grid))
    #for i in pos:
     #   print(i)
    
    '''
    l_grid = enumerate(map(lambda x: x, grid))
    print(l_grid)
    for c, char in l_grid:
        if char != "@" in c:
            agent = (char, c)
            print(agent)
    
    '''
    
    """initialize grid from tuple to assignable parts

    Returns: parts of grid
        _type_: tuple
    """
    # take the grid string and create a 0-indexed row,col formatted grid 
    print(grid)
    print("in grid, scan row; assign int to it\n")
    for r, row in enumerate(grid):
        print(f"r is the number assigned to each row {r}")
        print(f"row is each row {row}")
        for c, char in enumerate(row):
            print(f"scan each number assigned to row: {c}")
            print(f"scan each char in row {char}")
            print("format", r, row, c, char)
            '''
              0123456
            0 #######
            1 #  .  #
            2 #  $  #
            3 #  @  #
            4 #######
            '''
            # assign the positional values of var based on the position of the char
            if char == "@":
                agent = (r, c)
                print(agent)
            elif char == "#":
                boxes.add((r,c)) 
            elif char == ".":
                goals.add((r,c))
    
    '''
              0123456
            0 #######
            1 #  .  # <- goal
            2 #  $  # <- box
            3 #  @  # <- agent
            4 #######
    '''
    return agent, boxes, goals # TODO: double check the functionality of this return
    

def sokoban(grid):
    """creates the state_0 for the agent, objects, and environment

    Args:
        grid (list): the environment 

    Returns:
        None
    """
    
    # 2. create initial positions
    s_agent, s_boxes, goals = get_positions(grid)

    
    # 3. initialize the queue list FIFO
    queue = deque([(s_agent, frozenset(s_boxes), [])])
    """make var that has an empty queue with the agent and boxes starting positions
    Data: tuples
    Job: optimize FIFO
    

    Returns:
        _type_:
    """
    
    visited = set([(s_agent, frozenset(s_boxes))])
    """make a var that creates a collection that can
    store *unqie* elements. 
    this is used to avoid revisits and more loops

    Returns:
        _type_:
    """


get_positions(grid)