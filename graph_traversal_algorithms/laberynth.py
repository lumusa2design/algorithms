import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.colors import ListedColormap
from graph_traversal_algorithms.DFS import *
from graph_traversal_algorithms.BFS import BFS_find_way
from graph_traversal_algorithms.dijkstra_algorithm import dijkstra
from matplotlib.animation import FuncAnimation, PillowWriter

import networkx as nx

def save_animation(original_matrix, path, start, end, filename="animation.gif", fps=10):
    matrix_of_visited = np.copy(original_matrix).astype(int)
    cmap = ListedColormap(["white", "black", "red", "blue", "green", "#39FF14"])
    fig, ax = plt.subplots(figsize=(8, 8))
    img = ax.imshow(matrix_of_visited, cmap=cmap, vmin=0, vmax=5)
    plt.xticks([]), plt.yticks([])

    def update(frame):
        x, y = path[frame]
        if (x, y) != start and (x, y) != end:
            matrix_of_visited[x][y] = 2  # rojo (visitado)
        matrix_of_visited[start] = 3
        matrix_of_visited[end] = 4
        img.set_data(matrix_of_visited)
        return [img]

    anim = FuncAnimation(fig, update, frames=len(path), interval=1000 / fps, blit=True)
    anim.save(filename, writer=PillowWriter(fps=fps))
    plt.close()


# ----------------------------
# Generar laberinto
# ----------------------------
def create_laberynth_withPath(width, height):
    laberynth = np.ones((height, width), dtype=int)
    visited = np.zeros((height, width), dtype=bool)

    def dfs(x, y):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx_, ny_ = x + dx*2, y + dy*2
            if 0 <= nx_ < height and 0 <= ny_ < width and not visited[nx_][ny_]:
                laberynth[x + dx][y + dy] = 0
                laberynth[nx_][ny_] = 0
                visited[nx_][ny_] = True
                dfs(nx_, ny_)

    laberynth[0][0] = 0
    visited[0][0] = True
    dfs(0, 0)
    return laberynth

# ----------------------------
# Convertir laberinto a grafo
# ----------------------------
def laberynth_to_graph(matriz):
    G = nx.Graph()
    row, cols = matriz.shape
    for x in range(row):
        for y in range(cols):
            if matriz[x][y] == 0:
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx_, ny_ = x + dx, y + dy
                    if row > nx_ >= 0 == matriz[nx_][ny_] and 0 <= ny_ < cols:
                        G.add_edge((x, y), (nx_, ny_), weight=1)  # Añadir peso explícito
    return G


# ----------------------------
# Visualización combinada: recorrido rojo + camino verde
# ----------------------------
def visualize_exploration_and_path(original_matrix, path, start, end, delay=0.0009):
    matrix_of_visited = np.copy(original_matrix).astype(int)

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
    img = plt.imshow(matrix_of_visited, cmap=cmap, vmin=0, vmax=5)
    plt.xticks([]), plt.yticks([])

    for x, y in path:
        if (x, y) != start and (x, y) != end:
            matrix_of_visited[x][y] = 2  # rojo (visitado)
        matrix_of_visited[start] = 3  # azul
        matrix_of_visited[end] = 4     # verde
        img.set_data(matrix_of_visited)
        plt.draw()
        plt.pause(delay)

    plt.title("Path finded by DFS")
    plt.show()

if __name__ == "__main__":
    ancho, alto = 20, 20
    inicio = (0, 0)
    fin = (alto - 2, ancho - 2)

    lab = create_laberynth_withPath(ancho, alto)
    grafo = laberynth_to_graph(lab)

    recorrido_dfs = DFS(grafo,inicio)

    # Mostrar camino en consola
    print("🟢 Camino correcto desde inicio hasta fin:")
    '''for paso in camino_correcto:
        print(paso)'''

    visualize_exploration_and_path(lab, recorrido_dfs, inicio, fin)

    recorrido_bfs = BFS_find_way(grafo, inicio, fin)
    visualize_exploration_and_path(lab, recorrido_bfs, inicio, fin)
"""
    recorrido_dfs_solution = DFS_find_way(grafo, inicio, fin)
    save_animation(lab, recorrido_dfs_solution, inicio, fin, filename="dfs_exploracion.gif", fps=20)

    recorrido_bfs = BFS_find_way(grafo, inicio, fin)
    save_animation(lab, recorrido_bfs, inicio, fin, filename="bfs_exploracion.gif", fps=20)

    recorrido_dijkstra = dijkstra(grafo, inicio, fin)
    save_animation(lab, recorrido_dijkstra, inicio, fin, filename="dijkstra_exploracion.gif", fps=20)
"""