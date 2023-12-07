def find_wining_count(time, distnace):
    counter = 0
    for hold in range(1, time):
        distnace_on_hold = hold * (time - hold)
        if distnace < distnace_on_hold:
            counter += 1
    return counter


def count_winning_combinations(lines):
    _, *times = next(lines).split()
    _, *distance = next(lines).split()

    acc = 1
    for i in range(len(times)):
        acc *= find_wining_count(int(times[i]), int(distance[i]))
    return acc


if __name__ == "__main__":
    data = open("input/day_6.txt")
    print(count_winning_combinations(data))
    data.close()
