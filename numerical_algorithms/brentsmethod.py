import math

def brent_root(f, a, b, tol=1e-12, maxit=100):
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        raise ValueError("El intervalo [a,b] no encierra una raíz (no hay cambio de signo).")

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c, fc = a, fa
    d = e = b - a
    mflag = True

    eps = 2.220446049250313e-16  

    for _ in range(maxit):
        if fb == 0.0:
            return b

        if abs(fc) < abs(fb):
            a, b, c = b, c, b
            fa, fb, fc = fb, fc, fb

        tol_act = 2 * eps * abs(b) + tol / 2
        m = 0.5 * (c - b)

        if abs(m) <= tol_act:
            return b

        if fa != fc and fb != fc:

            s = (a * fb * fc) / ((fa - fb) * (fa - fc)) \
              + (b * fa * fc) / ((fb - fa) * (fb - fc)) \
              + (c * fa * fb) / ((fc - fa) * (fc - fb))
        else:

            s = b - fb * (b - a) / (fb - fa)

        if b > a:
            cond1 = (s < (3 * a + b) / 4) or (s > b)
        else:
            cond1 = (s > (3 * a + b) / 4) or (s < b)

        cond2 = mflag and (abs(s - b) >= abs(b - c) / 2)
        cond3 = (not mflag) and (abs(s - b) >= abs(c - d) / 2)
        cond4 = mflag and (abs(b - c) < tol_act)
        cond5 = (not mflag) and (abs(c - d) < tol_act)

        if cond1 or cond2 or cond3 or cond4 or cond5:
            s = b + m  
            mflag = True
        else:
            mflag = False

        fs = f(s)
        d = c
        c, fc = b, fb

        if fa * fs < 0:
            b, fb = s, fs
        else:
            a, fa = s, fs

        if abs(fa) < abs(fb):
            a, b = b, a
            fa, fb = fb, fa

    raise RuntimeError("No convergió en maxit iteraciones.")