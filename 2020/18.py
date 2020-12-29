import functools
import re


#%% part 1
def solve_problem(problem: str) -> int:
    if '(' not in problem:
        if not (first_operator_loc := re.search('[*+]', problem)):
            return int(problem)
        ans = functools.reduce(lambda ans, i: eval(f'{ans}{problem[i.start()-1:i.end()]}'),
                               list(re.finditer('\d+', problem))[1:], int(problem[:first_operator_loc.start()]))
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

        rest = problem[closing_parenthesis+1:] if closing_parenthesis < len(problem)-1 else ''
        return solve_problem(f'{first_part}{inside_parenthesis}{rest}')


if __name__ == '__main__':
    with open('18.txt') as homework_file:
        solution_sum = 0
        for problem_str in homework_file:
            solution_sum += solve_problem(problem_str.strip().replace(' ', ''))
    print(solution_sum)


#%% part 2
class WeirdInt:
    """Switches multiplication with addition so that operator precedence is switched."""
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.__class__(self.value+other.value)

    def __add__(self, other):
        return self.__class__(self.value*other.value)

    def __repr__(self):
        return f'WeirdInt({self.value})'

    def __str__(self):
        return f'WeirdInt({self.value})'


if __name__ == '__main__':
    with open('18.txt') as homework_file:
        solution_sum = 0
        for problem_str in homework_file:
            problem_str = problem_str.replace(' * ', '+')
            problem_str = problem_str.replace(' + ', '*')
            for i in range(1, 10):
                problem_str = problem_str.replace(str(i), f'WeirdInt({i})')
            solution_sum += eval(problem_str).value
    print(solution_sum)
