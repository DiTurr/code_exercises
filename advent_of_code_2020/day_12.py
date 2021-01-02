"""
Advent of Code 2020: day 12
"""


def read_in_puzzle(path_puzzle):
    file = open(path_puzzle, "r")
    direcction = []
    distance = []
    for line in file:
        direcction.append(str.rstrip(line)[0])
        distance.append(str.rstrip(line)[1:])
    assert len(direcction) == len(distance)
    return direcction, distance


def main_1(direction, distance):
    direction_actual = 0
    position_actual = [0, 0]
    for idx, (direction_step, distance_step) in enumerate(zip(direction, distance)):
        if direction_step == "N":
            position_actual[1] = position_actual[1] + int(distance_step)
        elif direction_step == "S":
            position_actual[1] = position_actual[1] - int(distance_step)
        elif direction_step == "E":
            position_actual[0] = position_actual[0] + int(distance_step)
        elif direction_step == "W":
            position_actual[0] = position_actual[0] - int(distance_step)
        elif direction_step == "L":
            direction_actual = direction_actual + int(distance_step)
        elif direction_step == "R":
            direction_actual = direction_actual - int(distance_step)
        else:
            assert direction_step == "F"
            if direction_actual == 0:
                position_actual[0] = position_actual[0] + int(distance_step)
            elif direction_actual == 90:
                position_actual[1] = position_actual[1] + int(distance_step)
            elif direction_actual == 180:
                position_actual[0] = position_actual[0] - int(distance_step)
            elif direction_actual == 270:
                position_actual[1] = position_actual[1] - int(distance_step)
            else:
                print(direction_actual)
                raise ValueError

        if direction_actual < 0:
            direction_actual = direction_actual + 360
        if direction_actual >= 360:
            direction_actual = direction_actual % 360
        # print(idx)
        # print(position_actual)
        # print(direction_actual)
        # print("#####")
    return abs(position_actual[0]) + abs(position_actual[1])


def main_2(direction, distance):
    position_ship_actual = [0, 0]
    position_relative_waypoint_actual = [10, 1]
    for idx, (direction_step, distance_step) in enumerate(zip(direction, distance)):
        if direction_step == "N":
            position_relative_waypoint_actual[1] = position_relative_waypoint_actual[1] + int(distance_step)
        elif direction_step == "S":
            position_relative_waypoint_actual[1] = position_relative_waypoint_actual[1] - int(distance_step)
        elif direction_step == "E":
            position_relative_waypoint_actual[0] = position_relative_waypoint_actual[0] + int(distance_step)
        elif direction_step == "W":
            position_relative_waypoint_actual[0] = position_relative_waypoint_actual[0] - int(distance_step)
        elif direction_step == "L":
            if distance_step == "0":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] =\
                    position_relative_waypoint_actual[0], position_relative_waypoint_actual[1]
            elif distance_step == "90":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] = \
                    - position_relative_waypoint_actual[1], position_relative_waypoint_actual[0]
            elif distance_step == "180":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] = \
                    - position_relative_waypoint_actual[0], - position_relative_waypoint_actual[1]
            elif distance_step == "-90" or distance_step == "270":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] = \
                    position_relative_waypoint_actual[1], - position_relative_waypoint_actual[0]
            else:
                raise ValueError
        elif direction_step == "R":
            if distance_step == "0":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] =\
                    position_relative_waypoint_actual[0], position_relative_waypoint_actual[1]
            elif distance_step == "90":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] = \
                    position_relative_waypoint_actual[1], - position_relative_waypoint_actual[0]
            elif distance_step == "180":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] = \
                    - position_relative_waypoint_actual[0], - position_relative_waypoint_actual[1]
            elif distance_step == "-90" or distance_step == "270":
                position_relative_waypoint_actual[0], position_relative_waypoint_actual[1] = \
                    - position_relative_waypoint_actual[1], position_relative_waypoint_actual[0]
            else:
                raise ValueError
        else:
            assert direction_step == "F"
            position_ship_actual[0] = position_ship_actual[0] + \
                                      position_relative_waypoint_actual[0] * int(distance_step)
            position_ship_actual[1] = position_ship_actual[1] + \
                                      position_relative_waypoint_actual[1] * int(distance_step)

        # print(idx)
        # print(position_ship_actual)
        # print(position_relative_waypoint_actual)
        # print("#####")

    return abs(position_ship_actual[0]) + abs(position_ship_actual[1])


if __name__ == "__main__":
    puzzle_direction, puzzle_distance = read_in_puzzle\
        ("/home/ditu/Documents/03_Projects/code_exercises/advent_of_code_2020/day_12_puzzle.txt")
    print(puzzle_direction, puzzle_distance)
    print(main_1(puzzle_direction, puzzle_distance))
    print(main_2(puzzle_direction, puzzle_distance))
