class Agent:
    def __init__(self):
        total_rewards = 0
        actions = {"North": (1,1), "South": (2,2), "East": (2,1), "West": (1,2)}
        goal_state = ([24])
        
    def init_agent(self):
        self.dy = 0
        self.dx = 0
        agent_poisition = (self.dy,self.dx)
        #print(agent_poisition)
        return agent_poisition