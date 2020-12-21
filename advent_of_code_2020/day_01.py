"""
Advent of Code 2020: day 01
"""


def read_in_puzzle(path_puzzle):
    y = []
    f = open(path_puzzle, "r")
    for x in f:
        y.append(int(str.rstrip(x)))
    return y


def main(x):
    num_samples = len(x)
    for idx_1 in range(0, num_samples):
        for idx_2 in range(idx_1 + 1, num_samples):
            for idx_3 in range(idx_2 + 1, num_samples):
                if x[idx_1] + x[idx_2] + x[idx_3] == 2020:
                    print(x[idx_1], x[idx_2], x[idx_3])
                    return x[idx_1] * x[idx_2] * x[idx_3]
    return None


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_01_puzzle.txt")
    output = main(puzzle)
    print(output)
