from numpy import array

def beam_search(distances, beta):
    path_far = [[list(), 0]]
    for i, tier in enumerate(distances):
        path_tier = list()
        for j in range(len(path_far)):
            path, distance = path_far[j]

            for k in range(len(tier)):
                path_extended = [path + [j], distance + tier[j]]
                path_tier.append(path_extended)

        path_sorted = sorted(path_tier, key=lambda element: element[1])
        path_far = path_sorted[:beta]
    return path_far
