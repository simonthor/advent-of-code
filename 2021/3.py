import numpy as np


def bin2dec(binarray: np.ndarray) -> float:
    return np.sum(2 ** np.arange(binarray.shape[-1] - 1, -1, -1) * binarray)


def part1(numbers: np.ndarray) -> float:
    gamma = bin2dec(np.sum(numbers == 1, axis=0) > (numbers.shape[0] / 2))
    epsilon = int(bin((1 << numbers.shape[1]) - 1 - gamma), 2)  # binary not on the int
    return epsilon * gamma


def ogr(numbers):
    selected_numbers = numbers.copy()
    for i in range(numbers.shape[-1]):
        col = selected_numbers[:, i]
        common = np.sum(col == 1) >= (selected_numbers.shape[0] / 2)
        selected_numbers = selected_numbers[col == common, :]
        if selected_numbers.shape[0] == 1:
            break
    return bin2dec(selected_numbers)


def csr(numbers):
    selected_numbers = numbers.copy()
    for i in range(numbers.shape[-1]):
        col = selected_numbers[:, i]
        common = np.sum(col == 1) < (selected_numbers.shape[0] / 2)
        selected_numbers = selected_numbers[col == common, :]
        if selected_numbers.shape[0] == 1:
            break
    return bin2dec(selected_numbers)


def part2(numbers: np.ndarray) -> float:
    return ogr(numbers) * csr(numbers)


if __name__ == '__main__':
    numbers = np.genfromtxt('3.txt', delimiter=1, dtype=np.uint32)
    print(part1(numbers))
    print(part2(numbers))

