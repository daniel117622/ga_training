from knapsack import Knapsack
from box import Box
import random


random.seed(42)

available_boxes = [Box(7,5),Box(2,4),Box(1,7),Box(9,2)]

population = []
for gene in range(10):  
    individual = [random.randint(0, 1) for _ in range(4)]  
    population.append(individual)

        
knap = Knapsack(18)
# The fitness along with the gene which produced that fitness is saved
scoring = []

for gene in population:
    knap.add_selected_boxes(available_boxes, gene)
    scoring.append((gene , knap.get_score()))  
    knap.empty()

# Tournament phase : Some genes along with their scores are chosen.
 # This return the larger gene
def tournament_selection(scoring, tournament_size):
    tournament = random.sample(scoring, tournament_size)
    return max(tournament, key=lambda item: item[1])[0]

tournament_size = 4
parent1 = tournament_selection(scoring, tournament_size)
parent2 = tournament_selection(scoring, tournament_size)

while parent1 == parent2:
    parent2 = tournament_selection(scoring, tournament_size)

 #Selects a random point and combines the genes
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

child1, child2 = crossover(parent1, parent2)


def mutate(gene, mutation_rate):
    return [bit if random.random() > mutation_rate else 1 - bit for bit in gene]

mutation_rate = 0.05
child1 = mutate(child1, mutation_rate)
child2 = mutate(child2, mutation_rate)

# Evaluate and print scores of children
knap.add_selected_boxes(available_boxes, child1)
child1_score = knap.get_score()
knap.empty()

knap.add_selected_boxes(available_boxes, child2)
child2_score = knap.get_score()
knap.empty()

print(f"Child 1: Gene {child1}, Score {child1_score}")
print(f"Child 2: Gene {child2}, Score {child2_score}")