def create_map(destination, source, range_size):
    return (source, source + range_size - 1, destination - source)


def orginize_map(maps):
    return sorted(maps, key=lambda x: x[0])


def find_value_in_map(value_range, maps):
    res = list()
    value_start, value_end = value_range
    finished = False
    for start, end, shift in maps:
        if value_start < start:
            res.append((value_start, start))
            value_start = start + 1
        if value_start > end:
            continue
        if value_start >= start:
            if value_start >= end:
                continue
            if value_end <= end:
                res.append((value_start + shift, value_end + shift))
                value_start = value_end
                finished = True
                break
            else:
                res.append((value_start + shift, end + shift))
                value_start = end + 1

    if not finished:
        res.append((value_start, value_end))

    return res


def parse_ranges(line):
    destination, source, range_size = line.split()
    return int(destination), int(source), int(range_size)


def parse_seeds(line):
    _, line = line.split(":")
    line = line.split()
    res = list()
    for i in range(0, len(line), 2):
        start = int(line[i])
        res.append((start, start + int(line[i + 1]) - 1))
    return res


def find_minumal_seeds(lines):
    seeds = parse_seeds(next(lines))
    res = seeds.copy()
    res = orginize_map(res)
    res_buf = list()
    next(lines)
    current_map = list()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            current_map = orginize_map(current_map)
            for i in range(len(res)):
                res_buf.extend(find_value_in_map(res[i], current_map))
            res = res_buf.copy()
            res = orginize_map(res)
            res_buf = list()
            current_map = list()
            continue
        if line.endswith("map:"):
            continue
        destination, source, range_size = parse_ranges(line)
        current_map.append(create_map(destination, source, range_size))
    res = [p[0] for p in res]
    return min(res)


if __name__ == "__main__":
    data = open("input/day_5.txt", "r")
    print(find_minumal_seeds(data))
    data.close()
