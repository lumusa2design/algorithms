import math
from data_structures.matrix import *

def cholesky_decomposition(matrix):
    size = len(matrix)
    L = [[0.0] * size for _ in range(size)]

    for i in range(size):
        for j in range(i+1):
            sum_ = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:
                val = matrix[i][i] - sum_
                if val <= 0:
                    raise ValueError("Matrix is not positive definite")
                L[i][j] = math.sqrt(val)
            else:
                L[i][j] = (matrix[i][j] - sum_) / L[j][j]
    return L

