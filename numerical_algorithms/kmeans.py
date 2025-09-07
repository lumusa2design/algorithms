import math
import random

def squared_euclidean(a,b):
    square = 0.0
    for ai, bi, in zip(a,b):
        square += (ai - bi) ** 2

    return square

def mean_point(points):
    distance = len(points)
    res = [0.0] * distance

    for point in points:
        for j in range(distance):
            res[j] = point[j]

    for i in range(distance):
        res[i] /= float(len(points))
    return res

def assign_labels(data, centroids):
    labels = []
    for x in data:
        best_k = 0
        best_distance = squared_euclidean(x, centroids[0])

        for i in range(1, len(centroids)):
            distance = squared_euclidean(x, centroids[i])

            if distance < best_distance:
                best_distance = distance
                best_k = i
        labels.append(best_k)
    return labels

def recompute_centroids(data, labels, k):
    distance = len(data[0])
    sums = [[0.0] * distance for _ in range(k)]
    counts = [0] * k

    for x, label in zip(data, labels):
        counts[label] += 1
        for j in range(distance):
            sums[label][j] +=  x[j]

    centroids = []

    for i in range(k):
        if counts[i] == 0:
            centroids.append(data[random.randrange(len(data))][:])
        else:
            centroid = []
            for j in range(distance):
                centroid.append(sums[i][j] / float(counts[i]))
            centroids.append(centroid)

    return centroids

def inertia(data, centroids, labels):
    total = 0.0

    for x, label in zip(data, labels):
        total += squared_euclidean(x, centroids[label])
    return total

def kmeans(data, k, max_iters=1000, tol=1e-10):
    centroids = [data[i][:] for i in random.sample(range(len(data)), k)]

    previous_inertia = float("inf")

    for _ in range(max_iters):
        labels = assign_labels(data, centroids)
        centroids = recompute_centroids(data, labels, k)

        current_inertia = inertia(data, centroids, labels)
        if previous_inertia - current_inertia <= tol:
            break
        previous_inertia = current_inertia

    return centroids, labels, current_inertia
