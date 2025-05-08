import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
from matplotlib.colors import ListedColormap
from data_structures.stack import Stack
from graph_traversal_algorithms.DFS import *
from graph_traversal_algorithms.BFS import BFS, BFS_find_way

'''def DFS_camino_correcto(graph, start, goal):
    stack = Stack()
    came_from = {}
    visited = set()
    recorrido = []

    stack.insert(start)
    visited.add(start)

    while not stack.is_empty():
        current = stack.pop()
        recorrido.append(current)

        if current == goal:
            # Reconstruir el camino
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return recorrido, path  # visitados, camino correcto

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.insert(neighbor)

    return recorrido, []  # No hay camino'''

# ----------------------------
# Generar laberinto
# ----------------------------
def crear_laberinto_con_camino(ancho, alto):
    laberinto = np.ones((alto, ancho), dtype=int)
    visitado = np.zeros((alto, ancho), dtype=bool)

    def dfs(x, y):
        direcciones = [(0,1), (1,0), (0,-1), (-1,0)]
        random.shuffle(direcciones)
        for dx, dy in direcciones:
            nx_, ny_ = x + dx*2, y + dy*2
            if 0 <= nx_ < alto and 0 <= ny_ < ancho and not visitado[nx_][ny_]:
                laberinto[x + dx][y + dy] = 0
                laberinto[nx_][ny_] = 0
                visitado[nx_][ny_] = True
                dfs(nx_, ny_)

    laberinto[0][0] = 0
    visitado[0][0] = True
    dfs(0, 0)
    return laberinto

# ----------------------------
# Convertir laberinto a grafo
# ----------------------------
def laberinto_a_grafo(matriz):
    G = nx.Graph()
    filas, cols = matriz.shape
    for x in range(filas):
        for y in range(cols):
            if matriz[x][y] == 0:
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx_, ny_ = x + dx, y + dy
                    if 0 <= nx_ < filas and 0 <= ny_ < cols and matriz[nx_][ny_] == 0:
                        G.add_edge((x, y), (nx_, ny_))
    return G

# ----------------------------
# Visualización combinada: recorrido rojo + camino verde
# ----------------------------
def visualizar_exploracion_y_camino(matriz_original, recorrido, inicio, fin, delay=0.0009):
    matriz_vis = np.copy(matriz_original).astype(int)

    # Colormap:
    # 0 = blanco (camino)
    # 1 = negro (muro)
    # 2 = rojo (visitado)
    # 3 = azul (inicio)
    # 4 = verde (fin)
    # 5 = verde fosforito (camino correcto)
    cmap = ListedColormap(["white", "black", "red", "blue", "green", "#39FF14"])

    # Inicializar gráfico
    plt.figure(figsize=(8, 8))
    img = plt.imshow(matriz_vis, cmap=cmap, vmin=0, vmax=5)
    plt.xticks([]), plt.yticks([])

    for x, y in recorrido:
        if (x, y) != inicio and (x, y) != fin:
            matriz_vis[x][y] = 2  # rojo (visitado)
        matriz_vis[inicio] = 3  # azul
        matriz_vis[fin] = 4     # verde
        img.set_data(matriz_vis)
        plt.draw()
        plt.pause(delay)

    plt.title("Camino encontrado por DFS")
    plt.show()

if __name__ == "__main__":
    ancho, alto = 40, 40
    inicio = (0, 0)
    fin = (alto - 2, ancho - 2)

    lab = crear_laberinto_con_camino(ancho, alto)
    grafo = laberinto_a_grafo(lab)

    """recorrido_dfs = DFS(grafo,inicio)

    # Mostrar camino en consola
    print("🟢 Camino correcto desde inicio hasta fin:")
    '''for paso in camino_correcto:
        print(paso)'''

    visualizar_exploracion_y_camino(lab, recorrido_dfs, inicio, fin)

    recorrido_bfs = BFS(grafo, inicio)
    visualizar_exploracion_y_camino(lab, recorrido_bfs, inicio, fin)"""

    recorrido_dfs_solution = DFS_find_way(grafo, inicio, fin)
    visualizar_exploracion_y_camino(lab, recorrido_dfs_solution, inicio, fin)

    recorrido_bfs = BFS_find_way(grafo, inicio, fin)
    visualizar_exploracion_y_camino(lab, recorrido_bfs, inicio, fin)
