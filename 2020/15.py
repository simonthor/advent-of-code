import numba as nb
import numpy as np

@nb.njit
def elf_game(starting_numbers, max_iter):
    """Gives the last number in the memory elf game.
    The non-pythonic declaration of the dict is required for numba to work.
    numba gives a 3x performance improvement."""
    numbers = dict()
    for i, number in enumerate(starting_numbers):
        numbers[number] = i

    current_number = 0
    for i in range(len(starting_numbers), max_iter-1):
        if current_number in numbers:
            last_number_appearance = numbers[current_number]
            numbers[current_number] = i
            current_number = i - last_number_appearance
        else:
            numbers[current_number] = i
            current_number = 0
    return current_number


if __name__ == '__main__':
    starting_numbers = np.array([14, 8, 16, 0, 1, 17], dtype=np.int64)
    # part 1
    print(elf_game(starting_numbers, 2020))

    # part 2
    print(elf_game(starting_numbers, 30_000_000))
