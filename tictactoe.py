"""
Tic Tac Toe Player
"""
import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#count number of Xs in the board and as X starts when x numbeer = O number then it will be X's round so no need to if(X==O)
def countXandO(board):
    countX=0
    countO = 0
    for row in board:
        for cell in row:
            if(cell==X):
                countX+=1
            elif (cell==O):
                countO += 1
    if(countX>countO):
         return O
    else:
        return X


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if(board==initial_state()):
        return X
    else:
        return countXandO(board)
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    freeCells=[]
    for i in  range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==EMPTY):
                freeCells.append((i,j))
    return freeCells

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    fakeBoard=copy.deepcopy(board)
    i,j=action
    if(fakeBoard[i][j]==EMPTY):
        fakeBoard[i][j]=player(board)
        return fakeBoard
    else:
        print("not an empty place")
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #horizontal

    for row in board:
        if(row==[O,O,O]):
            return O
        elif (row==[X,X,X]):
            return X

    # vertical
    for j in range(len(board)):
        if(board[1][j]==board[0][j] and board[2][j]==board[0][j] and board[0][j]==O):
            return O
        elif (board[1][j] == board[0][j] and board[2][j] == board[0][j] and board[0][j] ==X):
            return X

    # diagonal
    if((board[0][0]==board[2][2] and board[0][0]==board[1][1] and board[0][0]==O)
           or(board[0][2]==board[2][0] and board[2][0]==board[1][1] and  board[1][1]==O)):
            return O
    if ((board[0][0] == board[2][2] and board[0][0] == board[1][1] and board[0][0] == X)
          or (board[0][2] == board[2][0] and board[2][0] == board[1][1] and board[1][1] == X)):
            return X

    return  None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    gameEnded=True
    win=winner(board)
    if(win==X or win==O):
        return gameEnded
    for i in  range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==EMPTY):
                gameEnded=False
                break

    return gameEnded
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(terminal(board)==True):
        win=winner(board)
        if (win == X):
            return 1
        elif(win == O):
            return -1
        else:
            return 0
    #raise NotImplementedError



def minimax(board):
    '''
    Returns the optimal action for the current player on the board.
    '''
    #print(board)
    if (terminal(board) == True):
        return None
    if player(board) == X:
        _,bestMove = MAX_VALUE(board)
        return bestMove
    elif player(board) == O:
        v,bestMove = MIN_VALUE(board)
        return bestMove
        #return MIN_VALUE(board)

    #raise NotImplementedError

def MAX_VALUE(board):
    if terminal(board):
        return utility(board),None
    v = -math.inf
    bestMove = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        bestValue,_ = MIN_VALUE(result(board, action))
        if bestValue > v:
            v = bestValue
            bestMove = action
            if v >= 1:
                return  v,bestMove
    return  v,bestMove




def MIN_VALUE(board):
    if terminal(board):
        return utility(board),None
    v = math.inf
    bestMove = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        bestvalue,_ = MAX_VALUE(result(board, action))
        if bestvalue < v:
            v = bestvalue
            bestMove = action
            if v <= -1:
                return  v,bestMove

    return v,bestMove

