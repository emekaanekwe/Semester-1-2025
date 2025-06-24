class Q_Function:
    def __init__(self):
        # Q-tables: [agent_x, agent_y, goal_x, goal_y, action]
        self.q_tables = [np.zeros((grid_size, grid_size, grid_size, grid_size, 4)) 
                        for _ in range(self.num_agents)]
        