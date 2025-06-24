class Episodes:
    def __init__(self):
        pass
    def setup_episode(self):
         # Random A and B locations where A != B
         coords = list(self.grid_world)
         self.a = RD.choice(coords)
         self.b = RD.choice(coords)
         while self.a == self.b:
             self.b = RD.choice(coords)
         
         # Agents start at A or B, with opposite as goal
         self.agent_positions = []
         self.goal_positions = []
         for _ in range(self.num_agents):
             start = RD.choice([self.a, self.b])
             goal = self.b if start == self.a else self.a
             self.agent_positions.append(start)
             self.goal_positions.append(goal)
