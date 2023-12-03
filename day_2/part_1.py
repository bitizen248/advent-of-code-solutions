from day_2.common import parse_blocks_line
from day_2.common import parse_game_line


def is_bag_possible(blocks, bag):
    for pull in blocks:
        for color, count in pull.items():
            if color not in bag:
                return False
            if bag[color] < count:
                return False
    return True


def find_sum_possible_id(lines, bag_line):
    res = 0
    bag = parse_blocks_line(bag_line)
    for line in lines:
        line = line.strip()
        game_info = parse_game_line(line)
        if is_bag_possible(game_info["blocks"], bag):
            res += game_info["game_id"]
    return res


if __name__ == "__main__":
    lines = open("input/day_2.txt")
    print(find_sum_possible_id(lines, "12 red, 13 green, 14 blue"))
    lines.close()
