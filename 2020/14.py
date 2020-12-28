# Day 14
import re
import numpy as np

#%% part 1

memory = {}
int_size = 36
with open('14.txt') as bitmask_file:
    for line in bitmask_file:
        if line[:4] == 'mask':
            mask = np.array([int(i)  if i != 'X' else np.nan for i in line[7:-1]])
        elif line[:3] == 'mem':
            memory_loc = int(re.search(r'\[(.*?)\]', line).group(1))
            value = int(line[line.index(' = ')+3:-1])
            value_bin = np.array(list(np.binary_repr(value).zfill(int_size))).astype(np.int8)
            masked_value_bin = np.where(np.isnan(mask), value_bin, mask).astype(np.uint64)
            masked_value = (masked_value_bin*np.uint64(2)**np.arange(int_size-1, -1, -1).astype(np.uint64)).sum()
            memory[memory_loc] = masked_value

print(sum(memory.values()))

#%% part 2

memory = {}
int_size = 36
with open('14.txt') as bitmask_file:
    for line in bitmask_file:
        # This loop is quite slow and takes a few seconds
        if line[:4] == 'mask':
            mask = np.array([int(i)  if i != 'X' else np.nan for i in line[7:-1]])
        elif line[:3] == 'mem':
            adress = int(re.search(r'\[(.*?)\]', line).group(1))
            value = int(line[line.index(' = ')+3:-1])
            adress_bin = np.array(list(np.binary_repr(adress).zfill(int_size))).astype(np.int8)
            float_bit_count = np.isnan(mask).sum()
            possible_float_states = (((np.arange(2**float_bit_count)[:,None] & (1 << np.arange(float_bit_count)))) > 0)
            adress_bin[mask == 1] = 1
            for float_state in possible_float_states:
                adress_bin[np.isnan(mask)] = float_state
                masked_adress = int((adress_bin*np.uint64(2)**np.arange(int_size-1, -1, -1).astype(np.uint64)).sum())
                memory[masked_adress] = value

print(sum(memory.values()))
