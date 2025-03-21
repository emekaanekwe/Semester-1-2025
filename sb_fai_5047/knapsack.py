import random

'''
you enter a treasure-filled cave carrying a knapsack. 
    The knapsack can only carry 35kg of weight. 
    The cave has 10 items, each with a specific weight and sell value.
    select the items that maximizes how much you can sell without
    exceeding the weight.
'''

'''
The first is a use case of a genetic algorithm to solve the problem
'''

# Knapsack parameters
k_items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value) as list of tuples
capacity = 8 
population = 10
generations = 20
mutation_rate = 0.1

# Generate a random chromosome (solution)
def create_chromosome():
    return [random.randint(0, 1) for _ in range(len(k_items))]

# Calculate the fitness of a chromosome
def fitness(chromosome):
    total_value = 0
    total_weight = 0
    for i, gene in enumerate(chromosome):
        if gene == 1:
            total_value += k_items[i][1]
            total_weight += k_items[i][0]
    # Penalize solutions that exceed the capacity
    if total_weight > capacity:
        return 0
    return total_value

# Roulette wheel selection
def roulette_wheel_selection(population):
    # Calculate total fitness of the population
    total_fitness = sum(fitness(chromosome) for chromosome in population)
    
    # Generate a random value between 0 and total_fitness
    pick = random.uniform(0, total_fitness)
    
    # Select a chromosome based on the random value
    current = 0
    for chromosome in population:
        current += fitness(chromosome)
        if current > pick:
            return chromosome

# Perform crossover to create a child
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(k_items) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Perform mutation on a chromosome
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip the gene
    return chromosome

# Main genetic algorithm
def genetic_algorithm():
    # Initialize population
    population = [create_chromosome() for _ in range(population)]
    
    for generation in range(generations):
        # Evaluate fitness
        population = sorted(population, key=fitness, reverse=True)
        
        # Select the best solution
        best_solution = population[0]
        print(f"Generation {generation}: Best Value = {fitness(best_solution)}")
        
        # Create the next generation
        new_population = [best_solution]  # Keep the best solution (elitism)
        while len(new_population) < population:
            parent1 = roulette_wheel_selection(population)
            parent2 = roulette_wheel_selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
    
    # Return the best solution
    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)

# Run the algorithm
best_solution, best_value = genetic_algorithm()
print("\nBest Solution:", best_solution)
print("Best Value:", best_value)