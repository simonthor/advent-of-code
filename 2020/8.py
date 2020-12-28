# Day 8
import pandas as pd

#%% part 1
instructions = pd.read_csv('8.txt', sep=' ', names=['instruction', 'value'])
visited_instructions = []
i = 0
acc = 0
while i not in visited_instructions:
    visited_instructions += [i]
    if instructions.loc[i, 'instruction'] == 'acc':
        acc += instructions.loc[i, 'value']
        i += 1
    elif instructions.loc[i, 'instruction'] == 'jmp':
        i += instructions.loc[i, 'value']
    else:
        i += 1
print(acc)


#%% part 2
def do_instructions(instructions):
    visited_instructions = []
    i = 0
    acc = 0

    while (i not in visited_instructions) and (i <= instructions.index[-1]):
        visited_instructions += [i]
        if instructions.loc[i, 'instruction'] == 'acc':
            acc += instructions.loc[i, 'value']
            i += 1
            continue
        elif instructions.loc[i, 'instruction'] == 'jmp':
            i += instructions.loc[i, 'value']
        else:
            i += 1
    return i, acc


for change_index in instructions.query("instruction == 'jmp' or instruction == 'nop'").index:
    modified_instructions = instructions.copy()
    modified_instructions.loc[change_index, 'instruction'] = 'jmp' if modified_instructions.loc[
                                                                          change_index, 'instruction'] == 'nop' else 'nop'
    i, acc = do_instructions(modified_instructions)
    if i > modified_instructions.index[-1]:
        print(acc)
        break
