# Day 9
import numpy as np
import itertools

#%% part 1

xmas_data = np.loadtxt('9.txt', dtype=np.int64)

for i, value in enumerate(xmas_data[25:]):
    combinations = np.array([combination for combination in itertools.combinations(xmas_data[i:i+25], 2)], dtype=np.int64)
    if value not in combinations.sum(axis=1):
        print(value)
        break

#%% part 2

for low_i, high_i in itertools.combinations(range(i), 2):
    contiguous_set = xmas_data[low_i:high_i]
    if contiguous_set.sum() == value:
        print(contiguous_set.min()+contiguous_set.max())
        break
