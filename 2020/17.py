from collections import defaultdict
import numpy as np
import itertools

state = defaultdict(bool)

with open('17.txt') as initial_state_file:
    for x, row in enumerate(initial_state_file):
        for y, cube in enumerate(row):
            if cube == '#':
                state[(x, y, 0)] = True

surroundings = np.array(list(itertools.product([-1, 0, 1], repeat=3)), dtype=int)
surroundings = np.delete(surroundings, surroundings.shape[0]//2, axis=0)
cycles = 6
new_state = defaultdict(bool)
for _ in range(cycles):
    state_coordinates = np.array(list(state.keys()))
    size = np.array([state_coordinates.min(axis=0), state_coordinates.max(axis=0)])
    for x in range(*size[:, 0]):
        for y in range(*size[:, 1]):
            for z in range(*size[:, 2]):
                active_nearby_cubes = np.array([state[tuple(nearby_cube)] for nearby_cube in surroundings + np.array([x, y, z])]).sum()
                if state[(x, y, z)] and (2 <= active_nearby_cubes <= 3):
                    new_state[(x, y, z)] = True
                elif active_nearby_cubes == 3:
                    new_state[(x, y, z)] = True
    state = new_state

print(len(state))
