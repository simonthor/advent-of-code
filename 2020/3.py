# Day 3
import numpy as np
import itertools

#%% part 1

tree_counter = 0
index = 0
slope = 3
with open('3.txt') as tree_pattern_file:
    for row in tree_pattern_file:
        row = row[:-1]
        tree_counter += (row[index] == '#')
        index = (index + slope) % (len(row))
print(tree_counter)

#%% part 2

slope = np.arange(1, 8, 2, dtype='int64')
index = np.zeros_like(slope)
tree_counter = np.zeros_like(slope)

with open('3.txt') as tree_pattern_file:
    for row in tree_pattern_file:
        row = row[:-1]
        tree_counter += [row[i] == '#' for i in index]
        index = (index + slope) % (len(row))

# Special case
s_slope = 1
s_index = 0
s_tree_counter = 0
with open('3.txt') as tree_pattern_file:
    for row in itertools.islice(tree_pattern_file, 0, None, 2):
        row = row[:-1]
        s_tree_counter += (row[s_index] == '#')
        s_index = (s_index + s_slope) % (len(row))
print(tree_counter.prod() * s_tree_counter)
