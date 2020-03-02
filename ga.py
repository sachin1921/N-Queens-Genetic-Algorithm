import random
# import numpy as np

MUTATE_FLAG = True
MUTATION_PROB = 0.03


def population(size): 
    obj = [ random.randint(1, 8) for _ in range(8) ]
    return obj

def fitness(chromosome):
    horizontal = sum([chromosome.count(queen)-1 for queen in chromosome])/2
    diagonal = 0

    size = len(chromosome)
    f1 = [0] * 2*size
    f2 = [0] * 2*size
    for i in range(size):
        f1[i + chromosome[i] - 1] += 1
        f2[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal = 0
    for i in range(2*size-1):
        counter = 0
        if f1[i] > 1:
            counter += f1[i]-1
        if f2[i] > 1:
            counter += f2[i]-1
        diagonal += counter / (size-abs(i-size+1))
    
    return int(28 - (horizontal + diagonal)) 
#     clashes = 0;
# # calculate row and column clashes
# # just subtract the unique length of array from total length of array
# # [1,1,1,2,2,2] - [1,2] => 4 clashes
#     row_col_clashes = abs(len(chromosome) - len(np.unique(chromosome)))
#     clashes += row_col_clashes

# # calculate diagonal clashes
#     for i in range(len(chromosome)):
#         for j in range(len(chromosome)):
#             if ( i != j):
#                 dx = abs(i-j)
#                 dy = abs(chromosome[i] - chromosome[j])
#                 if(dx == dy):
#                     clashes += 1
#     return 28 - clashes 

# def fitness(chromosome):
#     t1 = 0
#     t2 = 0
#     size = len(chromosome)
#     f1 = [0]*2*size
#     f2 = [0]*2*size
#     for i in range(1,size):
#         f1[i] = chromosome[i] - i
#         f2[i] = ((1 + size) - chromosome[i] - i)
#     f1.sort()
#     f2.sort()
#     for i in range(2,size):
#         if (f1[i] == f1[i-1]):
#             t1 = t1 + 1
#         if (f2[i] == f2[i-1]):
#             t2 = t2 + 1
#     fitness_val = t1 + t2
#     return fitness_val



def getProbability(chromosome, fitness):
    return fitness(chromosome) / 28

def random_pick(population, probabilities):
    population_and_probabilities = zip(population, probabilities)
    total = sum(w for c, w in population_and_probabilities)
    r = random.uniform(0, total)
    to = 0
    for c, w in zip(population, probabilities):
        if to + w >= r:
            return c
        to += w

def getParents(population, probabilities):
    while True:
        parent1 = random_pick(population, probabilities)
        parent2 = random_pick(population, probabilities)
        if(parent1 == parent2): continue
        else: break
    if parent1 is not None and parent2 is not None:
        return parent1, parent2
    else:
        return -1
        
def reproduce(parent1, parent2): #doing cross_over between two chromosomes
    n = len(parent1)
    c = random.randint(0, n - 1)
    return parent1[0:c] + parent2[c:n]

def mutate(x):  #randomly changing the value of a random index of a chromosome
    if random.random() < MUTATION_PROB:
        n = len(x)
        c = random.randint(0, n - 1)
        m = random.randint(1,n)
        x[c] = m
    return x


def ga(population, fitness):
    new_population = []
    probabilities = [getProbability(n, fitness) for n in population]
    for i in range(len(population)):
        parent1,parent2 = getParents(population, probabilities)
        child = reproduce(parent1, parent2) #creating two new chromosomes from the best 2 chromosomes
        if(MUTATE_FLAG):
            child = mutate(child)
        new_population.append(child)
        if fitness(child) == 28: break
    return new_population




def getAllSolutions():
    chrom_out = []
    solutions = []
    counter = 0
    while True:
        pop = [population(8) for _ in range(100)]
        generation = 1
        while not 28 in [fitness(chrom) for chrom in pop]:
        	# print("=== Generation {} ===".format(generation))
        	pop = ga(pop, fitness)
        	# print("")
        	# print("Maximum Fitness = {}".format(max([fitness(n) for n in pop])))
        	generation += 1

        print("Solved in Generation {}!".format(generation-1))
        for chrom in pop:
            if chrom in solutions:
                continue
            else:
                if fitness(chrom) == 28:
                    solutions.append(chrom)
                    counter = counter + 1
                    print("");
                    print(counter)
                    print("One of the solutions: ")
                    print("Chromosome = {},  Fitness = {}".format(str(chrom), fitness(chrom)))
                    pop.clear()
                    break
        if len(solutions) == 92:
            break
    print(solutions)            
        
def getOneSolution():
    chrom_out = []
    # solutions = []
    # counter = 0
    # while True:
    pop = [population(8) for _ in range(100)]
    generation = 1
    while not 28 in [fitness(chrom) for chrom in pop]:
        # print("=== Generation {} ===".format(generation))
        pop = ga(pop, fitness)
        # print("")
        # print("Maximum Fitness = {}".format(max([fitness(n) for n in pop])))
        generation += 1

    print("Solved in Generation {}!".format(generation-1))
    for chrom in pop:
        if fitness(chrom) == 28:
            print("");
            print("One of the solutions: ")
            print("Chromosome = {},  Fitness = {}".format(str(chrom), fitness(chrom)))
            break
       

getOneSolution()