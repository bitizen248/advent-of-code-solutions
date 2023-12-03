def get_number_from_line(line):
    line = line.strip()
    res = 0
    for c in line:
        if c.isdigit():
            res += int(c) * 10
            break
    for c in line[::-1]:
        if c.isdigit():
            res += int(c)
            break
    return res


def get_calibration_number(data):
    res = 0
    for line in data:
        res += get_number_from_line(line)
    return res


if __name__ == "__main__":
    data = open("input/day_1_part_1.txt", "r")
    res = get_calibration_number(data)
    print(res)
    data.close()
