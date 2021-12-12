import numpy as np


# def find_bingoboard(boards: np.ndarray, numbers: np.ndarray) -> np.ndarray:
#     for n in numbers:
#         boards[boards == n] += 1j
#         filled = boards.imag > 0
#         full_row = np.sum(np.sum(filled, axis=0) == 5, axis=0)
#         if np.any(full_row):
#             return boards[..., full_row.astype(bool)]
#
#         full_col = np.sum(np.sum(filled, axis=1) == 5, axis=0)
#         if np.any(full_col):
#             return boards[:, full_col.astype(bool)]
#

def find_bingoboard(boards, numbers):
    for n in numbers:
        boards[boards == n] += 1j
        filled = boards.imag > 0
        full_row = np.sum(np.sum(filled, axis=0) == 5, axis=0)
        if np.any(full_row):
            return boards[..., full_row.astype(bool)], n

        full_col = np.sum(np.sum(filled, axis=1) == 5, axis=0)
        if np.any(full_col):
            return boards[:, full_col.astype(bool)], n


def find_last_bingoboard(boards, numbers):
    previous_full_row = np.zeros(boards.shape[-1])
    previous_full_col = np.zeros(boards.shape[-1])
    # TODO code is wrong. Returns multiple boards.
    for n in numbers:
        boards[boards == n] += 1j
        filled = boards.imag > 0
        full_row = np.sum(np.sum(filled, axis=0) == 5, axis=0)
        if np.all(full_row):
            last_board = full_row - previous_full_row
            return boards[..., last_board.astype(bool)], n

        full_col = np.sum(np.sum(filled, axis=1) == 5, axis=0)
        if np.all(full_col):
            last_board = full_col - previous_full_col
            return boards[..., last_board.astype(bool)], n

        previous_full_row = full_row
        previous_full_col = full_col


def part1(boards, numbers):
    bingo_board, n = find_bingoboard(boards, numbers)
    print(bingo_board[bingo_board.imag <= 0].real.sum() * n.real)


def part2(boards, numbers):
    bingo_board, n = find_last_bingoboard(boards, numbers)
    print(bingo_board[bingo_board.imag <= 0].real.sum() * n.real)


if __name__ == '__main__':
    with open('4.txt') as file:
        boardstr = file.read().split('\n\n')
        numbers = np.fromstring(boardstr[0], sep=',', dtype=complex)

    boards = np.zeros((5, 5, len(boardstr)-1), dtype=complex)
    for i, board in enumerate(boardstr[1:]):
        boards[..., i] = np.fromstring(board.replace('\n', ' '), sep=' ').reshape((5, 5))

    #part1(boards, numbers)
    part2(boards, numbers)