"""
Advent of Code 2020: day 09
"""


def read_in_puzzle(path_puzzle):
    y = []
    f = open(path_puzzle, "r")
    for x in f:
        y.append(int(str.rstrip(x)))
    return y


def main_1(x, len_preamble=25):
    for idx in range(len_preamble, len(x)):
        actual_number = x[idx]
        preamble_relative = x[idx-len_preamble: idx]
        flag_sum_possible = sum_possible(sorted(preamble_relative), actual_number)

        if not flag_sum_possible:
            return x[idx]

    return -1


def sum_possible(preamble_relative, actual_number):
    for idx_1 in range(0, len(preamble_relative)):
        for idx_2 in range(idx_1 + 1, len(preamble_relative)):
            if preamble_relative[idx_1] + preamble_relative[idx_2] == actual_number:
                return True
            elif preamble_relative[idx_1] + preamble_relative[idx_2] > actual_number:
                break
            else:
                pass
    return False


def main_2(x, number_weak):
    for idx_1 in range(0, len(x)):
        for idx_2 in range(idx_1 + 1, len(x)):
            actual_list = x[idx_1: idx_2]
            if sum(actual_list) == number_weak:
                return max(actual_list) + min(actual_list)
            elif sum(actual_list) > number_weak:
                break
            else:
                pass
    return None


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_09_puzzle.txt")
    print(puzzle)
    output_1 = main_1(puzzle)
    print(output_1)
    output_2 = main_2(puzzle, output_1)
    print(output_2)
