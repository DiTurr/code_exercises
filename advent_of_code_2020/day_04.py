"""
Advent of Code 2020: day 04
"""


def read_in_puzzle(path_puzzle):
    f = open(path_puzzle, "r")
    batch_file = []
    string_passport = ""
    for line in f:
        actual_line = str.rstrip(line)
        # still data from actual password
        if actual_line != "":
            string_passport = string_passport + " " + actual_line if string_passport != "" else actual_line

        # blank line --> new password will come next, so we preprocess the actual password
        else:
            data = string_passport.split(" ")
            passport = {}
            for field in data:
                name_field = field[0:3]
                data_field = field[4:]
                passport[name_field] = data_field
            batch_file.append(passport)
            string_passport = ""
    return batch_file


def main_1(x):
    fields_main = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    fields_opt = {"cid"}
    num_valid_passport = 0
    for passport in x:
        if fields_main <= passport.keys() or fields_main.union(fields_opt) <= passport.keys():
            num_valid_passport += 1
    return num_valid_passport


def main_2(x):
    fields_main = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    fields_opt = {"cid"}
    num_valid_passport = 0
    for passport in x:
        #   are correct with just the main fields
        if fields_main <= passport.keys() or fields_main.union(fields_opt) <= passport.keys():
            flag_validity = True
            for name_field in passport.keys():
                if name_field == "byr":
                    if 1920 <= int(passport["byr"]) <= 2002:
                        pass
                    else:
                        flag_validity = False
                        break
                elif name_field == "iyr":
                    if 2010 <= int(passport["iyr"]) <= 2020:
                        pass
                    else:
                        flag_validity = False
                        break
                elif name_field == "eyr":
                    if 2020 <= int(passport["eyr"]) <= 2030:
                        pass
                    else:
                        flag_validity = False
                        break
                elif name_field == "hgt":
                    if passport["hgt"][-2:] == "cm":
                        if 150 <= int(passport["hgt"][0:-2]) <= 193:
                            pass
                        else:
                            flag_validity = False
                            break
                    elif passport["hgt"][-2:] == "in":
                        if 59 <= int(passport["hgt"][0:-2]) <= 76:
                            pass
                        else:
                            flag_validity = False
                            break
                    else:
                        flag_validity = False
                        break
                elif name_field == "hcl":
                    if passport["hcl"][0] == "#" and len(passport["hcl"]) == 7 and passport["hcl"][1:].isalnum():
                        pass
                    else:
                        flag_validity = False
                        break
                elif name_field == "ecl":
                    if passport["ecl"] == "amb" or passport["ecl"] == "blu" or \
                            passport["ecl"] == "brn" or passport["ecl"] == "gry" or \
                            passport["ecl"] == "grn" or passport["ecl"] == "hzl" or \
                            passport["ecl"] == "oth":
                        pass
                    else:
                        flag_validity = False
                        break
                elif name_field == "pid":
                    if len(passport["pid"]) == 9 and passport["pid"].isnumeric():
                        pass
                    else:
                        flag_validity = False
                        break
                elif name_field == "cid":
                    pass
                else:
                    raise ValueError
            if flag_validity:
                num_valid_passport += 1
        # field name is not correct
        else:
            pass
    return num_valid_passport


if __name__ == "__main__":
    puzzle = read_in_puzzle("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_04_puzzle.txt")
    print(main_1(puzzle))
    print(main_2(puzzle))
