from day_2.common import parse_game_line


def get_game_power(blocks):
    power = dict()
    for pull in blocks:
        for color, count in pull.items():
            if color not in power or power[color] < count:
                power[color] = count
    res = 1
    for number in power.values():
        res *= number
    return res


def sum_games_powers(lines):
    res = 0
    for line in lines:
        line = line.strip()
        game_info = parse_game_line(line)
        res += get_game_power(game_info["blocks"])
    return res


if __name__ == "__main__":
    lines = open("input/day_2.txt")
    print(sum_games_powers(lines))
    lines.close()
