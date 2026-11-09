# Part A - 6: Sudoku Solver using Backtracking
def solve(b):
    for r in range(9):
        for c in range(9):
            if b[r][c] == 0:
                for n in range(1, 10):
                    if all(b[r][i] != n and b[i][c] != n and 
                           b[3*(r//3) + i//3][3*(c//3) + i%3] != n for i in range(9)):
                        b[r][c] = n
                        if solve(b):
                            return True
                        b[r][c] = 0
                return False
    return True

grid = [
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

if solve(grid):
    print("Sudoku Solved:")
    for row in grid:
        print(row)
