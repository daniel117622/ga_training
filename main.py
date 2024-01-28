from knapsack import Knapsack
from box import Box
import random
from ga import *

random.seed(40)
available_boxes = [
    Box(7, 5), Box(2, 4), Box(1, 7), Box(9, 2),
    Box(5, 3), Box(4, 10), Box(2, 2), Box(8, 6),
    Box(3, 7), Box(6, 1), Box(1, 5), Box(7, 9),
    Box(8, 8), Box(5, 6), Box(6, 7), Box(7, 8),
    Box(2, 9), Box(3, 4), Box(4, 5), Box(5, 2),
    Box(9, 3), Box(8, 4), Box(7, 6), Box(6, 5),
    Box(5, 4), Box(4, 3), Box(3, 2), Box(2, 1)
]

# Adjust the capacity of the knapsack if needed
knap = Knapsack(100)  # Adjusted capacity

# Adjust the size of the population and the genes to match the number of boxes
population = []
for gene in range(10):
    individual = [random.randint(0, 1) for _ in range(len(available_boxes))]
    population.append(individual)
        
scoring = evaluate_population(population, knap, available_boxes)
num_generations = 150
best_overall_gene = None
best_overall_score = -1
for generation in range(num_generations):
    offspring = []
    for _ in range(len(population) // 2):
        parent1 = tournament_selection(scoring, tournament_size=3)
        parent2 = tournament_selection(scoring, tournament_size=3, exclude_individual=parent1)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1, mutation_rate=0.05)
        child2 = mutate(child2, mutation_rate=0.05)
        offspring.extend([child1, child2])

    offspring_scoring = evaluate_population(offspring, knap, available_boxes)

    # Replace population
    population, scoring = replace_population(population, scoring, offspring, offspring_scoring)

    best_current_score = max(scoring, key=lambda item: item[1])[1]

    if best_current_score > best_overall_score:
        best_overall_score = best_current_score
        best_overall_gene = max(scoring, key=lambda item: item[1])[0]
        print(f"Best score in Generation {generation + 1}: {best_current_score}")



# Final evaluation
best_solution = max(scoring, key=lambda item: item[1])
print(f"Best solution found: {best_solution}")
