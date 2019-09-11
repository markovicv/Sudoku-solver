sudoku_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end=" ")
        print("")

# checks if a given row contains the given number,if it contains the function returns False
def is_row_valid(board,row,number):
    for i in range(len(board)):
        if board[row][i] == number:
            return False
    return True

# checks if a given colum contains the given number,if it contains the function returns Flase
def is_column_valid(board,column,number):
    for i in range(len(board)):
        if board[i][column] == number:
            return False
    return True

# returns first empty square
def get_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[row][col]==0:
                return (i,j)
    return None

def backtrack(board):
    empty_square = get_empty_square(board):
    if not empty_square:
        return True
    row = empty_square[0]
    column = empty_square[1]

    for i in range(10):
        if is_row_valid(board,row,i) and is_column_valid(board,column,i) and is_box_valid(board,row,column,i):
            board[row][column] = i
            if backtrack(board):
                return True
            board[row][column] = 0

    return False

