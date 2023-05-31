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
        # create new board instnace
        board = Board()
        
        # make move
        board.position[row-1, col-1] = self.player_1
        
        # switch players
        (board.player_1, board.player_2) = (board.player_2, board.player_1)
        
        # return new board state
        return board
    
    


if __name__ == '__main__':
    # create board instance
    board = Board()

    # make move on board
    print(board)
    board = board.make_move(1, 1)
    print(board)
    board = board.make_move(2, 3)
    print(board)
    