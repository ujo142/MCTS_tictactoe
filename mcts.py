""" MCTS algorithm implementation """

import math
import random
from tree_node import TreeNode

# MCTS class
class MCTS():
    # search for best move in the current position
    def search(self, initial_state):
        # create root node
        self.root = TreeNode(initial_state, None)
        
        # walk through 1000 iterations
        for iteration in range(1000):
            # select a node (1. selection phase)
            node = self.select(self.root)
            
            # score current node (2. simulation phase)
            score = self.rollout(node.board)
            
            # backpropagate the number of visits and 
            # score up to the root node (3. backpropagation phase)
            self.backpropagate(node, score)
        
        # pick up the best moove in the current position
        try:
            return self.get_best_move(self.root, 0)
        except:
            print("Error: no best move found")
            
    # select most promising node 
    # (1. selection phase)
    def select(self, node):
        # make sure we are dealing with non-terminal nodes
        while not node.is_terminal:
            # case 1: node is  fully expanded
            if node.is_fully_expanded:
                # select the best child node
                node = self.get_best_move(node, 2)
                
            # case 2: node is not fully expanded
            else:
                # oterwise expand the node
                return self.expand(node)
        
        # return terminal node
        return node
    
    # expand the node
    def expand(self, node):
        # generate all possible next states for the given node
        states = node.board.generate_states()
        
        # loop over generated states (moves)
        for state in states:
            # make sure that current state is not among node's children
            if  str(state.position) not in node.children:
                # create a new child node
                new_node = TreeNode(state, node)
                
                # add child node to parent's node children list (dict) n
                node.children[str(state.position)] = new_node
                
                # case when node is fully expanded
                if len(states) == len(node.children):
                    node.is_fully_expanded = True
                
                # return newly created node
                return new_node
        
    # simulate the game from the current position via random moves
    # (2. simulation phase)
    def rollout(self, board):
        # make random moves for both sides until game is over
        while not board.is_win() and not board.is_draw():
            # try to make a move
            try:
                # make the move on board
                board = random.choice(board.generate_states())
                
            # no moves available
            except:
                print('Game drawn!')
                
                # return drawn score
                return 0
        
        
        # return score from the player 'x' perspective
        if board.player_2 == 'x': return 1
        elif board.player_2 == 'o': return -1
    
    # backprogagate the number of visits and score up to the root node
    # (3. backpropagation phase)
    def backpropagate(self, node, score):
        # update nodes's up to root node
        while node is not None:
            # update node's visits
            node.visits += 1
            
            # update node's score
            node.score += score
            
            # set node to parent
            node = node.parent
    
    # select the best node basing on UCB1 formula (not UCT)
    def get_best_move(self, node, exploration_constant):
        # define best score & best move
        best_score = float("-inf")
        best_moves = []
        
        # loop over child nodes
        for child_node in node.children.values():
            # define current player
            if child_node.board.player_2 == 'x': current_player = 1
            elif child_node.board.player_2 == 'o': current_player = - 1
            
            # get move score using UCT formula
            move_score = current_player * child_node.score /  \
                         child_node.visits + exploration_constant *  \
                         math.sqrt(math.log(node.visits) /  \
                         child_node.visits)
            
            # best move has been found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]
            
            # found as good move as already available
            elif move_score == best_score:
                best_moves.append(child_node)
                
            # return one of the best moves randomly
            return random.choice(best_moves)