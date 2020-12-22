import functools
import operator

#%% part 1
operator = {'+': operator.__add__, '*': operator.__mul__}


def solve_problem(problem: list) -> int:
    if '(' not in problem:
        # TODO: might be able to do this with functools.reduce
        ans = int(problem[0])
        for i, o in enumerate(problem[1:-1:2]):
            ans = operator[o](ans, int(problem[i*2+2]))
        return ans

    #problem.split()
    #return sum(solve_problem())

#%%
with open('18.txt') as homework_file:
    solution_sum = 0
    for problem_str in homework_file:
        problem_str = problem_str.strip()
        problem_str = problem_str.replace('(', '( ')
        problem_str = problem_str.replace(')', ' )')
        problem = problem_str.split(' ')
        solution_sum += solve_problem(problem)
print(solution_sum)