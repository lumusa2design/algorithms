import random
from uniform_crossover import uniform_crossover
from mutation import smart_mutation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def row_mutation(individual, puzzle):
    row = random.randint(0, 8)
    start = row * 9
    end = start + 9
    mutable_indices = [i for i in range(start, end) if puzzle[i] == 0]
    if len(mutable_indices) >= 2:
        i1, i2 = random.sample(mutable_indices, 2)
        individual[i1], individual[i2] = individual[i2], individual[i1]
    return individual

def plot_colored_sudoku_frame_with_errors(board, puzzle, ax):
    ax.clear()
    errors = set()
    grid = [board[i*9:(i+1)*9] for i in range(9)]

    for i, row in enumerate(grid):
        seen = {}
        for j, num in enumerate(row):
            if num in seen:
                errors.add((i, j))
                errors.add((i, seen[num]))
            elif num != 0:
                seen[num] = j

    for j in range(9):
        seen = {}
        for i in range(9):
            num = grid[i][j]
            if num in seen:
                errors.add((i, j))
                errors.add((seen[num], j))
            elif num != 0:
                seen[num] = i

    for bi in range(0, 9, 3):
        for bj in range(0, 9, 3):
            seen = {}
            for i in range(3):
                for j in range(3):
                    r, c = bi+i, bj+j
                    num = grid[r][c]
                    if num in seen:
                        errors.add((r, c))
                        errors.add(seen[num])
                    elif num != 0:
                        seen[num] = (r, c)

    for i in range(10):
        lw = 2 if i % 3 == 0 else 1
        ax.plot([0, 9], [i, i], color='black', linewidth=lw)
        ax.plot([i, i], [0, 9], color='black', linewidth=lw)

    for i in range(9):
        for j in range(9):
            num = board[i*9 + j]
            if num != 0:
                pos = (i, j)
                if pos in errors:
                    color = 'red'
                elif puzzle[i*9 + j] == 0:
                    color = 'blue'
                else:
                    color = 'black'
                ax.text(j + 0.5, 8.5 - i, str(num), va='center', ha='center', fontsize=16, color=color, fontweight='bold')

    ax.axis('off')
    ax.set_title("Sudoku's Evolution")

def update_colored(frame):
    plot_colored_sudoku_frame_with_errors(history[frame], flattened_puzzle, ax)
    percentage_fitness = [(f / 243.0) * 100 for f in fitness_over_time[:frame+1]]
    line.set_data(range(len(percentage_fitness)), percentage_fitness)
    return line,


def is_valid(board, row, col, num):
    if any(board[row][i] == num for i in range(9)):
        return False
    if any(board[i][col] == num for i in range(9)):
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    board = [[0 for _ in range(9)] for _ in range(9)]

    def fill_board():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if fill_board():
                                return True
                            board[i][j] = 0
                    return False
        return True

    fill_board()
    return board

def remove_cells(board, holes=40):
    puzzle = [row[:] for row in board]
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for i in range(holes):
        r, c = cells[i]
        puzzle[r][c] = 0
    return puzzle

def initialize_individual(puzzle):
    individual = puzzle[:]
    for i in range(9):
        row_start = i * 9
        missing = [n for n in range(1, 10) if n not in individual[row_start:row_start+9]]
        random.shuffle(missing)
        idx = 0
        for j in range(9):
            if individual[row_start + j] == 0:
                individual[row_start + j] = missing[idx]
                idx += 1
    return individual

def repair_individual(individual, puzzle):
    board = [individual[i*9:(i+1)*9] for i in range(9)]
    for i in range(9):
        row = board[i]
        seen = set()
        duplicates = []
        for j in range(9):
            if puzzle[i*9 + j] == 0:
                if row[j] in seen:
                    duplicates.append(j)
                else:
                    seen.add(row[j])
        missing = [n for n in range(1, 10) if n not in seen]
        for j, val in zip(duplicates, missing):
            row[j] = val
        board[i] = row
    return [cell for row in board for cell in row]

def solve_linear(individual):
    board = [individual[i*9:(i+1)*9] for i in range(9)]
    if solve(board):
        return [num for row in board for num in row]
    return individual

history = []
fitness_over_time = []


def optimized_genetic_algorithm(puzzle, generations=10000, population_size=200):
    def fitness(individual):
        board = [individual[i*9:(i+1)*9] for i in range(9)]
        errors = 0
        for row in board:
            errors += (9 - len(set(row)))
        for col in zip(*board):
            errors += (9 - len(set(col)))
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                errors += (9 - len(set(block)))
        return 243 - errors

    def tournament_selection(pop, k=5):
        return max(random.sample(pop, k), key=fitness)

    population = [initialize_individual(puzzle) for _ in range(population_size)]
    best = max(population, key=fitness)
    history.clear()
    fitness_over_time.clear()

    no_improvement_count = 0
    best_fitness = fitness(best)

    with open("generations.txt", "w", encoding="utf-8") as f:
        for generation in range(generations):
            elite = max(population, key=fitness)
            new_population = [elite]

            while len(new_population) < population_size:
                parents = [tournament_selection(population) for _ in range(2)]
                child = uniform_crossover(parents[0][:], parents[1][:])

                if random.random() < 0.5:
                    child = smart_mutation(child, puzzle, probability=20)
                else:
                    child = row_mutation(child, puzzle)

                if random.random() < 0.3:
                    child = repair_individual(child, puzzle)

                for i in range(81):
                    if puzzle[i] != 0:
                        child[i] = puzzle[i]

                fitness_child = fitness(child)
                f.write(f"Generation {generation:03d} - Fitness: {fitness_child:.2f} - Child: {','.join(map(str, child))}\n")
                new_population.append(child)

            population = sorted(new_population, key=fitness, reverse=True)
            best = population[0]
            current_fitness = fitness(best)
            history.append(best[:])
            fitness_over_time.append(current_fitness)

            print(f"Generation {generation:03d} → Fitness: {current_fitness/243*100:.2f}%")

            if current_fitness > best_fitness:
                best_fitness = current_fitness
                no_improvement_count = 0
            else:
                no_improvement_count += 1

            if no_improvement_count >= 200:
                print("Generation stuck... created new population")
                for i in range(1, population_size):
                    population[i] = initialize_individual(puzzle)
                no_improvement_count = 0

            if current_fitness >= 225:
                solved = solve_linear(best)
                if fitness(solved) > current_fitness:
                    best = solved
                    history.append(best[:])
                    fitness_over_time.append(fitness(best))
                    if fitness(best) == 243:
                        print("¡Solución exacta encontrada!")
                        break
                if fitness(best) == 243:
                    print("¡Solución exacta encontrada!")
                    break

    return best


if __name__ == "__main__":
    full_board = generate_full_board()
    puzzle = remove_cells(full_board, holes=40)
    flattened_puzzle = sum(puzzle, [])

    start_time = time.time()
    solution = optimized_genetic_algorithm(flattened_puzzle, generations=3000, population_size=500)
    end_time = time.time()
    print(f"\nTotal Time: {end_time - start_time:.2f} seconds")

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    line, = ax2.plot([], [], 'r-')
    ax2.set_xlim(0, len(history))
    ax2.set_ylim(0, 100)
    ax2.set_title("Fitness")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("fit")

    ani = FuncAnimation(fig, update_colored, frames=len(history), interval=100, blit=False, repeat=False)
    plt.tight_layout()
    plt.show()
