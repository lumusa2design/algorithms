def conjugate_gradient_method(A, b, x0, tol=1e-10, max_iter=1000):
    import numpy as np

    x = np.array(x0, dtype=float)
    r = b - A @ x  # Residual
    p = r.copy()  # Initial search direction
    rs_old = r.T @ r

    for i in range(max_iter):
        Ap = A @ p  # Matrix-vector product
        alpha = rs_old / (p.T @ Ap)  # Step size
        x += alpha * p  # Update solution
        r -= alpha * Ap  # Update residual
        rs_new = r.T @ r  # New residual squared norm

        if np.sqrt(rs_new) < tol:  # Check for convergence
            print(f'Convergence achieved after {i+1} iterations.')
            break

        p = r + (rs_new / rs_old) * p  # Update search direction
        rs_old = rs_new  # Update for next iteration

    return x