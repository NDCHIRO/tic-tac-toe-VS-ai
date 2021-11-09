from tictactoe import initial_state,player,actions,result,winner,terminal,utility,minimax
X = "X"
O = "O"
EMPTY = None
board =[[X, X,O],
        [O, O, EMPTY],
        [X, EMPTY, O]]

#print(player(board))
#print(actions(board))
#action=(2,0)
#print(result(board,action))
#print(winner(board))
#print(terminal(board))
#print(utility(board))
#print(MAX_VALUE(5,3))
minimax(board)