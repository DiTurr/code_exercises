"""
Advent of Code 2020: day 11
"""
import numpy as np


def read_in_puzzle(path_puzzle):
    file = open(path_puzzle, "r")
    map_character = {"#": -1, ".": 0, "L": 1}
    y = []
    for line in file:
        y_line = []
        for character in str.rstrip(line):
            y_line.append(map_character[character])
        y.append(y_line)
    return np.array(y)


def main_1(x):
    x_last = np.copy(x)
    x_actual = np.copy(x)
    while True:
        for idx_row in range(x.shape[0]):
            for idx_column in range(x.shape[1]):
                seat = x_last[idx_row, idx_column]
                surroundings = x_last[max(min(idx_row - 1, x.shape[0]), 0):
                                      max(min(idx_row + 2, x.shape[0]), 0),
                                      max(min(idx_column - 1, x.shape[1]), 0):
                                      max(min(idx_column + 2, x.shape[1]), 0)]
                # seat if not ocupied
                if seat == 1:
                    # if minimunm of surrounding if 0 --> no occupied seat in the surroundings
                    if np.min(surroundings) >= 0:
                        x_actual[idx_row, idx_column] = -1
                # seat is ocupied
                elif seat == -1:
                    if np.count_nonzero(surroundings == -1) >= 5:
                        x_actual[idx_row, idx_column] = 1
                # position is actually floor
                else:
                    assert seat == 0
        # check if they are equal. If so, break
        if np.array_equal(x_actual, x_last):
            break
        # update the seat layout
        x_last = np.copy(x_actual)
    # return
    return np.count_nonzero(x_actual == -1)


def main_2(x):
    x_last = np.copy(x)
    x_actual = np.copy(x)
    while True:
        for idx_row in range(x.shape[0]):
            for idx_column in range(x.shape[1]):
                seat = x_last[idx_row, idx_column]
                surroundings = []
                surroundings_1 = x_last[idx_row, 0:idx_column+1]
                surroundings_2 = np.diag(x_last[0:idx_row+1, 0:idx_column+1])
                surroundings_3 = x_last[0:idx_row+1, idx_column]
                surroundings_4 = np.diag(x_last[idx_row:-1, 0:idx_column+1])
                surroundings_5 = x_last[idx_row, idx_column:-1]
                surroundings_6 = np.diag(x_last[idx_row:-1, idx_column:-1])
                surroundings_7 = x_last[idx_row:-1, idx_column]
                surroundings_8 = np.diag(x_last[0:idx_row, idx_column:-1])

                # seat if not ocupied
                if seat == 1:
                    # if minimunm of surrounding if 0 --> no occupied seat in the surroundings
                    if np.min(surroundings) >= 0:
                        x_actual[idx_row, idx_column] = -1
                # seat is ocupied
                elif seat == -1:
                    if np.count_nonzero(surroundings == -1) >= 6:
                        x_actual[idx_row, idx_column] = 1
                # position is actually floor
                else:
                    assert seat == 0
        # check if they are equal. If so, break
        if np.array_equal(x_actual, x_last):
            break
        # update the seat layout
        x_last = np.copy(x_actual)
    # return
    return np.count_nonzero(x_actual == -1)


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_11_puzzle.txt")
    print(main_1(puzzle))
    print(main_2(puzzle))
