# Helper function to find an empty cell in the puzzle
def find_empty_location(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None

# Helper function to check if a move is valid in a Sudoku puzzle
def is_valid(puzzle, row, col, num):
    # Check row
    for x in range(9):
        if puzzle[row][x] == num:
            return False
    
    # Check column
    for x in range(9):
        if puzzle[x][col] == num:
            return False
    
    # Check subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False
    
    return True

# Recursive function to solve Sudoku using RBFS algorithm
def solve_sudoku(puzzle):
    row, col = find_empty_location(puzzle)

    if row is None:
        return True

    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num

            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = 0

    return False

# Example puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(puzzle):
    print("Sudoku puzzle solved:")
    for row in puzzle:
        print(row)
else:
    print("No solution exists.")
