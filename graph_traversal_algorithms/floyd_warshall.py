def floyd_warshall(graph):
    num_vertices = len(graph)
    distance = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance