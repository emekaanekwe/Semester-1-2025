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
    # store grid and get agent initial position
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "@":
                agent = (r, c) # this initializes the agent's position
                print(agent)
            elif char == "#":
                boxes.add((r,c)) # agent goes here 
            elif char == ".":
                goals.add((r,c)) # or agent goes here
    
    return agent, boxes, goals # TODO: double check the functionality of this return

    
# 1. define grid
def bfs_sokoban(grid):
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

    # bfs starts here    
    while queue: # continue the loop until queue is empty
        
        agent, boxes, path = queue.popleft() # TODO: test output
        """removes first el from queue

    Returns:
        _type_: _description_
    """
    
        # puzzle solved
        if boxes == goals: # when boxes coordinate is equal to goals coordinate
            return path 
    
        for move, (dr, dc) in directions.items(): # loop through all possible moves
            new_agent = (agent[0] + dr, agent[1] + dc) # TODO
            if grid[agent[0]][agent[1]] == "#": # check if agent is at grid index
                continue
            
            new_boxes = set(boxes)
            if new_agent in boxes:
                new_box = (new_agent[0]+dr, new_agent+dc)
                if grid[new_box[0][new_box[1]]] == "#" or new_box in boxes:
                    continue
                new_boxes.remove(new_agent)
                new_boxes.add(new_box)

                state = (new_agent, frozenset(new_boxes))
                if state not in visited:
                    visited.add(state)
                    queue.append((new_agent, frozenset(new_boxes), path + [move]))
    return None
    
solution = bfs_sokoban(grid)
print(solution)
        

        

