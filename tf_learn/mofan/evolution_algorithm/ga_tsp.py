# -*- coding: utf-8 -*-

"""
Visualize Genetic Algorithm to find the shortest path for travel sales problem.
Visit my tutorial website for more: https://morvanzhou.github.io/tutorials/
"""
import matplotlib.pyplot as plt
import numpy as np

N_CITIES = 20       # DNA size
POP_SIZE = 500
CROSS_RATE = 0.1
MUTATE_RATE = 0.02
N_GENERATIONS = 500


class GA(object):
    def __init__(self, DNA_size, cross_rate, mutation_rate, pop_size):
        self.DNA_size = DNA_size
        self.cross_rate = cross_rate
        self.mutation_rate = mutation_rate
        self.pop_size = pop_size

        self.pop = np.vstack([np.random.permutation(DNA_size) for _ in range(pop_size)])

    def translateDNA(self, DNA, city_position):     # get cities' coord in order
        line_x = np.empty_like(DNA, dtype=np.float64)
        line_y = np.empty_like(DNA, dtype=np.float64)

        for i, d in enumerate(DNA):
            city_crood = city_position[d]
            line_x[i, :] = city_crood[:, 0]
            line_y[i, :] = city_crood[:, 1]

        return line_x, line_y

    def get_fitness(self, line_x, line_y):
        total_distance = np.empty((line_x.shape[0],), dtype=np.float64)
        for i, (xs, ys) in enumerate(zip(line_x, line_y)):
            total_distance[i] = np.sum(np.sqrt(np.square(np.diff(xs)) + np.square(np.diff(ys))))

        fitness = np.exp(self.DNA_size * 2 / total_distance)
        return fitness, total_distance

    def select(self, fitness):
        idx = np.random.choice(np.range(self.pop_size), size=self.pop_size, replace=True, p=fitness/fitness.sum())
        return self.pop(idx)

    def crossover(self, parent, pop):
        if np.random.rand() < self.cross_rate:
            i_ = np.random.randint(0, self.pop_size, size=1)    # select another individual from pop
            cross_points = np.random.randint(0, 2, self.DNA_size).astype(np.bool)   # choose crossover points


