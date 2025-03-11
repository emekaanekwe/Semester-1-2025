# Implementation of Breadth First Search (BFS) algorithm for 8-puzzle problem

from collections import deque
'''
Note that state space concern is the entire set of possible nodes that can be traversed

'''
def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])  # (state, path)
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path  # Return the sequence of moves
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))

        # Generate possible moves
        zero_row, zero_col = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                new_state = [row[:] for row in state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                queue.append((new_state, path + [(new_row, new_col)]))

    return None  # No solution found

