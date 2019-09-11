
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
            if board[i][j]==0:
                return (i,j)
    return None
# checks if the 3x3 square doesnt contain a given number
def is_box_valid(board,row,column,number):
    # gets the x and y position of the 3x3 square
    row_offset = row//3
    column_offset = column//3

    # loops through 3x3 square
    for i in range(row_offset*3,row_offset*3+3):
        for j in range(column_offset*3,column_offset*3+3):
            if board[i][j] == number:
                return False
    return True


# algorithm for solving sudoku

def backtrack(board):
    # gets the first empty square
    empty_square = get_empty_square(board)
    # if all squares are not empty our board is solved
    if empty_square == None:
        return True
    row = empty_square[0]
    column = empty_square[1]

    # checks every number from 1 to 9 if it fits for the given square
    for i in range(1,10):
        if is_row_valid(board,row,i) and is_column_valid(board,column,i) and is_box_valid(board,row,column,i):
            board[row][column] = i
            if backtrack(board):
                return True
            board[row][column] = 0

    return False

# reads from file into a 2D board
def read_from_file(board):
    file  = open("testCase.txt","r")
    for line in file.readlines():
        board.append([int(num)for num in line.split(",")])


board = []
read_from_file(board)
backtrack(board)
print_board(board)
    

