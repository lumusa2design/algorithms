import time
import os

def nqueens(size, delay=0.2):
    chess = [[0 for _ in range(size)] for _ in range(size)]
    results = [0]
    solve(chess, 0, size, results, delay)
    print(f'Total solutions: {results[0]}')

def solve(chess, row, size, results, delay):
    if row == size:
        results[0] += 1
        print(f'--- Solution #{results[0]} ---')
        print_board(chess)
        time.sleep(1)
        return

    for col in range(size):
        chess[row][col] = 1
        clear_console()
        print(f'Trying row {row}, col {col}')
        print_board(chess)
        time.sleep(delay)

        if is_positionable(chess, row, col, size):
            solve(chess, row + 1, size, results, delay)
        # Backtrack
        chess[row][col] = 0
        clear_console()
        print(f'Backtracking from row {row}, col {col}')
        print_board(chess)
        time.sleep(delay)

def is_positionable(chess, row, col, size):
    for i in range(row):
        if chess[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if chess[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < size:
        if chess[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def print_board(chess):
    for row in chess:
        print(" ".join("♛" if cell else "·" for cell in row))
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

nqueens(8, delay=0.6)
