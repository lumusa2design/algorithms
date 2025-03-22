from bisection_method import bisection_method
from regulafalsi import regula_falsi
from newton_raphson_method import newton_raphson
import numpy as np
import matplotlib.pyplot as plt
from secant_method import secant_method
def f(x):
    return x ** 3 - 4 * x + 1


def view_graphic(f, inicio, fin, method, a, b=None, *args):
    x = np.linspace(inicio, fin, 500)
    y = f(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="Función", color="b")
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.grid(True, linestyle="--", alpha=0.6)

    try:
        if b is None:  # Para Newton-Raphson, solo necesita un punto inicial
            punto_x = method(f, a, *args)
        else:
            punto_x = method(f, a, b, *args)

        punto_y = f(punto_x)
        plt.scatter(punto_x, punto_y, color="red", zorder=3, label=f"Punto ({punto_x:.6f}, {punto_y:.6f})")
    except ValueError:
        print("El método no puede encontrar una raíz en el intervalo dado.")

    plt.title(f"Gráfica de la función usando {method.__name__}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()


# Pruebas con diferentes métodos
view_graphic(f, -4, 4, bisection_method, 1, 3)
view_graphic(f, -4, 4, regula_falsi, 1, 3, 100)
view_graphic(f, -4, 4, newton_raphson, -3, 100)
view_graphic(f, -4, 4, secant_method, 1,3)