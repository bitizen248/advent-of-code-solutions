from day_6.part_1 import find_wining_count


def count_winning_combinations(lines):
    _, *times = next(lines).split()
    _, *distance = next(lines).split()
    times = int("".join(times))
    distance = int("".join(distance))
    print(times)
    print(distance)
    return find_wining_count(times, distance)


if __name__ == "__main__":
    data = open("input/day_6.txt")
    print(count_winning_combinations(data))
    data.close()
