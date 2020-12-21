"""
Advent of Code 2020: day 08
"""


def read_in_puzzle(path_puzzle):
    intruction = []
    f = open(path_puzzle, "r")
    for x in f:
        line = x.split(" ")
        intruction.append([line[0], int(line[1])])
    return intruction


def main_1(x):
    accumulator = 0
    idx_actual_instruction = 0
    instruction_visited = {idx_actual_instruction}

    while True:
        # print(idx_actual_intruction)
        if x[idx_actual_instruction][0] == "nop":
            idx_next_instruction = idx_actual_instruction + 1
        elif x[idx_actual_instruction][0] == "acc":
            idx_next_instruction = idx_actual_instruction + 1
            accumulator = accumulator + x[idx_actual_instruction][1]
        elif x[idx_actual_instruction][0] == "jmp":
            idx_next_instruction = idx_actual_instruction + x[idx_actual_instruction][1]
        else:
            raise ValueError

        if idx_actual_instruction == len(x)-1:
            return accumulator, True
        elif idx_next_instruction in instruction_visited:
            return accumulator, False
        else:
            # print(x[idx_actual_instruction][0], accumulator)
            instruction_visited.add(idx_actual_instruction)
            idx_actual_instruction = idx_next_instruction % len(x)


def main_2(x):
    idx_last_modification = 0
    while True:
        # do modification
        x_modified = copy_list(x)
        for idx in range(idx_last_modification, len(x)):
            if x_modified[idx][0] == "jmp":
                x_modified[idx][0] = "nop"
                idx_last_modification = idx + 1
                break
            elif x_modified[idx][0] == "nop":
                x_modified[idx][0] = "jmp"
                idx_last_modification = idx + 1
                break
            else:
                pass
        # print(x_modified)
        # check modification
        accumulator, flag_finish = main_1(x_modified)
        if flag_finish:
            return accumulator


def copy_list(x):
    y = x.copy()
    for idx, sublist in enumerate(x):
        y[idx] = sublist.copy()
    return y


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_08_puzzle.txt")
    print(puzzle)
    print(main_1(puzzle))
    print(main_2(puzzle))
