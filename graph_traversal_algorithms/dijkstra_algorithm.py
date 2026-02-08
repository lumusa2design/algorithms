def dijkstra(graph, first_node, objective):
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[first_node] = 0
    visited = set()
    iteration = 0
    while len(visited) < len(graph.nodes):
        min_node = None
        min_distance = float('inf')

        for node in graph.nodes:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break
        if min_node == objective:
            print(f"Iter Num : {iteration}")
            break

        visited.add(min_node)

        for neighbor in graph.neighbors(min_node):
            if neighbor in visited:
                continue
            weight = graph[min_node][neighbor].get('weight', 1)
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = min_node
        iteration += 1

    path = []
    current = objective
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    return path

def dijkstra_all(graph, first_node):
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[first_node] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        min_node = None
        min_distance = float('inf')

        for node in graph.nodes:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break

        visited.add(min_node)

        for neighbor in graph.neighbors(min_node):
            if neighbor in visited:
                continue
            weight = graph[min_node][neighbor].get('weight', 1)
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = min_node

    return distances, previous

