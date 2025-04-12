from util import PriorityQueue  # Berkeley's priority queue implementation

def aStarSearch(problem, heuristic):
    """
    A* search for Pacman.
    :param problem: A SearchProblem instance (e.g., PositionSearchProblem in Berkeley's Pacman).
    :param heuristic: A function to estimate cost-to-goal (e.g., manhattanDistance).
    :return: List of actions to reach the goal.
    """
    # Initialize data structures
    start_state = problem.getStartState()
    frontier = PriorityQueue()  # Priority: f(n) = g(n) + h(n)
    frontier.push((start_state, [], 0), 0)  # (state, actions, cost), priority
    explored = set()  # Visited states

    while not frontier.isEmpty():
        current_state, actions, current_cost = frontier.pop()

        if problem.isGoalState(current_state):
            return actions  # Found the goal!

        if current_state not in explored:
            explored.add(current_state)

            for successor, action, step_cost in problem.getSuccessors(current_state):
                new_actions = actions + [action]
                new_cost = current_cost + step_cost
                priority = new_cost + heuristic(successor, problem)
                frontier.push((successor, new_actions, new_cost), priority)

    return []  # No solution found