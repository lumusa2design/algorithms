from data_structures.heap import Heap
import math

def A_star(graph, first_node, goal_node, heuristic):
    visited, viewed, open_set, came_from, g_score, cost_function, counter, iters = [], set(), Heap(), {}, {first_node: 0}, getattr(graph, "cost", lambda u, v: 1), 0, 0
    open_set.insert((heuristic(first_node, goal_node), counter, first_node))
    viewed.add(first_node)

    while len(open_set) > 0:
        f, _, actual_node = open_set.extract()

        if actual_node in visited:
            continue

        visited.append(actual_node)
        iters += 1

        if actual_node == goal_node:
            path = [goal_node]
            while path[-1] != first_node:
                path.append(came_from[path[-1]])
            path.reverse()
            print(f"Iter Num: {iters}\n")
            return path, visited, g_score[goal_node]

        for neighbour in graph.neighbors(actual_node):
            tentative_g = g_score[actual_node] + cost_function(actual_node, neighbour)

            if tentative_g < g_score.get(neighbour, math.inf):
                came_from[neighbour] = actual_node
                g_score[neighbour] = tentative_g
                f_score = tentative_g + heuristic(neighbour, goal_node)
                counter += 1
                open_set.insert((f_score, counter, neighbour))
                viewed.add(neighbour)

    print(f"Iter Num: {iters}\n")
    return [], visited, math.inf



def A_star_find_way(graph, first_node, goal, h):

    path, _, _ = A_star(graph, first_node, goal, h)
    return path
