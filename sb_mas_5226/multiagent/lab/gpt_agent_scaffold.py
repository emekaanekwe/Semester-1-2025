import numpy as np
import mdptoolbox.example

# generate a MDP based on forest management
#P, R = mdptoolbox.example.rand()
"""generate MDP based on forest management
    generates a transition Pr matrix and a reward matrix 
Returns:
    _type_: _description_
"""


#vi = mdptoolbox.mdp.ValueIteration(P, R, 0.9)

class Agent:
    def __init__(self, possible_states, num_actions, transition_matrix, reward_matrix, policy):
        self.possible_states = possible_states  # How many places the agent can be in
        self.num_actions = num_actions  # How many choices the agent can make
        self.transition_matrix = transition_matrix  # Rules of movement
        self.reward_matrix = reward_matrix  # Points the agent gets for actions
        self.policy = policy  # Agent's way of choosing actions
        self.state = 0  # The agent starts in the first place
    
    def choose_action(self):
        return self.policy[self.state]  # Follows the policy for the current state
    
    def step(self):
        action = self.choose_action()  # Pick an action based on the policy
        probabilities = self.transition_matrix[self.state][action]  # Get movement rules
        self.state = np.random.choice(self.num_states, p=probabilities)  # Move to a new state
        reward = self.reward_matrix[self.state]  # Get the reward for the new state
        return self.state, reward  # Return where the agent is now and its reward

# Example of setting up an environment
num_states = 3  # Three places the agent can be in
num_actions = 2  # Two choices at each place

# Transition matrix: action determines probability of moving to each state
transition_matrix = np.array([
    [[0.8, 0.2, 0.0], [0.1, 0.7, 0.2]],  # State 0
    [[0.2, 0.6, 0.2], [0.3, 0.3, 0.4]],  # State 1
    [[0.0, 0.3, 0.7], [0.5, 0.3, 0.2]]   # State 2
])

# Reward matrix: points agent gets in each state
reward_matrix = np.array([1, -1, 2])  # State 0 gives 1 point, etc.

# Policy: which action to take in each state
policy = [0, 1, 0]  # In state 0, take action 0, in state 1, take action 1, etc.

agent = Agent(num_states, num_actions, transition_matrix, reward_matrix, policy)

# Let the agent take some steps in the environment
for _ in range(5):
    state, reward = agent.step()
    print(f"Agent moved to state {state} and received reward {reward}")
