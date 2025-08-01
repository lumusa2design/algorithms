import random

from data_structures.node import Node

functions = ['+', '-', '*', '/']
terminals = ['x', 1.0, 2.0, 3.0]

def generate_random_tree(depth, functions, terminals):
    if depth == 0 or (depth > 1 and random.random() < 0.3):
        return Node(random.choice(terminals))
    else:
        funct = random.choice(functions)
        left = generate_random_tree(depth - 1, functions, terminals)
        right = generate_random_tree(depth - 1, functions, terminals)
        return Node(funct, left, right)

def evaluate_tree(node, x):
    if node.left is None and node.right is None:
        return x if node.value == 'x' else node.value
    else:
        a = evaluate_tree(node.left, x)
        b = evaluate_tree(node.right, x)
        try:
            return eval(f'{a} {node.value} {b}')
        except ZeroDivisionError:
            return float('inf')

def crossover_trees(tree1, tree2):
    if random.random() < 0.6 and tree1.left and tree2.left:
        tree1.left, tree2.left = crossover_trees(tree1.left, tree2.left)
    elif tree1.right and tree2.right:
        tree1.right, tree2.right = crossover_trees(tree1.right, tree2.right)
    return tree1, tree2

def mutate_tree(node, functions, terminals, depth=3):
    if random.random() < 0.1:
        return generate_random_tree(depth, functions, terminals)
    if node.left:
        node.left = mutate_tree(node.left, functions, terminals, depth)
    if node.right:
        node.right = mutate_tree(node.right, functions, terminals, depth)
    return node

def fitness(individual):
    error = 0
    for x in range(-10, 11):
        predicted = evaluate_tree(individual, x)
        target = x ** 2 + 3
        error += abs(predicted - target)
    return error,

