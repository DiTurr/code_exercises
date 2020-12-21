"""
Advent of Code 2020: day 03
"""


def read_in_puzzle(path_puzzle):
    y = []
    f = open(path_puzzle, "r")
    for x in f:
        y.append(str.rstrip(x))
    return y


def main_1(x, move_right=3, move_down=1):
    num_trees = 0
    actual_horizontal_position = 0
    length_horizontal_template = len(x[0])
    print(x[0])
    for line in range(0, len(x)-1, move_down):
        actual_horizontal_position = (actual_horizontal_position + move_right) % length_horizontal_template
        actual_line = x[line + move_down]
        if actual_line[actual_horizontal_position] == "#":
            num_trees += 1
            # print(actual_line[:actual_horizontal_position]
            #       + "X"
            #       + actual_line[actual_horizontal_position + 1:])
        else:
            pass
            # print(actual_line[:actual_horizontal_position]
            #       + "O"
            #       + actual_line[actual_horizontal_position + 1:])

    return num_trees


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_03_puzzle.txt")
    output = main_1(puzzle, move_right=3, move_down=1)
    print(output)
    print("####################")
    output1 = main_1(puzzle, move_right=1, move_down=1)
    print(output1)
    output2 = main_1(puzzle, move_right=3, move_down=1)
    print(output2)
    output3 = main_1(puzzle, move_right=5, move_down=1)
    print(output3)
    output4 = main_1(puzzle, move_right=7, move_down=1)
    print(output4)
    output5 = main_1(puzzle, move_right=1, move_down=2)
    print(output5)
    print("####################")
    print(output1*output2*output3*output4*output5)
