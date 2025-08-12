from copy import deepcopy
from data_structures.matrix import *

def gauss_jordan(matrix,eps=1e-12 ):
    A = deepcopy(matrix)
    n_rows, pivot, pivots = len(A), 0, []
    n_cols = len(A[0]) if n_rows else 0

    for col in range(n_cols):
        pivote_row = max(range(pivot, n_rows), key=lambda i: abs(A[i][col]))
        if abs(A[pivote_row][col]) < eps:
            continue

        if pivote_row != pivot:
            A[pivot], A[pivote_row] = A[pivote_row], A[pivot]
        piv = A[pivot][col]
        for j in range(col, n_cols):
            A[pivot][j] /= piv

        for i in range(n_rows):
            if i == pivot:
                continue
            factor = A[i][col]
            if abs(factor) > eps:
                for j in range(col, n_cols):
                    A[i][j] -=  factor * A[pivot][j]

        pivots.append(col)
        pivot += 1
        if pivot == n_rows:
            break

    for i in range(n_rows):
        for j in range(n_cols):
            if abs(A[i][j]) < eps:
                A[i][j] = 0.0
    rank = len(pivots)
    return A, rank, pivots

arr = create_matrix(3, 4)
R, rank, pivots = gauss_jordan(arr)
print("RREF final:")
print(R)

