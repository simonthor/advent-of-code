import functools
import re


#%% part 1
def solve_problem(problem: str) -> int:
    if '(' not in problem:
        # might be able to do this with functools.reduce
        # TODO: this might not work
        ans = functools.reduce(lambda ans, i: eval(f'{ans}{problem[i.start():i.end()+1]}'),
                               re.finditer('[*+]', problem), int(problem[0]))
        #ans = int(problem[0])
        #for i in re.finditer('[*+]', problem):
        #    ans = eval(f'{ans}{problem[i.start():i.end()+1]}')
        return ans
    else:
        first_parenthesis = problem.index('(')
        first_part = (str(solve_problem(problem[:first_parenthesis-1]))+problem[first_parenthesis-1]
                      if first_parenthesis != 0 else '')

        parenthesis_depth = 1
        closing_parenthesis = first_parenthesis
        while parenthesis_depth != 0:
            closing_parenthesis += 1
            if problem[closing_parenthesis] == '(':
                parenthesis_depth += 1
            elif problem[closing_parenthesis] == ')':
                parenthesis_depth -= 1
        inside_parenthesis = solve_problem(problem[first_parenthesis+1:closing_parenthesis])
        rest = (problem[closing_parenthesis+1] + str(solve_problem(problem[closing_parenthesis+2:]))
                if closing_parenthesis < len(problem)-1 else '')
        return solve_problem(f'{first_part}{inside_parenthesis}{rest}')


#%%
if __name__ == '__main__':
    print(solve_problem('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'.replace(' ', '')))
    # with open('18.txt') as homework_file:
    #     solution_sum = 0
    #     for problem_str in homework_file:
    #         problem_str = problem_str.strip()
    #         problem_str = problem_str.replace(' ', '')
    #         #problem_str = problem_str.replace(')', ' )')
    #         #problem = problem_str.split(' ')
    #         solution_sum += solve_problem(problem_str)
    # print(solution_sum)
