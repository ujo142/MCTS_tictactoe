class TreeNode():
    # class constructor
    def __init__(self, board, parent):
        # init associated board state
        self.board = board

        # init is node terminal flag
        if self.board.is_win() or self.board.is_draw():
            self.is_terminal = True
        else:
            # we have a non-terminal node
            self.is_terminal = False
        
        # init is fully exanded flag
        self.is_fully_expanded = self.is_terminal
        
        # init parent node if available
        self.parent = parent
        
        # init the numer of visits
        self.visits = 0
        
        # init the total reward of the node
        self.score = 0
        
        # init current node's children
        self.children = {}
