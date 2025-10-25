import numpy as np
import itertools

def nash_equilibria(A, B, search_mixed=True):
    A, B = np.array(A, dtype=float), np.array(B, dtype=float)
    m, n = A.shape
    if B.shape != (m, n):
        raise ValueError("Las matrices A y B deben tener el mismo tamaño")

    equilibrios = []

    for i in range(m):
        for j in range(n):
            pago_j1_actual = A[i, j]
            mejor_p_j1 = np.max(A[:, j])
            pago_j2_actual = B[i, j]
            mejor_p_j2 = np.max(B[i, :])
            if np.isclose(pago_j1_actual, mejor_p_j1) and np.isclose(pago_j2_actual, mejor_p_j2):
                x = np.zeros(m)
                y = np.zeros(n)
                x[i] = 1
                y[j] = 1
                equilibrio = {
                    "x": x,
                    "y": y,
                    "type": "pure",
                    "support": ((i,), (j,)),
                    "values": (pago_j1_actual, pago_j2_actual)
                }
                equilibrios.append(equilibrio)

    if search_mixed:
        for k in range(1, min(m, n) + 1):
            for S in itertools.combinations(range(m), k):
                for T in itertools.combinations(range(n), k):
                    A_ST = A[np.ix_(S, T)]
                    B_ST = B[np.ix_(S, T)]
                    M_y = np.zeros((k + 1, k + 1))
                    rhs_y = np.zeros(k + 1)

                    for r in range(k):
                        for c in range(k):
                            M_y[r, c] = A_ST[r, c]
                        M_y[r, -1] = -1

                    for c in range(k):
                        M_y[-1, c] = 1
                    rhs_y[-1] = 1

                    try:
                        sol_y = np.linalg.solve(M_y, rhs_y)
                    except np.linalg.LinAlgError:
                        continue

                    y_T = sol_y[:k]
                    v1 = sol_y[-1]
                    M_x = np.zeros((k + 1, k + 1))
                    rhs_x = np.zeros(k + 1)

                    for r in range(k):
                        for c in range(k):
                            M_x[r, c] = B_ST[c, r]
                        M_x[r, -1] = -1

                    for c in range(k):
                        M_x[-1, c] = 1
                    rhs_x[-1] = 1

                    try:
                        sol_x = np.linalg.solve(M_x, rhs_x)
                    except np.linalg.LinAlgError:
                        continue

                    x_S = sol_x[:k]
                    w2 = sol_x[-1]

                    if np.any(x_S < -1e-8) or np.any(y_T < -1e-8):
                        continue
                    x_S[x_S < 0] = 0
                    y_T[y_T < 0] = 0
                    x_S = x_S / np.sum(x_S)
                    y_T = y_T / np.sum(y_T)
                    x = np.zeros(m)
                    y = np.zeros(n)
                    for idx, i in enumerate(S):
                        x[i] = x_S[idx]
                    for idx, j in enumerate(T):
                        y[j] = y_T[idx]

                    Ay = A @ y
                    xTB = x @ B
                    Ay_support = Ay[list(S)]
                    xTB_support = xTB[list(T)]

                    if not np.allclose(Ay_support, v1, atol=1e-6):
                        continue
                    if not np.allclose(xTB_support, w2, atol=1e-6):
                        continue
                    fuera_S = [i for i in range(m) if i not in S]
                    fuera_T = [j for j in range(n) if j not in T]
                    hay_mejor_fila = any(Ay[i] > v1 + 1e-6 for i in fuera_S)
                    hay_mejor_columna = any(xTB[j] > w2 + 1e-6 for j in fuera_T)
                    if hay_mejor_fila or hay_mejor_columna:
                        continue

                    tipo = "mixed"
                    if np.count_nonzero(x) == 1 and np.count_nonzero(y) == 1:
                        tipo = "pure"

                    equilibrio = {
                        "x": x,
                        "y": y,
                        "type": tipo,
                        "support": (S, T),
                        "values": (v1, w2)
                    }

                    repetido = False
                    for e in equilibrios:
                        if np.allclose(e["x"], x, atol=1e-6) and np.allclose(e["y"], y, atol=1e-6):
                            repetido = True
                            break

                    if not repetido:
                        equilibrios.append(equilibrio)

    return equilibrios
