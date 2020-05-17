#Sudoku solver
import time

board = [[8, "_", "_", "_", "_", "_", "_", "_", "_"],  # unsolved sudoku board
         ["_", "_", 3, 6, "_", "_", "_", "_", "_"],
         ["_", 7, "_", "_", 9, "_", 2, "_", "_"],
         ["_", 5, "_", "_", "_", 7, "_", "_", "_"],
         ["_", "_", "_", "_", 4, 5, 7, "_", "_"],
         ["_", "_", "_", 1, "_", "_", "_", 3, "_"],
         ["_", "_", 1, "_", "_", "_", "_", 6, 8],
         ["_", "_", 8, 5, "_", "_", "_", 1, "_"],
         ["_", 9, "_", "_", "_", "_", 4, "_", "_"]]
print("   " * 5, "SUDOKU SOLVER", "\n" * 2)


def print_board():  # displaying sudoku board
    for i in range(9):
        if ((i % 3) == 0 and i != 0):
            print(" --- --- --- --- --- --- --- --- ---")
        print(" " * 3, end="")
        for j in range(9):
            if (j % 3 == 0 and j != 0):
                print(" | ", end="")
            print(board[i][j], end="  ")
        print("\n")


print_board()
print("\n" * 2)


def locate_empty():  # locating blanks
    for i in range(9):
        for j in range(9):
            if (board[i][j] == "_"):
                return ((i, j))
    return (None)


def check_validity(option, position):  # checking validity of a no. to be filled in the blank
    i = position[0]
    j = position[1]
    for k in range(9):
        if (board[i][k] == option and j != k) or (
                board[k][j] == option and i != k):  # checking same row and same column validity
            return (False)

    subgrid_x = j // 3
    subgrid_y = i // 3
    for m in range(subgrid_y * 3, (subgrid_y * 3) + 3):  # checking subgrid validity
        for n in range(subgrid_x * 3, (subgrid_x * 3) + 3):
            if (option == board[m][n] and (m, n) != (i, j)):
                return (False)
    return (True)


def solve_sudoku():  # solving the unsolved sudoku board
    location = locate_empty()
    if (location == None):
        return (True)
    else:
        (row, col) = location
    for option in range(1, 10):
        if check_validity(option, (row, col)):
            board[row][col] = option
            if (solve_sudoku()):  # as long as the board can be solved further, we perfom recursion
                return (True)
            board[row][col] = "_"  # if we fail to fill a blank, we make the previous blank that was filled empty again
            # or simply backtrack


start = time.time()
solve_sudoku()
end = time.time()
time_elapse = end - start  # calculating time taken to solve the board
print_board()
print(time_elapse, " seconds elapsed")



