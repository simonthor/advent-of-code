# Day 6
import functools

#%% part 1

print(sum(len(set(group_answers.replace('\n', ''))) for group_answers in open('6.txt').read().split('\n\n')))

#%% part 2

print(sum(len(functools.reduce(set.__and__, (set(individual_answer) for individual_answer in group.split('\n'))))
      for group in open('6.txt').read().split('\n\n')))
