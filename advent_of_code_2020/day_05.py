"""
Advent of Code 2020: day 05
"""


def read_in_puzzle(path_puzzle):
    y = []
    f = open(path_puzzle, "r")
    for x in f:
        y.append(str.rstrip(x))
    return y


def main_1(x):
    list_id = []
    for code in x:
        assert len(code) == 10
        row_possible = [idx for idx in range(0, 128)]
        column_possible = [idx for idx in range(0, 8)]
        for idx, character in enumerate(code):
            # row information
            if idx < 7:
                if character == "F":
                    row_possible = row_possible[0:len(row_possible)//2]
                elif character == "B":
                    row_possible = row_possible[len(row_possible)//2:]
                else:
                    raise ValueError

            # seat information;
            else:
                if character == "L":
                    column_possible = column_possible[0:len(column_possible)//2]
                elif character == "R":
                    column_possible = column_possible[len(column_possible)//2:]
                else:
                    raise ValueError
        list_id.append(row_possible[0] * 8 + column_possible[0])
    return list_id


def main_2(x):
    list_id_sorted = sorted(x)
    for idx in range(1, len(list_id_sorted)-1):
        if list_id_sorted[idx] + 1 == list_id_sorted[idx+1]:
            pass
        else:
            return list_id_sorted[idx] + 1


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_05_puzzle.txt")
    print(max(main_1(puzzle)))
    print(main_2(main_1(puzzle)))
