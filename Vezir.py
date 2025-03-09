import random

def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def generate_population(size, n):
    population = []
    for _ in range(size):
        board = random.sample(range(n), n)
        population.append(board)
    return population

def selection(population):
    sorted_population = sorted(population, key=lambda x: fitness(x))
    return sorted_population[:2]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(board):
    mutation_point = random.randint(0, len(board) - 1)
    new_value = random.randint(0, len(board) - 1)
    board[mutation_point] = new_value
    return board

def print_chessboard(board):
    size = len(board)
    chessboard = [["" for _ in range(size)] for _ in range(size)]

    for row, col in enumerate(board):
        chessboard[row][col] = "Q"

    for row in range(size):
        for col in range(size):
            if chessboard[row][col] == "Q":
                print(f"\033[48;5;196m{chessboard[row][col]:^3}\033[0m", end=" ")
            else:
                if (row + col) % 2 == 0:
                    print(f"\033[48;5;232m{chessboard[row][col]:^3}\033[0m", end=" ")
                else:
                    print(f"\033[48;5;255m{chessboard[row][col]:^3}\033[0m", end=" ")
        print()
    print("\n")

def genetic_algorithm(n=35, population_size=200, mutation_rate=0.5):
    population = generate_population(population_size, n)
    generation = 0

    while True:
        population = sorted(population, key=lambda x: fitness(x))
        best_fitness = fitness(population[0])
        print(f"{generation}. Nesil: Hata Sayisi = {best_fitness}")

        if best_fitness == 0:
            print(f"{generation}. Nesilde Bulunan Çözüm: {population[0]}")
            print_chessboard(population[0])
            break

        parents = selection(population)

        offspring = []
        for _ in range(len(population) // 2):
            child1, child2 = crossover(parents[0], parents[1])
            offspring.extend([child1, child2])

        for child in offspring:
            if random.random() < mutation_rate:
                mutate(child)

        population = offspring[:population_size]
        generation += 1

genetic_algorithm()
