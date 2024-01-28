import random
from knapsack import Knapsack
from box import Box

def replace_population(population, scoring, offspring, offspring_scoring):
    # Combine current population and offspring
    combined_population = population + [gene for gene, score in offspring_scoring]
    combined_scoring = scoring + offspring_scoring

    # Sort combined population by score (descending)
    combined_population_sorted = sorted(combined_scoring, key=lambda x: x[1], reverse=True)

    # Keep only the top individuals
    new_population = [gene for gene, score in combined_population_sorted[:len(population)]]
    new_scoring = combined_population_sorted[:len(population)]

    # Print message when a member is replaced
    for original, new in zip(scoring, new_scoring):
        if original != new:
            pass # Dont print anything
    return new_population, new_scoring

def evaluate_population(population, knapsack, boxes):
    scoring = []
    for gene in population:
        knapsack.empty()
        knapsack.add_selected_boxes(boxes, gene)
        scoring.append((gene, knapsack.get_score()))
    return scoring

def mutate(gene, mutation_rate):
    return [bit if random.random() > mutation_rate else 1 - bit for bit in gene]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def tournament_selection(scoring, tournament_size, exclude_individual=None): #To avoid infinite loop
    candidates = scoring.copy()
    if exclude_individual is not None:
        candidates = [item for item in candidates if item[0] != exclude_individual[0]]


    tournament = random.sample(candidates, tournament_size)
    return max(tournament, key=lambda item: item[1])[0]