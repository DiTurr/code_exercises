"""
Advent of Code 2020: day 07
"""


def read_in_puzzle(path_puzzle):
    y = {}
    f = open(path_puzzle, "r")
    for x in f:
        words = str.rstrip(x).split(" ")
        actual_bag = words[0] + "_" + words[1]
        inner_bags = {}
        for idx, word in enumerate(words):
            if word.isnumeric():
                inner_bags[words[idx+1] + "_" + words[idx+2]] = int(word)
        y[actual_bag] = inner_bags
    return y


def main_1(x, search_bag):
    total_container_bags = set()
    inner_bags = {search_bag}
    outer_bags = set()
    while True:
        for bag in x.keys():
            outer_bags_tmp = inner_bags.intersection(set(x[bag].keys()))
            if len(outer_bags_tmp) != 0:
                outer_bags.add(bag)
                total_container_bags.add(bag)
        # print(outer_bags)
        # print(total_container_bags)
        if len(outer_bags) == 0:
            break
        inner_bags = outer_bags
        outer_bags = set()
    return len(total_container_bags)


def main_2(x, search_bag):
    outer_bags = {search_bag: 1}
    inner_bags = {}
    num_total_bags = 0
    while True:
        for outer_bag in outer_bags:
            inner_bags_tmp = {}
            if len(x[outer_bag].keys()) > 0:
                for inner_bag in x[outer_bag].keys():
                    inner_bags_tmp[inner_bag] = x[outer_bag][inner_bag] * outer_bags[outer_bag]
                inner_bags = merge_dict(inner_bags, inner_bags_tmp)
                if len(inner_bags_tmp) > 0:
                    num_total_bags += outer_bags[outer_bag]
            else:
                num_total_bags += outer_bags[outer_bag]
                pass

        if len(inner_bags) == 0:
            break

        print(num_total_bags)
        print(inner_bags)
        outer_bags = inner_bags
        inner_bags = {}

    # actual implementation takes also into account the first bag (mother bag)
    return num_total_bags - 1


def merge_dict(dict1, dict2):
    for key in dict1.keys():
        if key in dict2.keys():
            dict2[key] = dict2[key] + dict1[key]
        else:
            dict2[key] = dict1[key]
    return dict2


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_07_puzzle.txt")
    # print(puzzle)
    print(main_1(puzzle, "shiny_gold"))
    print(main_2(puzzle, "shiny_gold"))

