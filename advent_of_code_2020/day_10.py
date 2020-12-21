"""
Advent of Code 2020: day 10
"""


def read_in_puzzle(path_puzzle):
    y = set()
    f = open(path_puzzle, "r")
    for x in f:
        y.add(int(str.rstrip(x)))
    return y


def main_1(x, charging_outlet=0):
    actual_charging_outlet = charging_outlet
    max_outlet = max(x)
    num_diff_1 = 0
    num_diff_3 = 0
    while True:
        # check actual outlet
        if actual_charging_outlet+1 in x:
            new_charging_outlet = actual_charging_outlet+1
            num_diff_1 += 1
        elif actual_charging_outlet+3 in x:
            new_charging_outlet = actual_charging_outlet+3
            num_diff_3 += 1
        else:
            return [False, num_diff_1*(num_diff_3+1)]

        # Update outlet
        print(actual_charging_outlet, new_charging_outlet)
        if new_charging_outlet == max_outlet:
            break
        else:
            actual_charging_outlet = new_charging_outlet

    return [True, num_diff_1*(num_diff_3+1)]


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_10_puzzle.txt")
    print(puzzle)
    output = main_1(puzzle)
    print(output)
