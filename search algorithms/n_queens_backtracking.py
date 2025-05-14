def nqueens(size):
    chess = [[0 for _ in range(size)] for _ in range(size)]
    print(chess)
    solve(chess, 0, size)

def solve(chess, row, size):
    if row == size:
        print(chess)
        return

    for col in range(size):
        if is_positionable(chess, row, col, size):
            chess[row][col] = 1
            solve(chess, row + 1, size)
            chess[row][col] = 0



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


nqueens(7)