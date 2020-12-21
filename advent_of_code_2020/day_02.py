"""
Advent of Code 2020: day 02
"""


def read_in_puzzle(path_puzzle):
    num_min = []
    num_max = []
    letter = []
    password = []
    f = open(path_puzzle, "r")
    for x in f:
        part = x.split(" ")
        num_min.append(int(part[0].split("-")[0]))
        num_max.append(int(part[0].split("-")[1]))
        letter.append(part[1][0])
        password.append(str.rstrip(part[2]))
    assert len(num_min) == len(num_max) == len(letter) == len(password)
    return num_min, num_max, letter, password


def main_1(num_min_list, num_max_list, letter_list, password_list):
    num_valid_passwords = 0
    for num_min, num_max, letter, password in zip(num_min_list, num_max_list, letter_list, password_list):
        num_letter_password = 0
        for letter_password in password:
            if letter == letter_password:
                num_letter_password += 1
        if num_min <= num_letter_password <= num_max:
            num_valid_passwords += 1
    return num_valid_passwords


def main_2(num_min_list, num_max_list, letter_list, password_list):
    num_valid_passwords = 0
    for num_min, num_max, letter, password in zip(num_min_list, num_max_list, letter_list, password_list):
        if (password[num_min-1] == letter and password[num_max-1] != letter) or \
                (password[num_min-1] != letter and password[num_max-1] == letter):
            num_valid_passwords += 1
    return num_valid_passwords


if __name__ == "__main__":
    num_min_puzzle, num_max_puzzle, letter_puzzle, password_puzzle = \
        read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_02_puzzle.txt")
    output = main_1(num_min_puzzle, num_max_puzzle, letter_puzzle, password_puzzle)
    print(output)
    output = main_2(num_min_puzzle, num_max_puzzle, letter_puzzle, password_puzzle)
    print(output)
