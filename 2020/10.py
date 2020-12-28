# Day 10
import numpy as np
import awkward as ak

#%% part 1

jolts = np.loadtxt('10.txt', dtype=np.int64)
jolts = np.append(jolts, jolts.max() + 3)
jolts = np.insert(jolts, 0, 0)
jolts.sort()
jolt_diff = np.diff(jolts)
(jolt_diff == 3).sum() * (jolt_diff == 1).sum()

# %% part 2

nonmoveable = (jolt_diff == 3).nonzero()[0] + 1
all_possible_configurations = 1
for start_i, end_i in zip(np.insert(nonmoveable[:-1], 0, 0) + 1, nonmoveable):
    max_int = end_i - start_i - 1
    if max_int > 0:
        possible_subsets = 0

        for picks in ((np.arange(2 ** max_int)[:, None] & (1 << np.arange(max_int))) > 0).astype(bool).tolist():
            if (np.diff(jolts[start_i - 1:end_i][np.concatenate(((True,), picks, (True,)))]) <= 3).all():
                possible_subsets += 1
        all_possible_configurations *= possible_subsets
print(all_possible_configurations)


# The code below gives the same solution as above but using Awkward Array, thus making the code vectorized.
# I was not sure how to make this efficient as the typical ak.Array(np_array) does not create a variable row length array.
# I solved it by calling `extended_possible_subsets.tolist()` but I don't think this is efficient.

nonmoveable = (jolt_diff == 3).nonzero()[0] + 1
all_possible_configurations = 1
for start_i, end_i in zip(np.insert(nonmoveable[:-1], 0, 0) + 1, nonmoveable):
    max_int = end_i - start_i - 1
    if max_int > 0:
        possible_subsets = ((np.arange(2 ** max_int)[:, None] & (1 << np.arange(max_int))) > 0).astype(bool)
        extended_possible_subsets = np.ones((2 ** max_int, max_int + 2)).astype(bool)
        extended_possible_subsets[:, 1:-1] = possible_subsets
        allowed_subsets = ak.Array(np.tile(jolts[start_i - 1:end_i], (2 ** max_int, 1)))[
            ak.Array(extended_possible_subsets.tolist())]
        allowed_subset_count = int(ak.sum(ak.all((allowed_subsets[:, 1:] - allowed_subsets[:, :-1]) <= 3, axis=1)))
        all_possible_configurations *= allowed_subset_count
print(all_possible_configurations)
