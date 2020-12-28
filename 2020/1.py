# Day 1
import numpy as np

# part 1

with open('1.txt') as numberfile:
    numbers = np.array(numberfile.read().split(), dtype=int)

for i in numbers:
    if (product := numbers[numbers + i == 2020] * i).size > 0:
        print(product)

#%% part 2

for i, n in enumerate(numbers):
    for m in numbers[i:]:
        if (product := numbers[numbers + n + m == 2020] * n * m).size > 0:
            print(product)
