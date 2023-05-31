from copy import deepcopy




# Tic Tac Toe board class
class Board():
    # init board class instance
    def __init__(self, board=None):
        # define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_square = '.'
        # define board position
        self.position = {}
        
        # init (reset) board
        self.init_board()
        
        # create a copy of a previous board state if available
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)

    # init (reset) board
    def init_board(self):
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # set every board square to empty
                self.position[row, col] = self.empty_square
            
    # init (reset) board
    def __str__(self):
        # define board string representation
        board_str = ''
        
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # set position to empty
                board_str += ' %s' % self.position[row, col]
            
            # print new line every row
            board_str += '\n'
            
        # prepand side to move
        if self.player_1 == 'x':
            board_str = '\n ----------------- \n x to move \n ----------------- \n\n' + board_str
        elif self.player_1 == 'o':
            board_str = '\n ----------------- \n o to move \n ----------------- \n\n' + board_str
        
        # return board string representation
        return board_str
        
    # make move
    def make_move(self, row, col):
        # create new board instnace that inherites from the current board 
        board = Board(self)
        
        # make move
        board.position[row, col] = self.player_1
        
        # switch players
        (board.player_1, board.player_2) = (board.player_2, board.player_1)
        
        # return new board state
        return board
    
    def is_draw(self):
        #loop over board squares
        for row, col in self.position:
            # empty square found
            if self.position[row, col] == self.empty_square:
                return False
        
        # by default return True
        return True
    
    # get whether the game is won
    def is_win(self):#
        #############################
        # vertival sequence check
        #############################
        
        # loop over board columns
        for col in range(3):
            # define winning sequence list
            winning_sequence = []
            
            # loop over board rows
            for row in range(3):
                # if found same next element in the row
                if self.position[row, col] == self.player_2:
                    # upadte winning sequence
                    winning_sequence.append((row, col))
                # if we have 3 elements in the row
                if len(winning_sequence) == 3:
                    # return wining state
                    return True 
                
        #############################
        # horizontal sequence check
        #############################
        
        # loop over board rows
        for row in range(3):
            # define winning sequence
            winning_sequence = []
            
            # loop over board columns
            for col in range(3):
                # if found same nex element in the column
                if self.position[row, col] == self.player_2:
                    # update winning sequence
                    winning_sequence.append((row, col))
                
                # if we have 3 elements in the row
                if len(winning_sequence) == 3:
                    # return wining state
                    return True
                
        #############################
        # 1st diagonal sequence check
        #############################
        winning_sequence = []
        # loop over board rows
        for row in range(3):
            # define winning sequence
            
            col = row 
            
            # if found same nex element in the column
            if self.position[row, col] == self.player_2:
                # update winning sequence
                winning_sequence.append((row, col))
            
            # if we have 3 elements in the row
            if len(winning_sequence) == 3:
                # return wining state
                return True
        #############################
        # 2st diagonal sequence check
        #############################
        
        # define winning sequence list
        winning_sequence = []
        
        # loop over board rows
        for row in range(3):
            # init column
            col = 3 - row - 1
        
            # if found same next element in the row
            if self.position[row, col] == self.player_2:
                # update winning sequence
                winning_sequence.append((row, col))
                
            # if we have 3 elements in the row
            if len(winning_sequence) == 3:
                # return the game is won state
                return True
        
        # by default return False
        return False
        
    # generate legal movesto play in the current position
    def generate_states(self):
        # define states list (moves list - list of available actions to consider)
        actions = []
        
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # make sure the square is empty
                if self.position[row, col] == self.empty_square:
                    # append legal move to the list
                    actions.append(self.make_move(row, col))
        
        # return list of available actions (board class instances)
        return actions
        
        
        
        
        
        
if __name__ == '__main__':
    # create board instance
    board = Board()
    print('this is initial board state')
    print(board)

    # generte available actions
    actions = board.generate_states()
    
    # loop over generated actions
    for action in actions:
        # print action
        print(action)
        
    # take action (make move on board)
    board = actions[0]
    
    # print updated board
    print('First generated move had been made on bord:')
    print(board)