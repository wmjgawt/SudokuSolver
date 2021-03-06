from __future__ import print_function

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# 9 x 9 sudoku grid

row = 0
col = 0
print()
print ("You will now be asked to input the numbers (0-9) on the sudoku grid for your sudoku problem.")
print ("You will be asked to input the numbers by each row, staring at the first row and ending at the ninth row.")
print ("Please input numbers from left to right and enter 0 for any squares that are blank.")
print ("For example, 800000000 would be a valid entry for a sudoku problem with a first row only consisting of an 8 in the first column")
print()


def make_grid():
    for i in range(9):
        line = str(raw_input("Enter the numbers in row " + (str(i+1) + " of the sudoku problem >>> ")))
        if len(line) != 9:
            print("Invalid input. Each entry must contain exactly 9 numbers.")
            exit()
        else:
            for j in range(9):
                grid[i][j] = int(line[j])
            line = ''


make_grid()
# Takes user input for every square of the grid. 0 is entered if square is blank.


def possible(grid, row, col, number):
    # Ensures that number is a possible option in empty square
    for a in range(9):
        if grid[row][a] == number:
            return False
    # Returns false if number already exists within row
    for a in range(9):
        if grid[a][col] == number:
            return False
    # Returns false if number already exists within column
    box_row = row - row % 3
    box_col = col - col % 3
    for a in range(3):
        for b in range(3):
            if grid[box_row + a][box_col + b] == number:
                return False
    # Returns false if number already exists within the same 3x3 box
    return True
    # Returns True if number is a valid option to fill in a square


def sol(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row = row + 1
        col = 0
    # Moves on to next row once column is full.
    if grid[row][col] > 0:
        return sol(grid, row, col + 1)
    # Moves on to next square in column if spot is already has a number

    for num in range(1, 10):
        # Loop checks all numbers from 0 - 9
        if possible(grid, row, col, num):
            grid[row][col] = num
            # Sets empty square to num if num is a possible option
            if sol(grid, row, col + 1):
                return True
            # Returns true if number is the solution.(Backtracking)
        grid[row][col] = 0
        # If num is not the solution, it sets the empty square back to 0
    return False
    # If num is not the solution, it returns false for num


if sol(grid, 0, 0):
    print()
    print ("Solution: ")
    print()
    for i in range(9):
        for j in range(9):
            print (grid[i][j], end='  ')
        print ()
# Prints grid if sudoku is solved
else:
    print ("This sudoku problem is not solvable")
# Prints if sudoku has no solution
