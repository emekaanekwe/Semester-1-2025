from collections import deque

def func_with___doc__():
     "This is an implementation of breadth-first search"
     pass
 

func_with___doc__.__doc__
'This function has a docstring.'
help(func_with___doc__)

func_with___doc__()



# Example grid
grid = [
    ["S", ".", ".", "."],
    ["#", "#", ".", "#"],
    [".", ".", ".", "G"]
]

# Directions for movement (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Find the start and goal positions
start = goal = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            start = (r, c)
        elif grid[r][c] == "G":
            goal = (r, c)

'''this is a learning note'''
def bfs(grid, start, goal):
    queue = deque([(start, [])])  # (position, path to this position)
    visited = set([start])  # Track visited states
    
    while queue:
        (x, y), path = queue.popleft()
        
        # Goal check
        if (x, y) == goal:
            return path
        
        # Try all possible moves
        for dr, dc in directions:
            nx, ny = x + dr, y + dc
            
            # Check grid boundaries and wall collisions
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None

# Run BFS
path = bfs(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
