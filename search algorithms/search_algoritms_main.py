from bisection_method import bisection_method
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x + 1

def view_graphic(f, inicio, fin, method,a,b):
    x = np.linspace(inicio,fin,(fin+abs(inicio)*100))
    y = f(x)

    plt.figure(figsize=(8,5))
    plt.plot(x,y, label="funcion", color="b")
    plt.axhline(0, color="black", linewidth=1)  # Eje x
    plt.axvline(0, color="black", linewidth=1)  # Eje y
    plt.grid(True, linestyle="--", alpha=0.6)

    punto_x = method(f,a,b)
    punto_y = f(punto_x)

    plt.scatter(punto_x, punto_y, color="red", zorder=3, label=f"Punto ({punto_x}, {punto_y:.2f})")
    plt.title("Gráfica de la función")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    plt.show()
view_graphic(f, -4, 4, bisection_method, 1, 3)

