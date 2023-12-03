numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def is_number_substring(line, ends_with=False):
    for number in numbers.keys():
        if ends_with:
            if number.endswith(line):
                return True
        else:
            if number.startswith(line):
                return True
    return False


def get_number_from_line(line):
    buf = ""
    res = 0
    for c in line:
        if c.isdigit():
            res += int(c) * 10
            break
        buf += c
        if is_number_substring(buf):
            if buf in numbers.keys():
                res += numbers[buf] * 10
                break
        else:
            buf = buf[1:]
    buf = ""
    for c in line[::-1]:
        if c.isdigit():
            res += int(c)
            break
        buf = c + buf
        if is_number_substring(buf, ends_with=True):
            if buf in numbers.keys():
                res += numbers[buf]
                break
        else:
            buf = buf[:-1]
    return res


def get_calibration_number(lines):
    res = 0
    for line in lines:
        line = line.strip()
        res += get_number_from_line(line)
    return res


if __name__ == "__main__":
    data = open("input/day_1_part_2.txt", "r")
    res = get_calibration_number(data)
    print(res)
    data.close()
