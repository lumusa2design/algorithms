import matplotlib.pyplot as plt
import one_point_crossover as opc
def draw_individual(ax, individual, title, crossover_point=None, highlight=False):
    ax.set_title(title)
    ax.axis('off')
    for i, gene in enumerate(individual):
        if highlight and crossover_point is not None:
            color = 'orange' if i < crossover_point else 'lightgreen'
        else:
            color = 'lightblue'
        rect = plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black')
        ax.add_patch(rect)
        ax.text(i + 0.5, 0.5, str(gene), ha='center', va='center', fontsize=12)

    ax.set_xlim(0, len(individual))
    ax.set_ylim(0, 1)

def visualize_one_point_crossover(father, mother, point):
    fig, axs = plt.subplots(2, 1, figsize=(len(father), 2))
    draw_individual(axs[0], father, "Padre")
    draw_individual(axs[1], mother, "Madre")
    plt.suptitle(f"Antes del cruce en el punto {point}", fontsize=14)
    plt.tight_layout()
    plt.show()

    new_father, new_mother = opc.one_point_crossover(point, father, mother)

    fig, axs = plt.subplots(2, 1, figsize=(len(father), 2))
    draw_individual(axs[0], new_father, "Hijo 1 (Padre tras el cruce)", point, highlight=True)
    draw_individual(axs[1], new_mother, "Hijo 2 (Madre tras el cruce)", point, highlight=True)
    plt.suptitle(f"Después del cruce en el punto {point}", fontsize=14)
    plt.tight_layout()
    plt.show()

father = [1, 1, 1, 1, 1, 1, 1, 1]
mother = [0, 0, 0, 0, 0, 0, 0, 0]
crossover_point = 4

visualize_one_point_crossover(father, mother, crossover_point)
