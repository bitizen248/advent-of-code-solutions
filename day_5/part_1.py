def create_map(destination, source, range_size):
    return (source, source + range_size - 1, destination)


def orginize_map(maps):
    return sorted(maps, key=lambda x: x[0])


def find_value_in_map(value, maps):
    for start, end, destination in maps:
        if value >= start and value <= end:
            return (value - start) + destination
    return value


def parse_ranges(line):
    destination, source, range_size = line.split()
    return int(destination), int(source), int(range_size)


def parse_seeds(line):
    _, line = line.split(":")
    return [int(seed) for seed in line.split()]


def find_minumal_seeds(lines):
    seeds = parse_seeds(next(lines))
    res = seeds.copy()
    next(lines)
    skip_line = False
    current_map = list()
    current_map_name = ""
    for line in lines:
        line = line.strip()
        if not line:
            current_map = orginize_map(current_map)
            for i in range(len(res)):
                res[i] = find_value_in_map(res[i], current_map)
            current_map = list()
            continue
        if line.endswith("map:"):
            continue
        destination, source, range_size = parse_ranges(line)
        current_map.append(create_map(destination, source, range_size))
    print(res)
    return min(res)


if __name__ == "__main__":
    data = open("input/day_5.txt", "r")
    print(find_minumal_seeds(data))
    data.close()
