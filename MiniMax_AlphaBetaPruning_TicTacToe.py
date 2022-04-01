# *********************************************** #
# TIC-TAC-TOE using MINIMAX with ALPHA-BETA PRUNING #
# *********************************************** #

# Checks whether the board is full
# Is used when checking "draw condition" of end situations in minimax function
def IsBoardFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is 0:
                return False
    return True

# Analyzes board and finds out whether someone has already won or not.
def AnalyzeBoard(board):
    # Horizontal check
    for i in range (3) :
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] is not 0):
            return board[i][0]
    
    # Vertical check
    for i in range (3) :
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] is not 0):
            return board[0][i]
    
    # Diagonal
    if (board[0][0] == board[1][1] == board[2][2]) and (board[1][1] is not 0):
        return board[1][1]
    if (board[2][0] == board[1][1] == board[0][2]) and (board[1][1] is not 0):
        return board[1][1]

    # If no one won, return 0
    return 0

# Function for printing the actual state of the playing board
def PrintBoard(board):
    print()
    for i in range(3):
        for j in range(3):
            if board[i][j] is 0:
                print("-  ", end = '')
            elif board[i][j] is 1:
                print("O  ", end = '')
            else:
                print("X  ", end = '')
        print("\n")

# Takes input from human player
def UserTurn(board):
    print("Enter position (coordinates) of placing your symbol.")
    print("For example:\nto place symbol to middle right first enter \"2\" (as second row) and then \"3\" (as third column)")
    row=int(input("Enter number of the row:  "))
    col=int(input("Enter number of the column:  "))
    if(row > 3 or row < 1 or col > 3 or col < 1 or (board[row-1][col-1] is not 0)):
        print("Wrong move, bye.")
        exit(0)
    board[row-1][col-1] = -1

# Function where NPC plays its turn using minimax
def NpcTurn(board):
    bestScore = float('-inf')
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 0):              # If the place on board is not already filled
                board[i][j] = 1                 # 1 stands for NPC, (-1 for user)
                score = MiniMax(board, False, float('-inf'), float('inf'))
                board[i][j] = 0
                if (score > bestScore):
                    bestScore = score
                    bestScoreCoordX = i
                    bestScoreCoordY = j
    board[bestScoreCoordX][bestScoreCoordY] = 1

# Minimax itself
def MiniMax(board, isMaximizing, alpha, beta):
    computedResult = AnalyzeBoard(board)
    if computedResult is not 0: # If someone has on in this scenario
        if computedResult is 1: # If NPC won in this scenario (1 = NPC, -1 = User)
            return 10           # return higher number, because we are satisfied with result and want to maximize at this point
        else:
            return -10
    else:
        if IsBoardFull(board):  # If no one has one and board is full, draw (draw must have better score than loss!)
            return 0

    if (isMaximizing):
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if (board[i][j] == 0):
                    board[i][j] = 1
                    score = MiniMax(board, False, alpha, beta)
                    board[i][j] = 0     # Must return board to the state before analysing with minimax alg.
                    bestScore = max(score, bestScore)
                    # ALPHA-BETA PRUNING
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    score = MiniMax(board, True, alpha, beta)
                    board[i][j] = 0
                    bestScore = min(score, bestScore)
                    # ALPHA-BETA PRUNING
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestScore


def playTicTacToe():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    print("Compute's symbols: O\nYours symbols: X")
    firstOrSecond= int(input("Enter 1 to play first or 2 to play second: "))
    for i in range(0,9):
        if(AnalyzeBoard(board) is not 0):
            break
        if((i+firstOrSecond)%2 is 0):
            NpcTurn(board)
        else:
            PrintBoard(board)
            UserTurn(board)

    if(AnalyzeBoard(board) is 0):
         PrintBoard(board)
         print("* * * DRAW * * *")
    if(AnalyzeBoard(board) is -1):
         PrintBoard(board)
         print("* * * YOU WIN * * *")
    if(AnalyzeBoard(board) is 1):
         PrintBoard(board)
         print("* * * YOU LOSE * * *")


######## GAME ON ########
playTicTacToe()