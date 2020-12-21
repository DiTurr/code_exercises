"""
Advent of Code 2020: day 06
"""


def read_in_puzzle(path_puzzle):
    list_group = []
    list_total = []
    f = open(path_puzzle, "r")
    for line in f:
        # if line is no ""
        if str.rstrip(line) != "":
            list_group.append(str.rstrip(line))
        else:
            list_total.append(list_group)
            list_group = []
    return list_total


def main_1(x):
    list_positive_answer = []
    for group in x:
        positive_answer_group = set()
        for passenger in group:
            for answer in passenger:
                positive_answer_group.add(answer)

        # append postive answer of actual group
        list_positive_answer.append(positive_answer_group)

    # return total of positive answers
    sum_positive_answer = 0
    for positive_answer_group in list_positive_answer:
        sum_positive_answer += len(positive_answer_group)
    return sum_positive_answer


def main_2(x):
    list_total_common_answers = []
    for group in x:
        # answer of the first passenger of the group
        common_answers_group = get_set_of_answers(group[0])
        for passenger in group:
            answer_actual_passenger = get_set_of_answers(passenger)
            common_answers_group = common_answers_group.intersection(answer_actual_passenger)

        # append postive answer of actual group
        list_total_common_answers.append(common_answers_group)

    # return total of common answers
    sum_common_answer = 0
    for common_answers_group in list_total_common_answers:
        sum_common_answer += len(common_answers_group)
    return sum_common_answer


def get_set_of_answers(list_answers):
    set_answer_group = set()
    for answer in list_answers:
        set_answer_group.add(answer)
    return set_answer_group


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_06_puzzle.txt")
    print(puzzle)
    print(main_1(puzzle))
    print(main_2(puzzle))
