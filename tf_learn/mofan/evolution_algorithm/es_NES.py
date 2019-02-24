# -*- coding: utf-8 -*-
"""
The basic idea about Nature Evolution Strategy with visualation.

Visit my tutorial website for more: https://morvanzhou.github.io/tutorials/
"""
import numpy as np
import tensorflow as tf



import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


DNA_SIZE = 1        # DNA (real number)
POP_SIZE = 100      # population size
N_KID = 50          # n kids per generation
DNA_BOUND = [0, 5]  # solution upper and lower bounds
N_GENERATION = 200


def F(x):
    return np.sin(10*x)*x + np.cos(2*x)*x     # to find the maximum of this function


# find non-zero fitness for selection
def get_fitness(pred):
    return pred.flatten()


def make_kid(pop, n_kid):
    # generate empty kid holder
    kids = {'DNA': np.empty((n_kid, DNA_SIZE))}
    kids['mut_strength'] = np.empty_like(kids['DNA'])

    for kid_value, kid_strength in zip(kids['DNA'], kids['mut_strength']):
        # crossover (roughly half p1 and half p2)
        p1, p2 = np.random.choice(np.arange(POP_SIZE), size=2, replace=False)
        crossover_point = np.random.randint(0, 2, DNA_SIZE, dtype=np.bool)      # crossover points

        # 获取p1或者p2索引的值
        kid_value[crossover_point] = pop['DNA'][p1, crossover_point]
        kid_value[~crossover_point] = pop['DNA'][p2, ~crossover_point]

        kid_strength[crossover_point] = pop['mut_strength'][p1, crossover_point]
        kid_strength[~crossover_point] = pop['mut_strength'][p2, ~crossover_point]

        # mutate (chang DNA base on normalize distribution)
        kid_strength[:] = np.maximum(kid_strength + (np.random.rand(*kid_strength.shape) - 0.5), 0.)  # must > 0
        kid_value += kid_strength * np.random.randn(*kid_value.shape)
        kid_value[:] = np.clip(kid_value, *DNA_BOUND)   # clip the mutated value

    return kids


def kill_bad(pop, kids):
    # put pop and kids together
    for key in ['DNA', 'mut_strength']:
        pop[key] = np.vstack((pop[key], kids[key]))

    fitness = get_fitness(F(pop['DNA']))    # calculate global fitness
    idx = np.arange(pop['DNA'].shape[0])
    good_idx = idx[fitness.argsort()][-POP_SIZE:]    # select by fitness ranking(not value)

    for key in ["DNA", 'mut_strength']:
        pop[key] = pop[key][good_idx]

    return pop


pop = {
    'DNA': 5. * np.random.rand(1, DNA_SIZE).repeat(POP_SIZE, axis=0),   # initialize the pop DNA values
    'mut_strength': np.random.rand(POP_SIZE, DNA_SIZE)                  # initialize the pop mutation strength values
}


# something about plotting
plt.ion()
x = np.linspace(*DNA_BOUND, 200)
plt.plot(x, F(x))

for _ in range(N_GENERATION):
    # something about plotting
    if 'sca' in globals():
        sca.remove()

    sca = plt.scatter(pop['DNA'], F(pop['DNA']), s=200, lw=0, c='red', alpha=0.5)
    plt.pause(0.05)

    # ES part
    kids = make_kid(pop, N_KID)
    pop = kill_bad(pop, kids)       # keep some good parent for elitism

plt.ioff()
plt.show()
