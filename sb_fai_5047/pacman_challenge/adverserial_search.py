import logging
import random
import numpy as np
from game import Actions, Agent, Directions
from logs.search_logger import log_function
from pacman import GameState
from util import *

def scoreEvaluationFunction(currentGameState):

    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

'''prelim test
python3 pacman.py -l layouts/q2_testClassic.lay -p Q2_Agent --timeout=30
'''

'''
python3 pacman.py -l layouts/q2_<maze>.lay -p Q2_Agent --timeout=30
'''
class Q2_Agent(Agent):

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '3'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = lookup(evalFn, globals())
        self.depth = int(depth)   
         


    @log_function
    def getAction(self, gameState: GameState):
        food = gameState.getFood()
        capsule = gameState.getCapsules()
        # FOR PRINTING AND DEBUGGING
        #print("do not run game because I'm a string?????")
        print(0.001)
        print(gameState.getPacmanPosition()) # (1,1)
        print(0.002)
        print(gameState.getGhostPositions()) # [(2,7)] one ghost
        print(00.0002)
        print(gameState.getGhostPosition(1))
        print(0.003)
        print(gameState.getCapsules()) # none
        print(0.004)
        print(gameState.getFood()) # this is a n-array of bools
        print(0.005)
        print(gameState.getNumFood()) # int
        print(0.006)
        print(gameState.getNumAgents()) # 2 agents
        print(00.007)
        print(2147483647) # largest int for python
        print(00.008)
        print(gameState.getGhostStates() is False)
        print(00.009)
        print(gameState.getCapsules())
        
        
        """
        alpha-beta applied here
            pacman: MAX
            ghosts: MIN
        
        some code pasted from my Replit app 
        other code can be attributed to the following sources:
        https://github.com/sanprab/CS188/blob/master/pj2/multiAgents.py
        https://github.com/Murf-y/pacman-minimax/blob/main/multiAgents.py
        https://inst.eecs.berkeley.edu/~cs188/sp25/projects/proj2/#q3-5-pts-alpha-beta-pruninglecture-7
        
        
       
        """
        depth = 0
        if gameState.isWin() or gameState.isLose() or self.depth == depth:
            return self.evaluationFunction(gameState), None
        
        ghost_pos = [i for i in range(1, gameState.getNumAgents())]
        
        def min_turn(state, d, ghost):
            if gameState.isWin() or gameState.isLose() or self.depth == depth:
                return self.evaluationFunction(gameState), None

            MAXINT = 2147483647
            for action in gameState.getLegalActions(ghost):
                if ghost == ghost_pos[-1]:
                    MAXINT = min(MAXINT, max(gameState.generteSucessor(ghost, action), d, ghost +1))
                else:
                    MAXINT = max()
        
        def max_turn(state, d, alpha, beta):
            if state.isWin() or state.isLose() or depth == depth:
                return self.evaluationFunction(state)
            value = -np.inf
            legal_actions = state.getLegalActions(0)  
            
            for action in legal_actions:
                successor = state.generateSuccessor(0, action)
                value = max(value, min_value(successor, depth, 1, alpha, beta))
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value

        def min_value(state, depth, agent_index, alpha, beta):
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)
                
            value = np.inf
            legal_actions = state.getLegalActions(agent_index)
            
            for action in legal_actions:
                successor = state.generateSuccessor(agent_index, action)
                if agent_index == state.getNumAgents() - 1:  # Last ghost
                    value = min(value, max_value(successor, depth - 1, alpha, beta))
                else:
                    value = min(value, min_value(successor, depth, agent_index + 1, alpha, beta))
                
                if value < alpha:
                    return value
                beta = min(beta, value)
            return value    
        
        def max_value(state, depth, alpha, beta):
            if state.isWin() or state.isLose() or depth == 0:
                return self.evaluationFunction(state)
            
            value = -np.inf
            legal_actions = state.getLegalActions(0)  # Pacman's actions
            
            for action in legal_actions:
                successor = state.generateSuccessor(0, action)
                value = max(value, min_value(successor, depth, 1, alpha, beta))
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value
        
        score = gameState.getScore()
        food_list = food.asList()
        if capsule:
            '''TODO: use block to create capsule rule
            # Eat capsule
        if( position in state.getCapsules() ):
            state.data.capsules.remove( position )
            state.data._capsuleEaten = position
            # Reset all ghosts' scared timers
            for index in range( 1, len( state.data.agentStates ) ):
                state.data.agentStates[index].scaredTimer = SCARED_TIME
        consume = staticmethod( consume )
            '''
            
        if food_list:
            closest_food = min(manhattanDistance(gameState.getPacmanPosition(), f) for f in food_list)
            food_bonus = 20.0 / (closest_food + 1)  # +1 to avoid division by zero
            score += food_bonus
        # n_ghost = 0    
        for ghostx in gameState.getGhostPositions():
            # for successor, action, step_cost in  problem.getSuccessors(c_state):
                # hn = min(manhattanDistance(successor, food) for food in astarData.food_positions)
            #cap_dist = manhattanDistance(gameState.getPacmanPosition(), capsule[1])
            dist = manhattanDistance(gameState.getPacmanPosition(), gameState.getGhostPosition(1)) # for some reason, if 1 -> testMaze doesn't work, else it works
            #n_ghost += 1
            # true := scared shosts
            if gameState.getGhostState is True > 0: 
                score += 20.0 / (dist + 1)
            elif dist < 3:  # Danger zone
                score -= 40.0 / (dist + 1)    
        
        best_score = -np.inf
        beta = np.inf
        # best move, ceterus paribus, is to not
        best_action = Directions.STOP
        legal_actions = gameState.getLegalActions(0)
        
        for action in legal_actions:
            successor = gameState.generateSuccessor(0, action)
            score = min_value(successor, self.depth, 1, best_score, beta)
            
            if score > best_score:
                best_score = score
                best_action = action
                
        return best_action
        
        
        
        
        
        
        '''TODO
        1) get game data
            1.1) pacman pos
            1.2) ghost pos
            1.3) number of food
            1.4) maze
        2) pacman goes first
            2.1) implement modified dfs
        3) ghosts go second
            2.1) implement 
            
            
        '''
        
        
        
        
        
        
        
        
        logger = logging.getLogger('root')
        logger.info('MinimaxAgent')
        "*** YOUR CODE HERE ***"
        raiseNotDefined()
        
        """
    Returns the minimax action from the current gameState using self.depth
    and self.evaluationFunction.

     Here are some method calls that might be useful when implementing minimax.

     gameState.getLegalActions(agentIndex):
    Returns a list of legal actions for an agent
    agentIndex=0 means Pacman, ghosts are >= 1

     gameState.generateSuccessor(agentIndex, action):
    Returns the successor game state after an agent takes an action

     gameState.getNumAgents():
    Returns the total number of agents in the game
"""
