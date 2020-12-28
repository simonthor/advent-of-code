# Day 7
import pandas as pd
import functools
import re


#%% part 1
def count_outer_bags(bag_name):
    outer_bag_index = bags['inner'].str.contains(bag_name)
    if outer_bag_index.sum() == 0:
        return set()
    return set(bags['outer'][outer_bag_index]) | functools.reduce(set.__or__, (count_outer_bags(bag) for bag in bags['outer'][outer_bag_index]))


bags = pd.read_csv('7.txt', sep='bags contain ', names=['outer', 'inner'], engine='python')
print(len(count_outer_bags('shiny gold')))

#%% part 2

bag_rules = {}
with open('7.txt') as bag_rule_file:
    for bag_rule in bag_rule_file:
        bag_rule = bag_rule.strip('\n')
        bag_name = bag_rule[:bag_rule.index(' bags contain ')]
        if bag_rule.endswith('contain no other bags.'):
            bag_rules[bag_name] = []
        else:
            # I barely know what this line does but it works
            inner_bags = re.split(' bags.| bags, | bag.| bag, ', bag_rule[bag_rule.index('s contain ')+len('s contain'):])
            inner_bags.remove('')
            bag_rules[bag_name] = [{'bag name': inner_bag[3:], 'count': int(inner_bag[1])} for inner_bag in inner_bags]


@functools.lru_cache(maxsize=len(bag_rules))
def count_inner_bags(bag_name):
    if bag_rules[bag_name]:
        return (sum(inner_bag['count']*count_inner_bags(inner_bag['bag name'])
                   for inner_bag in bag_rules[bag_name]) + 1)
    else:
        return 1


print(count_inner_bags('shiny gold')-1)
