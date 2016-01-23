# the problem to solve: create a list of n numbers that are equal to X when added up
# reference http://lethain.com/genetic-algorithms-cool-name-damn-simple/

import random as r
from operator import add
from functools import reduce

#create random individual


def individual(n, min, max):
    return[r.randint(min, max)for x in range(n)]

# creates a population of n individuals
def population(count, n, min, max):
    return [individual(n, min, max) for x in range(count)]

# evaluates the fitness of an individual, careful perfect fitness = 0 in this case
def fitness(creature, target):
    sum = reduce(add, creature, 0)
    return abs(target-sum)


def avg_fitness(p, target):
    summed = reduce(add, (fitness(x, target) for x in p), 0)
    return summed / (len(p) * 1.0)

# Test
x = population(250, 5, 0, 100)
target = 100
print(avg_fitness(x, target))


def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [ (fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    # randomly add other individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > r.random():
            parents.append(individual)
    # mutate some individuals
    for individual in parents:
        if mutate > r.random():
            pos_to_mutate = r.randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = r.randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = r.randint(0, parents_length-1)
        female = r.randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) / 2
            child = male[:int(half)] + female[int(half):]
            children.append(child)
    parents.extend(children)
    return parents

target = 371
p_count = 100
i_length = 6
i_min = 0
i_max = 100
p = population(p_count, i_length, i_min, i_max)
fitness_history = [avg_fitness(p, target), ]
for i in range(100):
    p = evolve(p, target)
    fitness_history.append(avg_fitness(p, target))

for d in fitness_history:
    print(d)

