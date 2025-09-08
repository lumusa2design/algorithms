import math
import random

def squared_euclidean(a,b):
    square = 0.0
    for ai, bi   in zip(a,b):
        square += (ai - bi) ** 2

    return square

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

##### TEST

def generate_gaussian_cluster(cx, cy, sx, sy, n):
    pts = []
    for _ in range(n):
        u1, u2 = random.random(), random.random()
        u1 = max(u1, 1e-12)  # evitar log(0)
        r = math.sqrt(-2.0 * math.log(u1))
        theta = 2.0 * math.pi * u2
        z1, z2 = r * math.cos(theta), r * math.sin(theta)
        pts.append([cx + sx * z1, cy + sy * z2])
    return pts


def generate_dataset():
    data = []
    data += generate_gaussian_cluster(0, 0, 0.5, 0.5, 500)
    data += generate_gaussian_cluster(5, 5, 1.0, 0.5, 700)
    data += generate_gaussian_cluster(-5, 5, 0.7, 1.2, 600)
    data += generate_gaussian_cluster(5, -5, 1.5, 1.5, 800)
    for _ in range(200):  # ruido
        data.append([random.uniform(-8, 8), random.uniform(-8, 8)])
    return data

from matplotlib import pyplot as plt

if __name__ == "__main__":
    random.seed(42)
    data = generate_dataset()


    Ks = range(2, 9)  # 7 valores
    inertias = []

    cols = 4
    rows = (len(Ks) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(4*cols, 4*rows))
    axes = axes.ravel()

    for idx, K in enumerate(Ks):
        centroids, labels, J = kmeans(data, K)
        inertias.append(J)

        ax = axes[idx]
        for i, point in enumerate(data):
            ax.scatter(point[0], point[1], c=f"C{labels[i]}", s=10)
        for c in centroids:
            ax.scatter(c[0], c[1], c="black", marker="x", s=200, linewidths=3)
        ax.set_title(f"K={K}, Inercia={J:.1f}")

    for j in range(len(Ks), len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    plt.show()
